import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pywhatkit
import requests
import os
import wikipedia
import pyautogui
import pyjokes
from PyDictionary import PyDictionary as diction
from playsound import playsound
from pywikihow import search_wikihow
from keyboard import press
from bs4 import BeautifulSoup
from time import sleep
from keyboard import press_and_release
from keyboard import write
from googletrans import Translator

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',170)

def speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    print("   ")
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listining . . .")
        command.pause_threshold= 1
        audio = command.listen(source)

        try:
            print("recognizing . . .")
            query = command.recognize_google(audio,language='en-in')
            print(f"you said:\n{query}")

        except Exception as error:
            return "none"

        return query.lower()

def wish():
      hour = int(datetime.datetime.now().hour)

      if hour>=0 and hour<=12:
          speak("good morning sir")

      elif hour>=12 and hour<=19:
          speak("good afternoon sir")  

      else:
          speak("good night sir")

      print('''all commands of jarvis
               1.youtube search
               2.google search
               3.website
               4.launch
               5.play music
               6.wikipedia
               7.open
               8.close
               9.i need a joke
               10.repeat me
               11.my location
               12.dictionary
               13.screenshot
               14.translator
               15.remember that
               16.temperature
               17.you can sleep
               18.speedtest
               19.how to
               20.read google
               21.alarm
               22.chrome automation
               23.youtube automation''')
       

      speak("hello sir I am jarvis plese tell me how may I help you")

def openapps():
    speak("ok sir you can open any program you want")
    query = takecommand()

    if 'chrome' in query:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        speak("opening google chrome")

    elif 'code' in query:
        os.startfile("C:\\Users\\Admin\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe")
        speak("opening visual studio code")          

    elif 'notepad' in query:
        os.startfile("C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_10.2103.6.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe")
        speak("opening notepad")

    elif 'calculator' in query:
        webbrowser.open("https://www.google.com/search?q=calculator&rlz=1C1YTUH_enIN967IN967&oq=calcu&aqs=chrome.1.69i57j0i67i131i433j0i67j0i67i433j0i433i512l4j0i67j0i512.6947j0j7&sourceid=chrome&ie=UTF-8")
        speak("opening calculator")

    elif 'youtube' in query:
        webbrowser.open("https://youtube.com")
        speak("task completed")

    elif 'facebook' in query:
        webbrowser.open("https://facebook.com")
        speak("facebook opened")            

    elif 'meet' in query:
        webbrowser.open("https://meet.google.com/")
        speak("google meet opened")

    elif 'google' in query:
        webbrowser.open("https://google.com/")
        speak("google opened")

    elif 'instagram' in query:
        webbrowser.open("https://www.instagram.com/?hl=en")
        speak("instagram opened")            

def closeapp():
    speak("which program would you like to close")
    query = takecommand()

    if 'chrome' in query:
        os.system("TASKKILL /F /im chrome.exe")

    elif 'code' in query:
        os.system("TASKKILL /F /im code.exe")

    elif 'file manager' in query:
        os.system("TASKKILL /F /im File Explorer.exe")        

    elif 'notepad' in query:
        os.system("TASKKILL /F /im Notepad.exe")

    speak("the application is closed")

def takehindi():

    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listining . . .")
        command.pause_threshold= 1
        audio = command.listen(source)

        try:
            print("recognizing . . .")
            query = command.recognize_google(audio,language='hi')
            print(f"you said:\n{query}")

        except Exception as error:
            return "none"

        return query.lower()    

def speed():
    import speedtest
    query = takecommand()
    speak("which speed do you want to see downloading or uploading or both")
    speed = speedtest.Speedtest()
    download = speed.download()
    correctdown = int(download/800000)
    uploading = speed.upload()
    correctup = int(uploading/800000)

    if 'uploading' in query:
        speak(f"your network's uploading speed is {correctup} mbp/s")

    elif 'downloading' in query:
        speak(f"your network's downloading speed is {correctdown} mbp/s") 

    else:
        speak(f"your network's downloading speed is {correctdown} mbp/s")
        speak(f"your network's uploading speed is {correctup} mbp/s")       

def temp():
    search = "temperature in maharashtra"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div", class_ = "BNeawe").txt
    speak(f"temprature in kalwan is{temperature} celcius")

def trans():
    speak("what line should i translate")
    line = takehindi()
    translate = Translator()
    result = translate.translate(line)
    text = result.text
    speak("the translation for this line is:" + text)

def screenshot():
    speak("what would i name the file")
    path = takecommand()
    path1name = path + ".png"
    path1 = "C:\\Users\\Admin\\Downloads\\jarvis screenshots\\" + path1name
    kk = pyautogui.screenshot()
    kk.save(path1)
    os.startfile("C:\\Users\\Admin\\Downloads\\jarvis screenshots")
    speak("here is your screenshot")

def dik():
    speak("what is the problem")
    prob1 = takecommand()

    if 'meaning' in prob1:
        prob1 = prob1.replace("what is the","")
        prob1 = prob1.replace("jarvis","")
        prob1 = prob1.replace("of","")
        prob1 = prob1.replace("meaning of","")
        result = diction.meaning(prob1)
        speak(f"the meaning for {prob1} is : {result}")

    elif 'synonym' in prob1:
        prob1 = prob1.replace("what is the","")
        prob1 = prob1.replace("jarvis","")
        prob1 = prob1.replace("of","")
        prob1 = prob1.replace("synonym of","")
        result = diction.synonym(prob1)
        speak(f"the synonym for {prob1} is : {result}")

    elif 'antonym' in prob1:
        prob1 = prob1.replace("what is the","")
        prob1 = prob1.replace("jarvis","")
        prob1 = prob1.replace("of","")
        prob1 = prob1.replace("antonym of","")
        result = diction.antonym(prob1)
        speak(f"the antonyam for {prob1} is : {result}")

    speak("exited dictionary")        

def taskexecution():

    while True:


        query = takecommand()

        if 'hello' in query:
            speak("hello sir how are you...need any help")

        elif 'i am fine' in query:
             speak("good to know")

        elif 'youtube search'  in query:
            speak("ok sir this is what i found on youtube")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("enjoy!")

        elif 'google search' in query:
            speak("this is what i found on google")
            query = query.replace("jarvis","")    
            query = query.replace("google search","")
            pywhatkit.search(query)
            speak("you can read")

        elif 'website' in query:
            speak("opening website")
            query = query.replace("jarvis","")    
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)

        elif 'launch' in query:
            speak("what is the name of website") 
            name = takecommand()
            web = "https://www." + name + '.com'
            webbrowser.open(web)
            speak("opening sucsessful")

        elif 'play music' in query:
            music()

        elif 'wikipedia' in query:
            speak("searching wikipedia . . . .")
            query = query.replace("jarvis","") 
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            speak(f"according to wikipedia: {wiki}")

        elif 'open' in query:
            openapps()

        elif 'close' in query:
            closeapp()

        elif 'i need a joke' in query:
            get = pyjokes.get_joke()
            speak(get) 

        elif 'repeat me' in query:
            speak("yes sir")
            jj = takecommand()
            speak(f"{jj}")

        elif 'my location' in query:
            webbrowser.open("https://www.google.com/maps/place/Kalwan,+Maharashtra+423501/@20.489258,74.0271993,17.88z/data=!4m5!3m4!1s0x3bde7a495ec31655:0x5820e4e0bfeb7653!8m2!3d20.4890875!4d74.0270745")
            speak("your location is india..maharashtra..nashik..kalwan..ganesh nagar..thoke hospital")  
            
        elif 'dictionary' in query:
            dik()

        elif 'screenshot' in query:
            screenshot()

        elif 'translator' in query:
            trans()

        elif 'remember that' in query:
            remeberMsg = query.replace("remember that","")
            remeberMsg = query.replace("jarvis","")
            speak("you told me to remind you that" + remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()

        elif 'what do you remember' in query:
            remeber = open('data.txt','r')
            speak("you told me that"+ remeber.read())

        elif 'temperature' in query:
            temp()

        elif 'new tab' in query:
            press_and_release('ctrl + t')

        elif 'close tab' in query:
            press_and_release('ctrl + w')    

        elif 'downloads' in query:
            press_and_release('ctrl + j')

        elif 'reload' in query:
            press_and_release('ctrl + r')

        elif 'back' in query:
            press_and_release('alt + left')

        elif 'save' in query:
            press_and_release('ctrl + s')                    

        elif 'find' in query:
            press_and_release('ctrl + f')

        elif 'copy' in query:
            press_and_release('ctrl + c')

        elif 'task' in query:
            press_and_release('Shift + esc')

        elif 'bookmark' in query:
            press_and_release('ctrl + d')

        elif 'switch tab' in query:
            speak("to which tab")
            paad = int(query)
            if 'one' in query:
                press_and_release('ctrl + 1')

            elif 'to' in query:
                press_and_release('ctrl + 2')

            elif 'three' in query:
                press_and_release('ctrl + 3')

            elif 'four' in query:
                press_and_release('ctrl + 4')

            elif 'five' in query:
                press_and_release('ctrl + 5')

        elif 'start' in query:
            name = query.replace("start","")
            namea = str(name)

            if 'youtube' in namea:
                webbrowser.open('https://youtube.com/')

            else:
                string = 'https://www.' + namea +'.com'
                string2 = string.replace(" ","")
                webbrowser.open(string2)

        elif 'full screen' in query:
            pyautogui.press('f')
 
        elif 'mode' or 'theatre mode' in query:
            pyautogui.press('t')

        elif 'slow' or 'slow motion' in query:
            press_and_release('shift + ,')

        elif 'fast' or 'faster' in query:
            press_and_release('shift + .')

        elif 'forward' or 'fast forward' or 'skip' in query:
            pyautogui.press('l')

        elif 'backward' or 'backside' or 'kill' in query:
            pyautogui.press('j')

        elif 'volume up' in query:
            pyautogui.press('up')

        elif 'volume down' in query:
            pyautogui.press('down')

        elif 'cap' in query:
            pyautogui.press('c')

        elif 'mute' or 'unmute' in query:
            pyautogui.press('m')

        elif 'subscription' in query:
            webbrowser.open('https://www.youtube.com/feed/subscriptions')
                

        elif 'search' in query:
            pyautogui.click(x=568, y=134)
            speak("what should i search")
            search = takecommand()
            write(search)
            sleep(0.8)
            press('enter')            

        elif 'next video' in query:
            press_and_release('shift + n')

        elif 'zoom in' in query:
            press_and_release('ctrl + +')    

        elif 'pre video' in query:
            press_and_release('ctrl + -')                        

        elif 'paste' in query:
            press_and_release('ctrl + v')       

        elif 'new window' in query:
            press_and_release('ctrl + n') 

        elif 'history' in query:
            press_and_release('ctrl + h')       

        elif 'you can sleep' in query:
            speak("ok sir , you can call me any time")
            break    

        elif 'speed test' in query:
            speed()

        elif 'how to' in query:
            speak("collecting data from internet . . . .")
            op = query.replace("jarvis","")
            resul = 1
            how =  search_wikihow(op,resul)
            assert len(how) == 1
            how[0].print() 
            speak(how[0].summary)         

        elif 'read google' in query:
            import wikipedia as googlescrap
            query = query.replace("jarvis","")
            query = query.replace("read google","")
            query = query.replace("google","")
            speak("this is what i found for your search")
            pywhatkit.search(query)

            try:
                result = googlescrap.summary(query,3)
                speak (result)

            except:
                speak("something went wrong")    
                

        elif 'alarm' in query:
            speak("enter the time")
            time = input(": enter the time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("time up sir")
                    playsound("alarm.wav")

                elif now>time:
                    break       

def music():
    speak("3 options 1.believer 2.stay 3.toxic")
    musicname = takecommand()

    if 'believer' in musicname:
        os.startfile('C:\\Users\\Admin\\Downloads\\believer.mp3')

    elif 'stay' in musicname:
        os.startfile("C:\\Users\\Admin\\Downloads\\Stay_320(PaglaSongs).mp3")

    elif 'toxic' in musicname:
        os.startfile("C:\\Users\\Admin\\Downloads\\BoyWithUke_320(PaglaSongs).mp3")

    else:
        pywhatkit.playonyt(musicname)            

    speak("enjoy!")    

wish()               
taskexecution()