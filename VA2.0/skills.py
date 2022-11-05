import os
import pyttsx3


engine = pyttsx3.init()
engine.setProperty('rate', 140)


def speaker(text):
    engine.say(text)
    engine.runAndWait()


def passive():
    pass


def browser():
    os.system('open /Applications/Safari.app')

def stupid():
    engine.say("I can't do it right now, please add this action to me")