# Intelligent-Voice-Bot-for-Customer-Interaction
## 1. Project Overview
This project is a functional AI Voice Bot designed to handle customer queries and perform backend data retrieval. The bot listens to voice input, processes the intent using a Large Language Model (LLM), fetches dynamic user data (such as account balance), and responds via synthesized speech.


## 2. Key Features Implemented
This solution addresses all key requirements outlined in the assignment:


Speech-to-Text (STT): real-time audio transcription using Google Speech Recognition APIs.


Natural Language Understanding (NLU): Utilizes Google Gemini 2.0 Flash (a high-performance LLM) to understand user intent and generate conversational responses.


Backend Database Integration: Implemented a mock banking database. The bot detects specific intents (e.g., "What is my balance?") and queries this database to retrieve the user's name and balance ($4,500).


Text-to-Speech (TTS): Converts the AI's text response into audio using Google Text-to-Speech (gTTS) for immediate playback.



Analytics Dashboard: A logging system tracks every interaction (timestamp, user query, response, and latency) and saves it to project_logs.json for performance monitoring.

## 3. Technology Stack
Language: Python 3.x

AI Model: Google Gemini 2.0 Flash (Generative AI)

Speech Services: SpeechRecognition (STT), gTTS (TTS)

Data Handling: JSON (Logging), Dictionary (Mock DB)

## 4. Setup & Installation
To run this project locally, follow these steps:

### Step 1: 
Install Dependencies Open a terminal and run the following command to install the required Python libraries:

Bash

pip install google-generativeai SpeechRecognition gTTS playsound==1.2.2
### Step 2: 
API Configuration This project requires a valid Google Gemini API Key.

Open voice_bot.py.

Locate the variable GOOGLE_API_KEY.

Ensure your active key is pasted inside the quotes.

### Step 3: Run the Application Execute the script in your terminal:

Bash

python voice_bot.py
## 5. Usage Guide (Demo Scenarios)
Once the bot is running, you can test the following scenarios:

Scenario A: General Conversation

User: "Hello, who are you?"

Bot: "I am a helpful customer support assistant..."

Scenario B: Account Inquiry (Backend Integration)

User: "What is my account balance?"

Bot: "The account belongs to Alice and has a balance of $4,500."

## 6. Files Included
voice_bot.py: The main application source code.

project_logs.json: The analytics log file created automatically during runtime.

README.md: This project documentation.
