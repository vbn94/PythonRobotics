import speech_recognition as sr
import pyttsx3
import serial
import os
import wikipedia
import re
from datetime import datetime

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    ard = serial.Serial('COM9', 9600, timeout=1)
    speak("Hello! How can I assist you today?")

    while True:
        user_input = recognize_speech()

        if "hello" in user_input:
            speak("Hi there! How can I help?")
        elif "goodbye" in user_input or "bye" in user_input:
            current_datetime = datetime.now()
            current_hour = current_datetime.hour
            if current_hour >= 18 or current_hour <= 6:
                time_info = 'night'
            else:
                time_info = 'day'
            speak(f"Goodbye! Have a great {time_info}.")
            ard.close()
            break
        elif "light on" in user_input:
            speak('Turn on the lamp')
            ard.write('1'.encode())
        elif "light off" in user_input:
            speak('Turn off the lamp')
            ard.write('0'.encode())
        elif "make directory" in user_input:
            speak('Tell me directory name: ')
            user_input = recognize_speech()
            os.mkdir(user_input)
            speak('Directory created')
        elif "wikipedia" in user_input:
            speak("Tell me what you want to search in wikipedia")
            user_input = recognize_speech()
            try:
                result = wikipedia.summary(user_input, sentences = 2)
                result = re.sub(r'\([^)]*\)', '', result)
                speak(result)
            except:
                speak('Information not found')
        else:
            speak("I'm not sure how to respond to that. Please try again.")
