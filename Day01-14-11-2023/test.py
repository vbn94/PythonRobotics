import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def myfunction():
    print('UKTC')
    speak('UKTC')


if __name__ == '__main__':
    speak('Hello from python')
    myfunction()
    myfunction()
    speak('Bye bye')