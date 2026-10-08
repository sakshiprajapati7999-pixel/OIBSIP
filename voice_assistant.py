import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\nListening... Speak now!")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except sr.WaitTimeoutError:
        speak("I did not hear anything. Please try again.")
    except sr.UnknownValueError:
        speak("Sorry, I could not understand your voice.")
    except sr.RequestError:
        speak("Speech recognition service is unavailable. Check your internet.")
    except OSError:
        speak("Microphone is not available. Please check your microphone.")

    return ""

def run_assistant():
    speak("Hello Sakshi! I am your Python voice assistant.")
    speak("You can ask me the time, date, or to open Google.")

    while True:
        command = listen()

        if not command:
            continue

        if "hello" in command or "hi" in command:
            speak("Hello! How can I help you?")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The current time is " + current_time)

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + current_date)

        elif "open google" in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google.")

        elif "search" in command:
            speak("What would you like to search for?")
            query = listen()

            if query:
                url = "https://www.google.com/search?q=" + query.replace(" ", "+")
                webbrowser.open(url)
                speak("Here are the search results.")

        elif "stop" in command or "exit" in command or "bye" in command:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("Sorry, I do not know that command yet.")

if __name__ == "__main__":
    run_assistant()
