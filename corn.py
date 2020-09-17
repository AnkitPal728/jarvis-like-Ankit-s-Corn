import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voice')
engine.setProperty('voice',voices[0])

MASTER = "Ankit"
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hrs = int(datetime.datetime.now().hour)
    print(hrs)

    if hrs>=0 and hrs<12:
       speak(f"Good morning {MASTER} ...")
    elif hrs==12:
       speak("Good noon {MASTER} ...")
    elif hrs>12 and hrs<16:
       speak("Good after noon {MASTER} ...")
    else:
        speak("Good evening {MASTER} ...")
    speak("I am Corn. How can i help you Master ? ...")


def takecommond():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
       print("Recognizing...")
       query = r.recognize_google(audio, language = 'en-in')
       print(f"user said : {query}\n")
    except Exception as e:
       print("Say that again please")
       query = None

    return query

print("Initializing Corn....")
speak("Initializing Corn...")
wishme()
query = takecommond()

if 'wikipedia' in query.lower():
    speak("Searching wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences = 3)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    url = "youtube.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

elif 'open google' in query.lower():
    url = "google.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

elif 'play music' in query.lower():
    songs_dir = "F:\\New folder\\Download\\Download"
    songs = os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir, songs[0]))

elif 'the time' in query.lower():
    strtime = datetime.datetime.now().strtime("%H:%M:%S")
    speak(f"{MASTER} the time is {strtime}")

else :
    speak(f"sorry {MASTER} i cann't help you")

speak(f"Thanku {MASTER} its my pleasure to help you")

