import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("mulai bicara")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            print(command)
except:
    pass
