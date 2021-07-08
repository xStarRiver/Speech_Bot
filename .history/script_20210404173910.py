import speech_recognition as sr 
from win10toast import ToastNotifier
import os
import threading
from re import search


def listen():
    with sr.Microphone() as source:
        r = sr.Recognizer()
        r.energy_threshold = 3000
        r.adjust_for_ambient_noise(source)
        print("...")
        audio = r.listen(source)
    try:
        recog_speech = r.recognize_google(audio)
        print(recog_speech)
        if 'system call' in recog_speech:
            threading.Thread(target=doing).start()
            threading.Thread(target=notice).start()
            
            

    except:
        
        print("2")
        


def doing():
    with sr.Microphone() as source:
        re = sr.Recognizer()
        re.adjust_for_ambient_noise(source)
        print("....")
        audio = re.listen(source)
    try:
        reco_speech = re.recognize_google(audio)
        if search('open Google Chrome', reco_speech):
            print(reco_speech)
            os.startfile(url:"https://www.youtube.com/")
        else:
            print(reco_speech)
            

    except:
        
        print("1")

def notice():
    ToastNotifier().show_toast("system ready",
                   "waiting for command",
                   duration=6)

while True:
    listen()