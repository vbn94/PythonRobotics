import speech_recognition as sr
import pyttsx3


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
    speak("Hello! How can I assist you today?")


    while True:
        user_input = recognize_speech()


        if "hello" in user_input:
            speak("Hi there! How can I help?")
        elif "goodbye" in user_input:
            speak("Goodbye! Have a great day.")
            break
        else:
            speak("I'm not sure how to respond to that. Please try again.")


