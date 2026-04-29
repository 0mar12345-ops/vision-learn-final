import os
import sys
import speech_recognition as sr
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

 
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

r = sr.Recognizer()
r.pause_threshold = 0.8
r.dynamic_energy_threshold = True


def speak(text: str):
    if not text:
        return

    with open("speech.mp3", "wb") as f:
        audio = client.audio.speech.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=text
        )
        f.write(audio.read())

    
    os.system("mpg123 -q speech.mp3 2>/dev/null")


print("Vision AI Ready...")


conversation = [
    {
        "role": "system",
        "content": (
            "You are a friendly voice assistant talking to a blind student. "
            "Speak naturally like a human, slightly casual, not robotic. "
            "Keep responses short (12 sentences max). "
            "Sometimes ask small follow-up questions to keep conversation flowing."
        )
    }
]

while True:
    try:
        with sr.Microphone() as source:
            
            sys.stderr = open(os.devnull, 'w')

            print("\nListening...")
            r.adjust_for_ambient_noise(source, duration=1)

            
            audio = r.listen(source, timeout=5, phrase_time_limit=4)

        user_text = r.recognize_google(audio)
        print("You:", user_text)

        
        if user_text.lower() in ["stop", "exit", "quit", "goodbye"]:
            speak("Goodbye.")
            break

        
        conversation.append({"role": "user", "content": user_text})

        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation,
            max_tokens=40,
        )

        reply = response.choices[0].message.content

        if not reply:
            reply = "Sorry, I couldn't think of a response."

        print("AI:", reply)

        
        conversation.append({"role": "assistant", "content": reply})

        
        speak(reply)

    except sr.UnknownValueError:
        print("Didn't catch that")
        speak("Sorry, I didn't catch that.")

    except sr.WaitTimeoutError:
        print("No speech detected")

    except Exception as e:
        print("Error:", e)
        speak("Something went wrong.")
