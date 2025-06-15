# 🧠 AI-Powered Network Troubleshooter

A real-time, AI-assisted tool that continuously monitors network-connected devices, diagnoses their status, and provides intelligent suggestions using Google's Gemini AI. Built with Flask and designed for IT professionals, learners, and automation enthusiasts.

---

## 🚀 Features

- ✅ Live monitoring of device reachability and latency
- 🧠 AI explanations using Gemini (short, beginner-friendly tips)
- 🔁 Auto-refresh backend for live status updates
- 🌐 Web dashboard with clean interface
- 🔌 Ready for voice assistant integration (Vapi, coming soon)
- 📄 Logs and AI diagnostics for each host

---

## 📁 Project Structure

ai-network-troubleshooter/
├── api.py # Flask backend
├── ai_nlp.py # Gemini-based AI logic
├── templates/
│ └── index.html # HTML UI
├── static/
│ └── styles.css # (Optional) UI styles
├── requirements.txt # Dependencies
├── README.md
└── .gitignore

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/ai-network-troubleshooter.git
cd ai-network-troubleshooter

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate        # On Windows
source .venv/bin/activate     # On Linux/Mac

### 3. Install dependencies
```bash
pip install -r requirements.txt

### 4. Set your Gemini API key
```bash
export GEMINI_API_KEY=your_key_here       # or add to .env file

### 5. 5. Start the app
```bash
python api.py

Open in browser: http://localhost:5000

## 🛠️ Tech Stack
- Python (Flask)
- Gemini AI (Google Generative AI)
- JavaScript (AJAX for status polling)
- HTML/CSS (Jinja2 templates)

## 🔮 Coming Soon
- 🗣️ Voice Agent Control (Vapi AI + n8n bridge)
- 📊 Live charts for latency & health
- 🧾 PDF report export
- 📩 Alerts on failure (email/Slack)
- 📂 Bulk import devices via CSV/JSON

## 👤 Author
Abdulkabeer-W
🔗 GitHub

## 📄 License
MIT License — Free to use, improve, and share with credit.