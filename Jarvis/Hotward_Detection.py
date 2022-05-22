import os
import speech_recognition as sr


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

while True:

    wake_up = takecommand()

    if 'wake up' in wake_up:
        os.startfile("C:\\Users\\Admin\\Downloads\\advanced jarvis\\the jarvis\\AI-Desktop-Assistant-main\\main.py")

    else:
        print("nothing")    
