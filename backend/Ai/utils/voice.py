import pyttsx3
import speech_recognition as sr

def say(text:str)->None:
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen()->str:
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1.0  # Increase pause time to 1 second
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return None

if __name__ == "__main__":
    what_did_I_say = listen()
    say(what_did_I_say)
