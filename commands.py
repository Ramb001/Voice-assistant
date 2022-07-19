import os
import pyttsx3
import time, datetime
from subprocess import call


speakEngine = pyttsx3.init()
voices = speakEngine.getProperty('voices')
speakEngine.setProperty('voice', voices[10].id)


def playMusic():
    os.system('open /System/Applications/Music.app')


def openVk():
    os.system('open https://vk.com')


def openYoutube():
    os.system('open https://youtube.com')    


def speak(what):
    print(what)
    speakEngine.say(what)
    speakEngine.runAndWait()
    speakEngine.stop()


def greeting():
    speak("Hi! I'm glad to see you")
    

def screenshot():
    localTime = time.localtime()
    timeString = time.strftime("%H:%M:%S", localTime)
    call(['screencapture', f'screenshot{timeString}.png'])
    

def nowTime():
    now = datetime.datetime.now()
    answer = 'Current time is %d hours %d minutes' % (now.hour, now.minute)
    speak(answer)