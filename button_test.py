from gtts import gTTS
from ai_describe import describe_image
import RPi.GPIO as GPIO
import time
import os

BUTTON = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
   if GPIO.input(BUTTON) == 1:
    print("Capturing image...")

    # ?? Speak FIRST (before camera)
    os.system('espeak -s 140 "Please wait, analyzing image"')

    # ?? Then capture
    os.system("rpicam-still --zsl -o image.jpg")

    # ?? AI
    text = describe_image("image.jpg")
    print(text)
    # ?? Clean formatting for speech
    text = text.replace("#", "")
    text = text.replace("*", "")
    text = text.replace("’", "'")

    # ?? Better voice
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")

    # ?? Force clean playback
    os.system("mpg123 -q output.mp3")

    while GPIO.input(BUTTON) == 1:
        pass

    time.sleep(0.5)