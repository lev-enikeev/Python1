import lev_lib as l
import pyttsx3

l.my_func
engine = pyttsx3.init()
print("привет напиши слово я переверну его")
while True:
    wf = l.my_h()
    engine.say(wf)
    engine.runAndWait()