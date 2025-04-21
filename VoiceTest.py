import openai
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
'''for voice in voices:
   engine.setProperty('voice', voice.id)

   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()'''
for voice in voices:
    engine.setProperty('voice', voice.id)
    print(f"Now using: {voice.name} - {voice.id}")
    engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()
