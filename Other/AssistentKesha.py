import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

opts = {
    "alias": ('кеша', 'кеш'),
    "tbr":('скажи','расскажи','покажи','сколько','произнеси'),
    "cmds":{
        "ctime":('текущее время','сейчас времени','который час'),
        "radio":('включи музыку','включи радио'),
        "stupid1":('расскажи анекдот','расскажи шутку')
    }
}

def speak(what): 
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    #speak_engine.stop()


def callback(recognizer, audio):
    try:
        voise = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print("[log] распознано: " + voice)

    except sr.UnknownValueError:
        print("[log] Голос не распознан!: ")

    except sr.RequestError as e:
        print("[log] неисвестная ошибка, проверте интернет!")
def recognizer_cmd(cmd):
    pass

def execute_cmd(cmd):
    pass

r = sr.Recognizer()

#for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print(index, name)

m = sr.Microphone(device_index = 1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

voices = speak_engine.getProperty('voices')
print(voices)
speak_engine.setProperty('voice', voices[1].id)

speak("добрый день")
speak("кеша слушает")
    
stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1)







print("End!!!")

