import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150) 

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command(): 
    global command  
    try:
        with sr.Microphone() as source:
            print('I am listening, Say something...')
            talk('I am listening, Say something...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
        
    except sr.RequestError:
        print('Sorry, my speech service is down')
        talk('Sorry, my speech service is down')

    except:
        pass

    return command


def run_alexa():
    command = take_command()
    print('Me:', command)


    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        print('Playing' + song)
        pywhatkit.playonyt(song)

    elif 'search' in command:
        search = command.replace('search', '')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here is what i found for ' + search)
        talk('Here is what i found for ' + search)

    elif 'map' in command:
        location = command.replace('map', '')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('Here is the map of ' + location)
        talk('Here is the map of ' + location)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%m %p')
        print(time)
        talk('Current time is ' + time)

    elif 'tell me about' in command:
        ask = command.replace('tell me about', '')
        info = wikipedia.summary(ask, 2)
        print(info)
        talk(info)

    elif 'how are you' in command:
        talk('I am fine. Thank You! How about you?')

    elif 'what are you doing' in command:
        talk('hmmm.. I am damn busy')

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'Hello' in command:
        print('hello master, how can i help you')
        talk('hello master, how can i help you')

    elif 'good morning' in command:
        print('good morning master')
        talk('good morning master')

    elif 'good afternoon' in command:
        print('good afternoon master')
        talk('good afternoon master')

    elif 'good evening' in command:
        print('good evening master')
        talk('good evening master')

    elif 'good night' in command:
        print('good night master, sweet dreams')
        talk('good night master, sweet dreams')

 
    elif 'who are you' in command:
        print('I am Alexa. Your 24 7 virtual assistant. if you are bored i can tell you a joke, i can play youtube videos for you, and blah blah and i am awesome.')
        talk('I am Alexa. Your 24 7 virtual assistant. if you are bored i can tell you a joke, i can play youtube videos for you, and blah blah and i am awesome.')

    elif 'thank you' in command:
        print('Your welcome. Anything else you want me to do ?')
        talk('Your welcome. Anything else you want me to do ?')

    elif 'goodbye' in command:
        print('GoodBye Smarty. See you later, Alligator.')
        talk('GoodBye Smarty. See you later, Alligator.')

    elif 'exit' in command:
        exit()

    else:
        print('Sorry, I did not get that')
        talk('Sorry, I did not get that')


while True:     
    run_alexa()
