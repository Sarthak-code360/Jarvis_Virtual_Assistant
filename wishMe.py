import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# To wish every time assistant got accessed according to time


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning, Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon, Sir!")

    else:
        speak("Good Evening Sir!")

    # can add diff. ways to intro himself everytime we access it
    speak("This is Jarvis. Please tell me how can i help you?")
