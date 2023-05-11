import speech_recognition as sr

r = sr.Recognizer()

audio = 'SampleData/send.wav'

with sr.AudioFile(audio) as source:
    audio = r.record(source)

try:
    text = r.recognize_google(audio)
    print(text)
    text_file = open("sample.txt", "w")
    n = text_file.write(text)
    text_file.close()

except Exception as e:
    print(e)