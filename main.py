
from chatbot import get_chatbot_response
from wether import get_weather

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize voice engine
engine = pyttsx3.init()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        speak("I am listening. Please speak.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return ""


def run_assistant():
    speak("Hello! Welcome to your Python Voice Assistant.")

    while True:
        command = listen()

        if "hello" in command or "hi" in command:
            speak("Hello! How can I help you?")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The current time is " + current_time)

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + current_date)

        elif "weather" in command:
            speak("Which city?")
            city = listen()

            if city:
                weather_report = get_weather(city)
                speak(weather_report)

        elif "search" in command:
            speak("What do you want to search?")
            topic = listen()

            if topic:
                webbrowser.open(
                    "https://www.google.com/search?q=" +
                    topic.replace(" ", "+")
                )
                speak("Here are your search results.")

        elif "stop" in command or "exit" in command:
            speak("Goodbye!")
            break

        elif command:
            response = get_chatbot_response(command)
            speak(response)


if __name__ == "__main__":
    run_assistant()
