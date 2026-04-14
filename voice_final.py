import os
import sys
import speech_recognition as sr
from openai import OpenAI

# ?? Your API key (rotate after demo)
client = OpenAI(api_key="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")

r = sr.Recognizer()
r.pause_threshold = 0.8
r.dynamic_energy_threshold = True

# ?? HUMAN VOICE OUTPUT
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

    # ?? Hide audio spam
    os.system("mpg123 -q speech.mp3 2>/dev/null")


print("Vision AI Ready...")

# ?? CONVERSATION MEMORY + HUMAN STYLE
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
            # ?? HIDE ALSA WARNINGS
            sys.stderr = open(os.devnull, 'w')

            print("\nListening...")
            r.adjust_for_ambient_noise(source, duration=1)

            # ? FASTER + MORE RESPONSIVE
            audio = r.listen(source, timeout=5, phrase_time_limit=4)

        user_text = r.recognize_google(audio)
        print("You:", user_text)

        # ?? EXIT COMMAND
        if user_text.lower() in ["stop", "exit", "quit", "goodbye"]:
            speak("Goodbye.")
            break

        # ?? SAVE USER MESSAGE
        conversation.append({"role": "user", "content": user_text})

        # ?? AI RESPONSE
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation,
            max_tokens=40,
        )

        reply = response.choices[0].message.content

        if not reply:
            reply = "Sorry, I couldn't think of a response."

        print("AI:", reply)

        # ?? SAVE AI RESPONSE
        conversation.append({"role": "assistant", "content": reply})

        # ?? SPEAK
        speak(reply)

    except sr.UnknownValueError:
        print("Didn't catch that")
        speak("Sorry, I didn't catch that.")

    except sr.WaitTimeoutError:
        print("No speech detected")

    except Exception as e:
        print("Error:", e)
        speak("Something went wrong.")
