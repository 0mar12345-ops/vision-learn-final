# AI Vision Assistant for the Visually Impaired

An AI-powered assistive system designed to help visually impaired individuals understand and interact with their surroundings using real-time image analysis and voice interaction.

---

## Overview

This project combines computer vision, speech recognition, and conversational AI to create a system that can:
- Describe surroundings using a camera
- Answer questions through voice interaction
- Provide real-time spoken feedback

The system is built on a Raspberry Pi and designed to be simple, accessible, and intuitive.

---

## Demo

https://www.youtube.com/watch?v=m50xAmoZy3s

---

## Features

### Voice Assistant
- Speech-to-text input using microphone
- AI-powered responses using OpenAI models
- Natural-sounding text-to-speech output
- Short, conversational replies

### Vision System
- Image capture using Raspberry Pi camera
- AI-based scene understanding
- Structured descriptions for visually impaired users
- Summary + detailed explanation format

### Physical Interaction
- Push-button triggers image capture
- Simple, tactile interface (no complex UI required)

---

## Hardware Used

- Raspberry Pi
- Camera Module
- Microphone
- Speaker
- Push Button

---

## Technologies

- Python
- OpenAI API (vision + language + TTS)
- SpeechRecognition
- gTTS / mpg123
- RPi.GPIO
- python-dotenv

---

## Setup

### 1. Install dependencies
```bash
pip install python-dotenv speechrecognition gtts openai
