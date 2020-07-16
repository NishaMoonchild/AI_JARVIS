import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import playsound
import random
from gtts import gTTS


value=random.randint(2,55)


engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12:
       speak("good morning")
    elif hour>=12 and hour<=18:
        speak("good Afternoon")

    else:
        speak(" good night")




def takeCommand():
    #it takes my microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query =r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
       # print(e) # show error  on consol


        print("say that again please....")
        speak("say that again please....")
        return"none"
    return query


if __name__=="__main__":
   wishMe()
   
   
   while True:
        query = takeCommand().lower()


       #logic for exicuting task based on query

        if 'wikipedia' in query:
            speak('searching wiki...')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        

        elif 'search ' in query:
            search_term = query.split("for")[-1]
            url = f"https://google.com/search?q={search_term}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {search_term} on google')

        elif " name" in query:
            speak ('hii I am jarvis your personal asisstant')
        
        elif "my name" in query:
            speak('nice name')

        elif 'hello' in query:
            speak("hii")    

        
        elif 'youtube' in query:
            search_term = query.split("for")[-1]
            url = f"https://www.youtube.com/results?search_query={search_term}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {search_term} on youtube')



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
       
        elif ' created ' in query:
            speak('sorry I cannot tell this it is secret')
    
        elif ' music' in query:
            music_dir='D:\\Zzzzzzzz\\Music\\Band_slow'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[value]))

    
        elif "good night" in query:
            speak("ok sleep")
    

        elif "goodby" in query:
            speak("goodby  thankyou for using me I am going to sleep ")
            exit()