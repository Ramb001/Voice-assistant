import queue
import sounddevice as sd
import vosk
import json
import words 
import skills as s
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


q = queue.Queue()

device = sd.default.device = 0, 4
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])

model = vosk.Model('model')


def callback(indata, frames, time, status):
    q.put(bytes(indata))
    
    
def recognize(text, vectorizer, clf):
    trg = words.TRIGER.intersection(text.split())
    if not trg:
        return
    text.replace(list(trg)[0], '')
    textVector = vectorizer.transform([text]).toarray()[0]
    answer = clf.predict([textVector])[0]
    
    funcName = answer.split()[0]
    s.speaker(answer.replace(funcName, ''))
    exec(f's.{funcName}()')


def main():
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.dataSet.keys()))
    
    clf = LogisticRegression()
    clf.fit(vectors, list(words.dataSet.values()))
    
    del words.dataSet
    
    with sd.RawInputStream(samplerate = samplerate, blocksize = 16000, device = device[0], dtype = 'int16', channels = 1, callback = callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                text = json.loads(rec.Result())['text']
                recognize(text, vectorizer, clf)
                # print(text)
                
                
if __name__ == "__main__":
    main()