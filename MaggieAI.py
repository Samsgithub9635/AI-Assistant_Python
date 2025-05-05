import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine =pyttsx3.init('sapi5')#used to take voices windows will give an API used to input voices
voices =engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir! ")
    elif hour>12 and hour<18:
        speak("Good Afternoon Sir! ")
    else:
        speak("Good Evening Sir! ")
        
    speak("Maggie here at your service! ")


def take_command():
    ''' to take mic audio input from the user and returns string output
    '''
    r = sr.Recognizer()#Recognizer class will help to recognize the voice
    with sr.Microphone() as source:#Microphone class will accept the input from the attached mic as the source
        print("Listening...")
        r.pause_threshold= 1 # to give a 1 sec pause after completion of a word
        audio = r.listen(source)
        r.phrase_threshold = 0.3  # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        query =r.recognize_bing(audio, Language='en-in') #to recognize command related te google and recognize indo-english accent
        print(f"User said: {query}\n") # also show in the output terminal what input is taken form user as audio  
        print("Recognizing...") 
        query =r.recognize_google_cloud(audio, Language='en-in') #to recognize command related te google and recognize indo-english accent
        print(f"User said: {query}\n") # also show in the output terminal what input is taken form user as audio  
        print("Recognizing...") 
        query =r.recognize_amazon(audio, Language='en-in') #to recognize command related te google and recognize indo-english accent
        print(f"User said: {query}\n") # also show in the output terminal what input is taken form user as audio  
        print("Recognizing...") 
        query =r.recognize_google(audio, Language='en-in') #to recognize command related te google and recognize indo-english accent
        print(f"User said: {query}\n") # also show in the output terminal what input is taken form user as audio  
        print("Recognizing...") 
        query =r.recognize_whisper(audio, Language='en-in') #to recognize command related te google and recognize indo-english accent
        print(f"User said: {query}\n") # also show in the output terminal what input is taken form user as audio  
        
    except Exception as e:
        # print(e)
        print("Please Say it Again!...")
        return"None" #if not recognized return "None"
    
    return query #if all ok return the audio query taken input


def send_email(to, content_in_email):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('samratsaha9635@gmail.com', email_pass) # Sams20052024@9635 #make a function to ask your password while running the function
    server.sendmail('samratsaha9635@gmail.com', to, content_in_email)
    server.close()

    
    
if __name__ == "__main__":
    
    greetMe()
    
    while True:
        speak("What can I do for you Sir?")
        query = take_command().lower()
        if 'ok Maggie' in query:
                speak("Yes Sir what can I do for you?")
                try:
                    if 'Hi Maggie' in query:
                        speak("Hello Sir")
                    elif 'Hello Maggie' in query:
                        speak("Hi Sir")
                        # print("Listening...")

                            # logic for executing tasks based on query
                    elif 'Who is Your Boss Maggie?' in query:
                        speak("Samrat is my Boss")

                    elif 'wikipedia' in query:
                        speak('Searching wikipedia...')
                        query = query.replace('wikipedia', "")
                        result = wikipedia.summary(query, sentences=2)
                        speak("According to wikipedia")
                        print(result)
                        speak(result)

                    elif 'open youtube' in query:
                            webbrowser.open("youtube.com")
                    elif 'open google' in query:
                            webbrowser.open("google.com")
                    elif 'open chatGPT' in query:
                            webbrowser.open("chat.openai.com")
                    elif 'open Mozila' in query:
                            webbrowser.open("lavasoft.com")
      

                    elif 'play music' in query:
                            webbrowser.open("open.spotify.com")
                            # music_dir='path' #add a folder here detect the mp3 only and play it
                            # songs = os.listdir(music_dir)
                            # print(songs)
                            #os.startfile(os.path.join(music_dir, songs[0])) #generate random songsusing random module

                    elif 'the time' in query:
                            strTime = datetime.datetime.now().strftime("%h:%m:%s")
                            speak(f"Sir, the time is {strTime}")

                        # elif 'open pycharm' or 'open python' in query:
                            pycode_path ='D:\\PYTHON B TO A\\PyCharm Community Edition 2023.3.2\\bin\\pycharm64.exe'
                            os.startfile(pycode_path)
                    elif 'open java code' or 'open java' in query:
                            javacode_path ='D:\\JAVA + DSA\\IntelliJ IDEA Community Edition 2023.3.2\\bin\\idea64.exe'
                            os.startfile(javacode_path)

                    elif 'send email to samrat' or 'send email to sams' in query:
                            try:
                                speak("What is the message, sir?")
                                content_in_email = take_command()#convert my audio command into string to write the content of the email
                                to = "samratsahaofficial9635@gmail.com"
                                send_email(to, content_in_email)
                                speak("What is your email password, sir?")
                                email_pass = str(input("Sir, Please, Enter your email password here:" )) #convert my audio command into string to write the password of the email
                                speak("The sent Successfully, Sir")
                            except Exception as e:
                                print(e)
                                speak("Sorry Sir!  Failed to sent the email")
                                speak("May I try to resend it?")
                                if 'Yes' in query:
                                    send_email(to, content_in_email)
                                else :
                                    print("Sir, an Error occured again,  Please check the detaiis")
                                    speak("Sir, an Error occured again,  Please check the detaiis")   
                except Exception as e:
                     print("Sorry sir I didn't get it ?")

        
        
            
        else:
            speak("Sorry sir I didn't get it ?")  
            
    
    