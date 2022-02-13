import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
voicespeed = 140
engine.setProperty('rate', voicespeed)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language = 'en-in')
            # print(voice_data)
        except sr.UnknownValueError:
            print('Sorry, I did not get that')
        except sr.RequestError:
            print('Sorry, my speech service is down')
        return voice_data

def response_audio(voice_data):
    speak(voice_data)

def welcome_audio():
    speak("How are you sir...")
    speak("What is your name? ")

welcome_audio()
voice_data = record_audio()
print(voice_data)
response_audio(voice_data)
#print('How can I help you?')
# voice_data = record_audio()
# print(voice_data)
