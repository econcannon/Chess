import speech_recognition as sr
import text_to_speech as tts

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=.2)
    print('Say something')
    audio = r.listen(source)
    speech = r.recognize_google(audio)
    print(speech)

tts.speak(speech)
