import speech_recognition
from commands import openVk, openYoutube, playMusic, greeting, screenshot


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


commandsDict = {
    'commands' : {
        'playMusic': 'включи музыку',
        'openVk' : ['открой вк', 'включи вк', 'включи vk', 'открой vk'],
        'openYoutube': ['открой youtube', 'включи youtube'],
        'greeting': ['привет', 'здарова', 'добрый день'],
        'screenshot' : ['сделай скриншот', 'сделай фото экрана']
    }
}


def listenCommand():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-Ru'). lower()
        if query == 'спать':
            return False
        else:
            return query
    
    except speech_recognition.UnknownValueError:
        return 'Повторите ещё раз'


def main():
    while True:    
        query = listenCommand()

        for k, v in commandsDict['commands'].items():
            if query in v:
                print(globals()[k]())
        

if __name__ == '__main__':
    main()
