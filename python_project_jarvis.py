import pyttsx3
from pyChatGPT import ChatGPT
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pyttsx3
import tkinter as tk
import pymysql
import openai
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
engine.setProperty('rate',150)
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def on_microphone_press():
    response_label.config(text="Listening...")
    microphone_button.config(state="disabled")
    text = takeCommand()
    response_label.config(text=text)
    speak(text)
    microphone_button.config(state="normal")
def there_exists(terms,query):
    for term in terms:
        if term in query:
         return True
def main(query):
    i = True
    while i:
        # if 3:
        query = query.lower()
        connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             db='db1',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Insert a new record into the `users` table
                sql = "INSERT INTO history (searches) VALUES (%s)"
                cursor.execute(sql, (query))

            # Commit the transaction
            connection.commit()

        finally:
            # Close the connection
            connection.close()
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
            break
        # elif 'youtube' in query:
        #     if 'search' in query:
        #         query=query.replace('search','')
        #         query=query.replace('on','')
        #         query=query.replace('youtube','')
        #         webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        #         break
        #     else:
        #         webbrowser.open("youtube.com")
        #         break
        elif ( 'search' in query and 'youtube' in query) or( 'youtube' in query and 'dikhao' in query ):
            speak("openning your youtube...")
            query=query.replace('pr','')
            query=query.replace('dikhao','')
            query=query.replace('kro','')
            query=query.replace('ki','')
            query=query.replace('search','')
            query=query.replace('on','')
            query=query.replace('youtube','')
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
            break
        elif 'hello' in query:
            res=["Hello","Thak gaya hu vro"]
            engine.say(res[random.randint(0,len(res)-1)])
            engine.runAndWait()
            break
        elif 'open google' in query:
            webbrowser.open("google.com")
            break
        elif 'best teacher' in query:
            speak("Dr. Priyanka Mishra is the best teacher")
            break
        elif 'google' in query and 'search' in query:
            query=query.replace('search','')
            query=query.replace('on','')
            query=query.replace('google','')
            webbrowser.open(f"https://www.google.co.in/search?q={query}&source=hp&ei=-Ky6Y6z1OKCXseMP3cayqAg&iflsig=AK50M_UAAAAAY7q7CJ0JwkN6n6Tby8FuPJaJbFvTPntH&ved=0ahUKEwis0eWO87f8AhWgS2wGHV2jDIUQ4dUDCAg&uact=5&oq=gl&gs_lcp=Cgdnd3Mtd2l6EAMyCwgAEIAEELEDEIMBMgsILhCABBCxAxCDATILCAAQgAQQsQMQgwEyBQgAEIAEMggIABCABBCxAzILCAAQgAQQsQMQgwEyBQgAEIAEMggIABCABBCxAzIICAAQgAQQsQMyBQgAEIAEOg4IABCPARDqAhCMAxDlAjoOCC4QjwEQ6gIQjAMQ5QI6EQguEIAEELEDEIMBEMcBENEDOggILhCxAxCDAVDyBFjSBWCMCWgBcAB4AIABigGIAYICkgEDMC4ymAEAoAEBsAEK&sclient=gws-wiz")
            break
        elif 'play' in query and 'spotify' in query:
            query=query.replace('play','')
            query=query.replace('spotify','')
            webbrowser.open(f"https://open.spotify.com/search/{query}")
            break
        elif 'open' in query:
            query=query.replace('open','')
            query=query.replace(' ','')
            webbrowser.open(f"www.{query}.com")
            break
        elif 'instagram' in query:
            webbrowser.open("instagram.com")
            break
        elif 'facebook ' in query:
            webbrowser.open("facebook.com")
            break
        elif 'video call' in query:
            webbrowser.open('https://omegle.com')
            break
        elif 'stackoverflow ' in query:
            webbrowser.open("stackoverflow.com")
            break
        elif 'play music' in query:
            music_dr = "C:\\Users\\hp\\Music"
            songs = os.listdir(music_dr)
            print(songs)
            list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13,
            14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
            os.startfile(os.path.join(music_dr, songs[random.choice(list)]))
            break   
        elif 'time ' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            break
        elif 'code' in query:
            code_path = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            break
        # elif 'email to rohan' in query:
        #     try:
        #         speak("what should i say?")
        #         content = takeCommand()
        #         to = "rohanyadav17667295@gmail.com"
        #         sendEmail(to, content)
        #         speak("email has been sent!")
        #         break
        #     except Exception as e:
        #         print(e)
        #         speak("sorry email not sent")
        elif 'open chrome' in query:
            speak("opening chrome, please wait")
            chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(chrome_path)
            break
        elif 'ram ram' in query or 'radhe radhe ' in query:
            i = False
            speak("Gubbbar is signing off!")
            break
        else:
            chatgpt_response(query)
            break

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("radhey radhey, good morning")

    elif hour >= 12 and hour < 18:
        speak("radhey radhey, Good Afternoon!")

    else:
        speak("radhey radhey, Good Evening!")

    speak("I am gubber. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    main(query)
    return ""


def chatgpt_response(prompt):
    # Apply the API key
    openai.api_key ="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"
    # Generate text

    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Print the first completion
    a=completions.choices[0].text
    print(completions.choices[0].text)
    speak(a)


   # speak("and i think his friends are also good ")
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("600x400")

# Add a background image to the root window


# Add a background image to the root window
background_image = tk.PhotoImage(file="C:\\Users\\hp\\Pictures\\background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create a frame to hold the widgets
frame = tk.Frame(root, bg='white', bd=5)
frame.place(relx=0.5, rely=0.6, relwidth=0.2, relheight=0.2, anchor='n')

# Add a custom font to the response label
custom_font = ("Arial", 15)
response_label = tk.Label(frame, text="", font=custom_font, bg='white', fg='black')
response_label.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.8, anchor='n')

microphone_button_img = tk.PhotoImage(file="D:\\Downloads\\microphone-icon-5048.png")
microphone_button = tk.Button(frame, image=microphone_button_img, bg='white', bd=0, activebackground='white', command=takeCommand)
microphone_button.place(relx=0.5, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')

wishMe()
root.mainloop()