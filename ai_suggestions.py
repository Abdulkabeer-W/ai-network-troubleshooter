def suggest_fix(status, latency=None):
    """
    Analyze status and latency to provide smart suggestions.
    """
    if status == "unreachable":
        return "❌ Host is unreachable. Check if the device is powered on and properly connected to the network."
    
    if latency is None:
        return "⚠️ Host is reachable, but no latency data was found. Check routing paths or DNS configuration."

    if latency > 250:
        return f"⚠️ High latency detected: {latency} ms. Recommend checking for heavy traffic, faulty cables, or congested routes."
    elif 100 < latency <= 250:
        return f"ℹ️ Moderate latency: {latency} ms. May indicate minor congestion or long-distance routing."
    else:
        return f"✅ Normal performance. Latency: {latency} ms."


if __name__ == "__main__":
    print(suggest_fix("reachable", 20))
    print(suggest_fix("reachable", 300))
    print(suggest_fix("unreachable"))
