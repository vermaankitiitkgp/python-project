import speech_recognition as sr
import pyttsx3
# import pywhatkit as py
import datetime
import wikipedia
import pyjokes
from googlesearch.googlesearch import GoogleSearch
import webbrowser


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        command = ''
        with sr.Microphone() as source:

            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()


    except Exception as e:
            print(e)
    return command


def run_phoenix():
    flag = True
    while(flag):


        command = take_command()
        print(command)

        if 'phoenix' in command:
            talk('hi user, how are you today. hope you are fine ')
            # command = command.replace('phoenix', '')


        elif 'hello world' in command:
            talk('Nigga what')

        elif 'play' in command:
            try:
                song = command.replace('play', '')
                talk('playing ' + song)
                url = 'www.youtube.com/results?search_query='+song
                webbrowser.open_new(url)

            except Exception as e:
                print e
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who is' in command:
            try:
                person = command.replace('who is', '')
                info = wikipedia.summary(person, 2)
                print(info)
                talk(info)
            except Exception as e:
                print e
                talk('Sorry Dude, No info')
        elif 'date' in command:
            talk(datetime.date.today())
        elif 'day today' in command:
            now = datetime.datetime.now()
            talk(now.strftime("%A"))
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'bye' in command or 'good night' in command or 'see you' in command:
            talk('Its been a long day, without you my friend. And I tell you all about it when I see you again ,Take Care')
            flag = False
        elif(command==''):
            talk('Please say the command again or speak up something.')
        else:
            talk('Here is some results from google to help you with')

            url = "https://www.google.co.in/search?q="+command
            webbrowser.open_new(url)



run_phoenix()