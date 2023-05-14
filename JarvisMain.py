import webbrowser
import pyttsx3
import speech_recognition
import requests
import datetime
from bs4 import BeautifulSoup
import os
import pyautogui  # Control keyboard
import random
from plyer import notification
from pygame import mixer  # python DJ
import speedtest


# Password Protection Function
for i in range(3):
    a = input("Enter password to acess Jarvis: ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if a == pw:
        print("\nWELCOME SIR!!\n\nPLEASE SPEAK [WAKE UP] COMMAND TO START\n")
        break
    elif i == 2 and a != pw:
        exit()
    elif a != pw:
        print("\nTRY AGAIN\n")


# JARVIS GUI Function
from INTRO import play_gif

play_gif

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listning.......")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 5)

    try:
        print("Understanding.......")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again, Sir!")
        return "None"
    return query


# ALARM
def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


# don't close the pop up window which comes after setting time


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        # START
        if "wake up" in query:
            # Greet Me Function
            from wishMe import wishMe

            wishMe()

            while True:
                query = takeCommand().lower()

                # SLEEP MODE
                if "go to sleep" in query:
                    speak("Ok sir, You can call me anytime!!")
                    break

                # Change Password by saying
                elif "change password" in query:
                    speak("What's the new password?")
                    new_pw = input("Enter new password: \n")
                    new_password = open("password.txt", "w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done, Sir!")
                    speak(f"Your new password is{new_pw}")

                # Schedule my day Function
                elif "schedule my day" in query:
                    tasks = []  # Empty list
                    speak("Do you want to clear old tasks (Please response YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("task.txt", "w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the number of tasks: "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task:- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the number of tasks: "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task:- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                elif "show my schedule" in query:
                    file = open("tasks.txt", "r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("JarvisNotification.mp3")
                    mixer.music.play()

                    notification.notify(
                        title="My schedule: ", message=content, timeout=15
                    )

                # FOCUS MODE Function -> BLOCKS WEBSITE
                elif "focus mode" in query:
                    a = int(
                        input(
                            "Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO] : "
                        )
                    )
                    if a == 1:
                        speak("Entering the focus mode....")
                        os.startfile(
                            "D:\\Codes try\\Projects\\Assistant\\Intermidiate\\FocusMode.py"
                        )
                        exit()
                    else:
                        pass

                # Graph for focus mode
                elif "show my focus" in query:
                    from FocusGraph import focus_graph

                    focus_graph()

                # Translator Function
                elif "translate" in query:
                    from Translator import translategl

                    query = query.replace("jarvis", "")
                    query = query.replace("translate", "")
                    translategl(query)

                # OPEN any app Function (easy method)
                elif "open" in query:
                    query = query.replace("open", "")
                    query = query.replace("jarvis", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")

                # Internet Speed Test Function
                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    speak("Calculating sir")
                    upload_net = wifi.upload() / 1048576  # Megabyte = 1024*1024 Bytes
                    upload_net = round(upload_net, 2)
                    download_net = wifi.download() / 1048576
                    download_net = round(download_net, 2)
                    print("Upload Speed is", upload_net, " mb")
                    print("Download speed is ", download_net, " mb")
                    speak(f"Download speed is {download_net} megabyte")
                    speak(f"Upload speed is {upload_net} megabyte")

                # Game Function
                elif "play a game" in query:
                    from game import game_play

                    game_play()

                # Screenshot Function
                elif "screenshot" in query:
                    import pyautogui  # pip install pyautogui

                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

                # Camera Function
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                # Conversations with Jarvis
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                elif "good" in query:
                    speak("Thank you sir")
                elif "nice" in query:
                    speak("Thank you sir")

                # Make you relax Function
                elif "tired" in query:
                    speak("Playing your favorite songs sir!!")
                    a = (1, 2, 3)
                    b = random.choice(a)
                    if b == 1:
                        speak("Palying Taylor Swift")
                        webbrowser.open("https://www.youtube.com/watch?v=gPqpSG6dAJ8")
                    elif b == 2:
                        speak("Playing One Direction")
                        webbrowser.open("https://www.youtube.com/watch?v=LGx5mtIwhGI")
                    elif b == 3:
                        speak("Playing Hindi Calming songs")
                        webbrowser.open(
                            "https://www.youtube.com/watch?v=GoKSLQQw2Bc&t=220s"
                        )

                # YOUTUBE VIDEO
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("video unmuted")
                elif "volume up" in query:
                    from keyboard import volumeup

                    speak("Turning volume up, Sir!")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown

                    speak("Turning volume down, Sir!")
                    volumedown()

                # OPEN and CLOSE APPs
                elif "open" in query:
                    from Dictapp import openappweb

                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb

                    closeappweb(query)

                # Searching from web
                elif "google" in query:
                    from searchNow import searchGoogle

                    searchGoogle(query)

                # Youtube
                elif "youtube" in query:
                    from searchNow import searchYoutube

                    searchYoutube(query)

                # Wikipedia
                elif "wikipedia" in query:
                    from searchNow import searchWikipedia

                    searchWikipedia(query)

                # News Function
                elif "news" in query:
                    from newsRead import latestnews

                    latestnews()

                # Calculator Function
                elif "calculate" in query:
                    from calculate import WolfRamAlpha
                    from calculate import Calc

                    query = query.replace("calculate", "")
                    query = query.replace("jarvis", "")
                    Calc(query)

                # Whatsapp Function
                elif "whatsapp" in query:
                    from whatsapp import sendMessage

                    sendMessage()

                # Temprature Function
                elif "temperature" in query:
                    search = "temprature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {temp}")

                # Alarm Function
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")

                # Time Function
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")

                # Final shutdown function
                elif "finally sleep" in query:
                    speak("The program is terminated.\n Going to sleep, Sir!!")
                    exit()

                # System shutdown function
                elif "shutdown the system" in query:
                    speak("Are you sure you want to shutdow your system?")
                    shutdown = input(
                        "Are you sure you want to shutdow your system?(yes\no)\n"
                    )
                    if shutdown == "yes":
                        speak("Shutting down the system, Sir!!")
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break

                # Remember function
                elif "remember that" in query:
                    rememberMessage = query.replace("remember", "")
                    rememberMessage = query.replace("jarvis", "")
                    speak("You told me" + rememberMessage)
                    remember = open("remember.txt", "a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("remember.txt", "r")
                    speak("You told me" + remember.read())
