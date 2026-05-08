# Autonomous Forensic Engine

Deepseek-cybersec is a specialized cybersecurity AI assistant built on top of a fine-tuned **Deepseek-cybersec-33b-instruct** model. It is designed to automate malware intent analysis and identify malicious patterns in obfuscated code with high precision.

## 🚀 Key Features
- **Deep Intent Analysis:** Unlike standard LLMs, Deepseek-cybersec is fine-tuned to recognize the underlying intent of code, not just its syntax.
- **Malware Detection:** Specifically trained to identify Discord webhooks, data exfiltration, and obfuscated Java/Python payloads.
- **Forensic Reports:** Generates structured observations and risk levels (CLEAN / SUSPICIOUS / MALICIOUS).

## 🧠 Model Details
- **Base Model:** DeepSeek-coder-33B-Instruct
- **Fine-tuning Method:** LoRA (Low-Rank Adaptation)
- **Specialization:** Cybersecurity forensics & Malware analysis
- **Hugging Face Repository:** [TeanShow/Deepseek-cybersec-33b-instruct](https://huggingface.co/TeanShow/Deepseek-cybersec-33b-instruct)

## 🏗️ Technical Infrastructure
The model was trained using state-of-the-art high-performance GPU infrastructure:
- **Hardware:** AMD Instinct™ MI300X Accelerators (ROCm stack).
- **Training duration:** Integrated Loss monitoring and optimized weights backup.
- **Frameworks:** Axolotl, PEFT, Transformers, BitAndBytes.

## 📊 Training Results
Training logs show a consistent loss reduction, ensuring the model effectively learned the specific cybersecurity dataset patterns without overfitting.
<img width="1811" height="791" alt="image" src="https://github.com/user-attachments/assets/3ae8dd2e-f1f1-4957-b694-08bbb58adb15" />


## 💻 Installation & Setup

1. **Download weights from HuggingFace**

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```
3. **Run :**
```bash
streamlit run demo.py
```
