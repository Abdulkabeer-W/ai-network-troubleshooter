from flask import Flask, jsonify
import subprocess
import platform
from ai_suggestions import suggest_fix
from flask import render_template
from ai_nlp import get_ai_explanation
from flask import request
from flask import send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

app = Flask(__name__)

# List of devices to monitor
hosts = {
    "Ubuntu-1": "192.168.56.108",
    "Ubuntu-2": "192.168.56.104",
    "Fake-Device": "192.168.56.199"
}

def ping_host(host_ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        output = subprocess.check_output(["ping", param, "3", host_ip], stderr=subprocess.STDOUT)
        output_str = output.decode()
        if "unreachable" in output_str.lower() or "timed out" in output_str.lower():
            return {"status": "unreachable", "latency": None}
        elif "time=" in output_str:
            times = [line for line in output_str.splitlines() if "time=" in line]
            latencies = []
            for line in times:
                try:
                    latency = float(line.split("time=")[-1].split("ms")[0].replace("<", "").strip())
                    latencies.append(latency)
                except:
                    continue
            avg_latency = sum(latencies) / len(latencies) if latencies else None
            return {"status": "reachable", "latency": round(avg_latency, 2)}
        else:
            return {"status": "reachable", "latency": None}
    except subprocess.CalledProcessError:
        return {"status": "unreachable", "latency": None}


@app.route('/status-basic')
def status_basic():
    results = {}
    for name, ip in hosts.items():
        res = ping_host(ip)
        suggestion = suggest_fix(res["status"], res["latency"])
        results[name] = {
            "ip": ip,
            "status": res["status"],
            "latency": res["latency"],
            "suggestion": suggestion
        }
    return jsonify(results)

@app.route('/ai-insight', methods=['POST'])
def ai_insight():
    data = request.get_json()
    name = data.get("device")
    status = data.get("status")
    latency = data.get("latency")
    suggestion = data.get("suggestion")

    ai_msg = get_ai_explanation(name, status, latency, suggestion)
    return jsonify({"ai_explanation": ai_msg})

@app.route('/status', methods=['GET'])
def get_status():
    results = {}
    for name, ip in hosts.items():
        res = ping_host(ip)
        suggestion = suggest_fix(res["status"], res["latency"])
        ai_msg = get_ai_explanation(name, res["status"], res["latency"], suggestion)

        results[name] = {
            "ip": ip,
            "status": res["status"],
            "latency": res["latency"],
            "suggestion": suggestion,
            "ai_explanation": ai_msg
        }
    return jsonify(results)

@app.route("/report", methods=["GET"])
def generate_report():
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    y = height - 40

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "AI Network Troubleshooting Report")
    y -= 30

    data = get_status()  # reuse your live monitoring logic

    c.setFont("Helvetica", 10)
    for name, info in data.items():
        lines = [
            f"Device: {name}",
            f"IP: {info['ip']}",
            f"Status: {info['status']}",
            f"Latency: {info['latency'] if info['latency'] else 'N/A'} ms",
            f"Suggestion: {info['suggestion']}",
            f"AI Insight: {info['ai_explanation']}",
            "-" * 60
        ]
        for line in lines:
            c.drawString(50, y, line)
            y -= 15
            if y < 50:
                c.showPage()
                y = height - 40

    c.save()
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="network_report.pdf", mimetype="application/pdf")

@app.route('/')
def dashboard():
    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run(debug=True)
