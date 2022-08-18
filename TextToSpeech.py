import speech_recognition as sr

r = sr.Recognizer()
while True:

    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=.2)
            print('Say something')
            audio = r.listen(source)
            speech = r.recognize_google(audio)
            print(speech)

    except: 
        pass
