# 🧠 AI-Powered Network Troubleshooter

A real-time AI-assisted tool to monitor multiple devices in a network, detect issues like unreachable hosts or high latency, and provide smart suggestions using Gemini AI. Built with Flask and integrated with Google’s Generative AI, this project is ideal for IT enthusiasts, network admins, and learners.

---

## 🚀 Features

- ✅ Monitor devices for status (online/offline) and latency
- 📡 Real-time diagnostics of network health
- 🧠 AI-generated explanations using Gemini (Google Generative AI)
- 📊 Web dashboard to display live results
- 📁 Log file to trace request-response history
- 🔌 Modular structure for easy integration with voice (Vapi) or n8n
- 🧪 Supports expansion for alert systems and live graphs

---

## 🧱 Tech Stack

- **Python** + **Flask** – Backend REST API
- **Gemini API** – Google Generative AI for explanations
- **JavaScript + AJAX** – Live frontend refresh
- **HTML/CSS** – UI (Jinja2 templating)
- *(Optional integrations coming: Vapi, n8n, alerts)*

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-network-troubleshooter.git
cd ai-network-troubleshooter
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate        # On Windows
source .venv/bin/activate     # On Linux/Mac
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your Gemini API key

```bash
export GEMINI_API_KEY=your_key_here       # or add to .env file
```
### 5. 5. Start the app

```bash
python api.py
```
---

## Open in browser: http://localhost:5000

---

## 🛠️ Tech Stack
- Python (Flask)
- Gemini AI (Google Generative AI)
- JavaScript (AJAX for status polling)
- HTML/CSS (Jinja2 templates)

---

## 🔮 Coming Soon
- 🗣️ Voice Agent Control (Vapi AI + n8n bridge)
- 📊 Live charts for latency & health
- 🧾 PDF report export
- 📩 Alerts on failure (email/Slack)
- 📂 Bulk import devices via CSV/JSON

---

## 📄 License
MIT License — Free to use, improve, and share with credit.

---

## 🤝 Contributions

PRs welcome! Drop a GitHub issue or feature request anytime.

---

## 👨‍💻 Maintainer

**@Abdulkabeer-W**

**Project:** *AI-Powered Network Troubleshooter*