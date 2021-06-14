import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import time
import subprocess
#from ecapture import ecapture as ec
import wolframalpha
import json
import requests
from urllib.request import urlopen
import psutil
import pyjokes
import pyautogui
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate=engine.setProperty("rate",140)

def currentTime():
    speak("current time is ")
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(time)
def date():
    speak("current date is")
    speak(datetime.datetime.now().day)
    speak(datetime.datetime.now().month)
    speak(datetime.datetime.now().year)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("welcome back !")
    speak("I am surdas. please tell me how may i help you!")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit = 5) 
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print(e)
        speak("pardon me , please say it again")
        return "None"

    return query



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def cpu():
    usage=str(psutil.cpu_percent)
    speak("cpu is at"+ usage)

    battery=psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke)

def screenshot():
    img= pyautogui.screenshot()
    img.save('d:/jarvis/screenshot.png')




if __name__ == "__main__":
    wishMe()

    while True:

        query = takeCommand().lower()

        if 'good bye' in query or 'ok bye' in query or 'stop' in query:
            speak("your personal assistant alexa is shutting down , good bye")
            speak("have a nice day ahead")
            break

        elif 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,2)
            speak("According to wikipedia")
           # print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("what will i search in youtube")
            search_tearm=takeCommand().lower()
            webbrowser.open_new_tab("https://www.youtube.com/results?search_query="+search_tearm)
            time.sleep(5)

        elif 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com")
            speak("google chrome is open now")
            time.sleep(2)

        elif 'date' in query:
            date()
        elif 'current time' in query:
            currentTime()

        elif 'news' in query:
            news=webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak("here are some headlines from the times of india , happy reading sir")
            time.sleep(20)

        #elif "camera" in query or "take a photo" in query:
         #   ec.capture(0,"robo camera","img.jpg")

        elif 'search' in query:
            query=query.replace("search","")
            webbrowser.open(query)
            time.sleep(2)

        elif 'who are you' in query or 'what can you do' in query:
            speak("I am alexa , version 1 point 0 your personal assistant. I am programmed to help you in your task sir ")
            speak("i can do a lots of stuff for you like openinng google , youtube or sreach something on google")
            speak("i am also capable of taking your selfie and photos and many more things")

        elif 'who made you' in query or 'who created you' in query:
            speak("I was built by shyam prakash")

        elif 'ask' in query:
            speak("i can answer to computational and geographical question and what question do you want to ask now")
            question=takeCommand()
            app_id="U3J4J2-5EHURP8KT2"
            client = wolframalpha.Client('U3J4J2-5EHURP8KT2')
            res=client.query(question)
            answer=next(res.results).text
            speak(answer)
            print(answer)
        

        elif 'cpu' in query:
            cpu()

        elif 'joke' or 'jokes' in query:
            joke()

        elif 'screenshot' in query:
            screenshot()

        elif 'play music' in query:
            songs_dr='D:/songs'
            music=os.listdir(songs_dr)
            speak('what sholud i play or song number')
            ans =takeCommand().lower()
            while('number' not in ans and ans != 'random' and ans !='you choose'):
                speak('i could not understand , please say it again')
                ans=takeCommand().lower()

            if 'number' in ans:
                no=int(ans.replace('number',''))
            if 'random' or 'you choose' or 'anyone' in ans:
                no= random.randint(1,100)

            os.startfile(os.path.join(songs_dr,music[no]))

        elif 'remember that' in query:
            speak("what should i remember")
            memory=takeCommand()
            speak("you asked me to remember that"+ memory)
            remember=open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember=open('memory.txt','r')
            speak('you asked me to remember that'+remember.read())
             

        elif 'where is' or 'locate' in query:
            if 'where is' in query:
                query=query.replace('where is','')
            else:
                query=query.replace('locate','')
            locatiom=query
            speak('user asked to loacate'+locatiom)
            webbrowser.open_new_tab("https://www.google.com/maps/place"+locatiom)

