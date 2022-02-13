from gtts import gTTS
from io import BytesIO
import pyttsx3

# audio = BytesIO()
# tts = gTTS('hello', lang='en')
# tts.write_to_fp(audio)

engine = pyttsx3.init('sapi5')
voices = engine.setProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say("hello")
engine.runAndWait()
