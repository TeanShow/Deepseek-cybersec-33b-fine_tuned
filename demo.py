
import torch
import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
base_model_path = "deepseek-ai/deepseek-coder-33b-instruct" 
lora_path = "./model-out-phase2/checkpoint-50"
@st.cache_resource
def load():
    tokenizer = AutoTokenizer.from_pretrained(base_model_path)
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_path, 
        torch_dtype=torch.bfloat16, 
        device_map="auto"
    )
    model = PeftModel.from_pretrained(base_model, lora_path)
    return tokenizer, model
tokenizer, model = load()
def analyze(user_code):
    prefix = "### Deepseek-cybersec FORENSIC ANALYSIS REPORT\n**VERDICT:**"
    prompt = (
	"Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n"
        "### Instruction:\n"
        "SYSTEM ROLE: You are Deepseek-cybersec, a Senior Malware Analyst. "
        "Analyze the code for ACTUAL malicious intent. Do not confuse administrative scripts with malware. "
        "Check for obfuscation, C2 patterns, and unauthorized data access. "
        "VERDICT OPTIONS: [CLEAN, SUSPICIOUS, MALICIOUS].\n\n"
        f"CODE:\n{user_code}\n\n"
        "### Response:\n" + prefix
    )
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    prompt_length = inputs.input_ids.shape[1]
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=800, temperature=0.1, repetition_penalty=1.1)
    new_tokens = outputs[0][prompt_length:]
    raw_response = tokenizer.decode(new_tokens, skip_special_tokens=True)
    clean_text = raw_response.replace("Ċ", "\n").replace("Ġ", " ").strip()
    stop_markers = ["<jupyter_text>", "<jupyter_code>", "openai.api_key", "import langchain", "## Prompt"]
    for marker in stop_markers:
        if marker in clean_text:
            clean_text = clean_text.split(marker)[0].strip()
    return prefix + clean_text
st.title("Deepseek-33b-cybersec: Autonomous Forensic Engine")
code_input = st.text_area("Paste code for audit:", height=300)
if st.button("RUN DEEP AUDIT"):
    with st.spinner("Deobfuscating causal pathways..."):
        result = analyze(code_input)
        st.markdown(result)
