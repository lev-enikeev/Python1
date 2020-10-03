import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3

def talk(words):
    print(words)
    engine = pyttsx3.init()
    engine.say("say" + words)
    engine.runAndWait()

talk ("привет спроси у меня что нибудь")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("говорите")
        
