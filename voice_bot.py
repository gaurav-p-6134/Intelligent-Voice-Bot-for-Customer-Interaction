import os
import json
import datetime
import time
import speech_recognition as sr
import google.generativeai as genai
from gtts import gTTS
from playsound import playsound

# --- CONFIGURATION ---
# PASTE YOUR GOOGLE GEMINI KEY HERE
GOOGLE_API_KEY = "AIzaSyA9ticU8cHZ_Q72Slag_WrWDIiK-ZXUa2g"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('models/gemini-2.0-flash')

# --- FEATURE 5: MOCK DATABASE ---
MOCK_DATABASE = {
    "user_123": {"name": "Alice", "balance": "$4,500", "status": "Active"}
}

def get_account_details(user_id="user_123"):
    return MOCK_DATABASE.get(user_id, "User not found.")

# --- FEATURE 1: SPEECH-TO-TEXT (FREE GOOGLE VERSION) ---
def listen_and_transcribe():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... (Speak now)")
        # Adjust for ambient noise automatically
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Processing audio...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

# --- FEATURE 2 & 3: INTELLIGENT RESPONSE (GEMINI) ---
def generate_response(user_text):
    if not user_text:
        return "I didn't catch that."

    # Simple intent check
    if "balance" in user_text.lower() or "account" in user_text.lower():
        data = get_account_details()
        prompt = f"You are a support bot. The user asking about account. Data: {data}. Summarize it."
    else:
        prompt = f"You are a helpful assistant. Reply concisely to this: {user_text}"

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"\n--- GEMINI ERROR: {e} ---\n") # This prints the real reason
    return "I am having trouble connecting to the AI."

# --- FEATURE 4: TEXT-TO-SPEECH ---
def speak_text(text):
    print(f"Bot says: {text}")
    tts = gTTS(text=text, lang='en')
    filename = "response.mp3"
    try:
        tts.save(filename)
        # Using os.system to avoid playsound errors on some Windows machines
        os.system(f"start {filename}") 
    except Exception as e:
        print("TTS Error:", e)

def log_interaction(user_text, bot_response, latency):
    """Logs queries and response times to a file for the Analytics Dashboard."""
    log_entry = {
        "timestamp": str(datetime.datetime.now()),
        "query": user_text,
        "response": bot_response,
        "latency_seconds": round(latency, 2),
        "status": "Success" if bot_response else "Failed"
    }
    
    # Append to a JSON file (simulating a database log)
    with open("project_logs.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    print(" [Analytics] Interaction logged.")

# --- MAIN LOOP ---
def main():
    print("--- VOICE BOT STARTED ---")
    while True:
        input("\nPress Enter to speak...")
        
        # Start Timer
        start_time = time.time()
        
        user_text = listen_and_transcribe()
        
        if user_text:
            bot_reply = generate_response(user_text)
            speak_text(bot_reply)
            
            # End Timer & Log
            end_time = time.time()
            latency = end_time - start_time
            log_interaction(user_text, bot_reply, latency)

if __name__ == "__main__":
    main()