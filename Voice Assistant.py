import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize voice commands
def recognize_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Can you repeat?")
        except sr.RequestError:
            print("Could not request results. Please check your internet connection.")

# Function to handle voice commands
def handle_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    elif "search" in command:
        search_query = command.replace("search", "").strip()
        search_url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(search_url)
        speak(f"Searching Google for {search_query}")
    elif "quit" in command or "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I don't understand that command.")

# Main function to run the voice assistant
def main():
    speak("Hello! I'm your voice assistant. How can I help you?")
    while True:
        command = recognize_command()
        if command:
            handle_command(command)

if __name__ == "__main__":
    main()
