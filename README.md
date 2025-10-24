# 🚨 Incident Response Playbook Automator (Python)

A Python-based command-line tool that simulates a **first-response automation workflow** for cybersecurity incidents.  
It collects live system data, performs basic threat intelligence checks via VirusTotal, and generates structured reports for triage.

---

## 🧠 Why I Built It
In a real SOC environment, the first few minutes after detecting a possible breach are critical.  
This tool automates those repetitive triage steps — checking processes, network connections, and known malicious hashes — so analysts can focus on deeper investigation.

---

## ⚙️ Features
✅ Captures live system and network info via **psutil**  
✅ Integrates with **VirusTotal API** for hash reputation lookups  
✅ Colorized summary using **Rich**  
✅ Exports structured reports in **JSON** format  
✅ Easily extendable for more threat feeds or YARA integration  

---

## 🧰 Setup
```bash
git clone https://github.com/<your-username>/incident-response-automator.git
cd incident-response-automator
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # (Windows)
pip install -r requirements.txt
