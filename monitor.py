import subprocess
import time

hosts = {
    "Ubuntu-1": "192.168.56.108",
    "Ubuntu-2": "192.168.56.104",  # Replace with actual IPs
    "Fake-Device": "192.168.56.199"
}

import subprocess
import platform

def ping_host(host_ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        output = subprocess.check_output(["ping", param, "3", host_ip], stderr=subprocess.STDOUT)
        output_str = output.decode()
        if "unreachable" in output_str.lower() or "request timed out" in output_str.lower():
            return {"status": "unreachable", "latency": None}
        elif "time=" in output_str:
            # Try to extract average latency manually
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


if __name__ == "__main__":
    while True:
        for name, ip in hosts.items():
            result = ping_host(ip)
            print(f"[{time.ctime()}] {name} ({ip}): {result}")
        print("—" * 40)
        time.sleep(10)
