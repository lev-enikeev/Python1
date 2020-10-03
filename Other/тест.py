import time
import pyttsx3
engine = pyttsx3.init()
a = input()
while True:
    if a == "начали":
        for i in range(61):
            print("", i)
            time.sleep(1)
        engine.say("time over")
        engine.runAndWait()
    if a == "ещё раз":

        for i in range(61):
            print("", i)
            time.sleep(1)
        engine.say("time over")
        engine.runAndWait()
