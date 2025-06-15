import google.generativeai as genai
import os
import time

# Configure Gemini (Make sure this is called once at the top)
genai.configure(api_key=os.getenv("AIzaSyC6N6b-UBjYoqEUyKYcV0F3t1h4YMcGo7E"))

def get_ai_explanation(device_name, status, latency, suggestion):
    prompt = (
        f"You are a helpful network assistant. "
        f"Give a short, clear, non-technical explanation of this status for a beginner user.\n\n"
        f"Device: {device_name}\n"
        f"Status: {status}\n"
        f"Latency: {latency if latency else 'N/A'} ms\n"
        f"System Suggestion: {suggestion}\n\n"
        f"Limit the explanation to 2–3 lines. End with one actionable tip."
    )

    start = time.time()
    
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        end = time.time()
        print(f"[AI] Took {end - start:.2f} seconds for {device_name}")
        
        return response.text.strip()
    
    except Exception as e:
        print(f"[AI Error] {e}")
        return "AI response unavailable due to error."


