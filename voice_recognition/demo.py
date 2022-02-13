import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
voicespeed = 170
engine.setProperty('rate', voicespeed)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
       # r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        print(e)
        print("---")

        return "None"
    return query




if __name__ == "__main__":

    while True:
        query = takeCommand().lower()  # take command in queary
        print(query)

        if "offline" in query:  # quit to end the program
            speak("going offline")
            quit()