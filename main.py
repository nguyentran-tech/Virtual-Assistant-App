import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb

mate = pyttsx3.init()
voice = mate.getProperty('voices')
mate.setProperty('voice', voice[1].id) # id[0] is male voice, id[1] is female voice

def speak(audio):
    print('M.A.T.E.: ' + audio)
    mate.say(audio)
    mate.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M%p")
    speak("It is " + time)

def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Mate")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Mate")
    elif hour >= 18 and hour < 24:
        speak("Good Night Mate")
    speak("How Can I Help You, Mate?")

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language='en-US')
        print("Newt: " + query)
    except sr.UnknownValueError:
        print("Sorry Mate! I didn't get that so please typing the command")
        query = str(input("Your Command: "))
    return query

if __name__ == "__main__":
    welcome()

    while True:
        #All the command will be stored in lower case for easy recognition
        query = command().lower()
        if "google" in query:
            speak("What Should I Search For?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here Is Your {search} On Google")
        
        elif "youtube" in query:
            speak("What Should I Search For?")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here Is Your {search} On YouTube")
        
        elif "time" in query:
            time()
        
        elif "quit" in query:
            speak("M.A.T.E is quitting mate. See You")
            quit()