from tkinter import *
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import subprocess

root = Tk()
root.geometry("500x500")
root.configure(background = "Light Blue")

label = Label(root,text = "welcome to your personal desktop assistant",bg = "Light Blue",font = ("Bahnschrift Light",15,"bold"))
label.place(relx = 0.5,rely = 0.1,anchor = CENTER)

text_to_speech = pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    

def r_audio():
    speak("how can i help you?")
    speech_recognisor = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        try:
            voice_data = speech_recognisor.recognize_google(audio,language = 'en-in')
        except sr.UnknownValueError:
            print('please repeat i did not understand what you just said ')
            speak("please repeat i did not understand what you just said")
            r_audio()
    print(voice_data)
    respond(voice_data)
    
def respond(voice_data):
    voice_data = voice_data.lower()
    print(voice_data)
    if "name" in voice_data:
        speak("My name regnold")
        print('my name is regnold')
        
    if "time" in voice_data:
        speak("current time is ")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
        
    if "search" in voice_data:
        speak("opening google")
        print("opening google")
        webbrowser.get().open("https://www.google.co.in/")
        
    if "videos" in voice_data:
        speak("opening youtube to watch videos")
        print("watch videos")
        webbrowser.get().open("https://www.youtube.com/")
        
    if "text editor" in voice_date:
        speak("opening the text editor")
        print("what i just said ")
        subprocess.Popen(["notepad.exe"])
        
button = Button(root,text = "start",bg = "red3",fg = "white",padx = 10,pady = 1,font =("Arial",11,"bold",command = r_audio))
button.place(relx = 0.5,rely = 0.5, anchor = CENTER)
        
r_audio()


root.mainloop()