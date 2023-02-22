import pyaudio
import datetime
import os
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia

# niche maine browser set kiya hai, iske liye bus browser ka path dal do
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
webbrowser.register("brave", None, webbrowser.BackgroundBrowser(brave_path))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Morning Sir")
    elif 12 <= hour <= 18:
        speak("Afternoon Sir")
    else:
        speak("Evening Sir")
    speak("I am PROSIG Please tell me how may i help you :")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        ques = r.recognize_google(audio, language='en-in')
        print(f"You said:{ques}\n")

    except Exception as e:
        # print(e)

        print("Say that again please")
        return "None"

    return ques


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching wikipedia....")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.get("brave").open("youtube.com")
            speak("Opening YouTube ")
        elif "open google" in query:
            webbrowser.get("brave").open("google.com")
        elif "play music" in query:
            webbrowser.get("brave").open("music.youtube.com")
            speak("Enjoy your music sir")
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "open vs code" in query:
            code = r"C:\Users\HP\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(code)
        elif "open classroom" in query:
            webbrowser.get("brave").open("classroom.google.com/u/1/h")
            speak("Here you go sir")
        elif "open meet" in query:
            webbrowser.get("brave").open("meet.google.com")
            speak("Enjoy your meet  sir!!")
        elif "open gmail" in query:
            webbrowser.get("brave").open("mail.google.com")
        elif "open whatsapp" in query:
            webbrowser.get("brave").open("web.whatsapp.com")
        elif "quit" in query:
            break
