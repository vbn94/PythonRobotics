import wikipedia 
import pyttsx3
import re

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    question = input('Enter your question: ')
    try:
        result = wikipedia.summary(question, sentences = 2)
        result = re.sub(r'\([^)]*\)', '', result) 
        speak(result)
    except:
        speak('No information')