# github.com/faizan-khanx
# linkedin.com/in/ethicalfaizan
# Instagram.com/ethicalfaizan

import time
import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices)
    engine.setProperty('voice', voices[0].id)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 174)
    eel.receiverText(text)

# Expose the Python function to JavaScript

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening...")
        eel.DisplayMessage("I'm listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 8)

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
        eel.DisplayMessage(query)
        
        
        speak(query)
    except Exception as e:
        print(f"Error: {str(e)}\n")
        return None

    return query.lower()



import os
import psutil
import platform
import pyperclip  # For clipboard management
import datetime
import eel
import pyttsx3

@eel.expose
def takeAllCommands(message=None):
    if message is None:
        query = takecommand()
        if not query:
            return
        print(query)
        eel.senderText(query)
    else:
        query = message
        print(f"Message received: {query}")
        eel.senderText(query)

    try:
        if query:
           
           if "who is your developer" in query.lower():
                dev_name = "Faizan Khan"
                tg_profile_url = "https://instagram.com/ethicalfaizan"
                speak(f"My developer is {dev_name}. Opening his Instagram profile now.")
                import webbrowser
                webbrowser.open(tg_profile_url)

           elif "tell me about yourself" in query.lower():
                
                speak("Hello! I am Jarvis, a fully functional AI assistant created by Faizan Khan. "
                  "I can help you with various tasks such as managing files, monitoring system performance, "
                  "playing media, and even analyzing stocks. Thanks to Mr. Faizan Khan for giving me life!")

           elif "battery status" in query.lower():

                battery = psutil.sensors_battery()
                if battery:

                   percent = battery.percent
                   plugged = battery.power_plugged
                   status = "charging" if plugged else "not charging"
                   speak(f"Your system battery is at {percent} percent and is currently {status}.")
                else:
                    speak("Sorry, I couldn't retrieve the battery status.")

           elif "system specifications" in query.lower():
                
                system_info = platform.uname()
                cpu_count = os.cpu_count()
                specs = (f"System: {system_info.system} {system_info.version}, "
                f"Processor: {system_info.processor}, "
                f"CPU Cores: {cpu_count}, "
                f"Machine Type: {system_info.machine}")
                speak(f"Here are your system specifications: {specs}")

           elif "create folder" in query.lower():
                
                folder_name = query.replace("create folder", "").strip()
                os.makedirs(folder_name, exist_ok=True)
                speak(f"Folder named {folder_name} has been created.")

           elif "delete file" in query.lower():
                file_name = query.replace("delete file", "").strip()
                if os.path.exists(file_name):
                    os.remove(file_name)
                    speak(f"File {file_name} has been deleted.")
                else:
                     speak(f"File {file_name} not found.")

           elif "increase volume" in query.lower():
                
                os.system("nircmd.exe changesysvolume 5000")  # Increases system volume by 5%
                speak("Volume increased by 5 percent.")

           elif "mute volume" in query.lower():
                
                os.system("nircmd.exe mutesysvolume 1")  # Mutes system volume
                speak("Volume has been muted.")

           elif "show clipboard" in query.lower():
                
            clipboard_content = pyperclip.paste()
            speak(f"Clipboard content is: {clipboard_content}")

           elif "copy to clipboard" in query.lower():
                text_to_copy = query.replace("copy to clipboard", "").strip()
                pyperclip.copy(text_to_copy)
                speak(f"Text copied to clipboard: {text_to_copy}")

           elif "set a reminder" in query.lower():
                
                reminder_text = query.replace("set a reminder", "").strip()
                reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
                speak(f"Reminder set for: {reminder_time}. I will remind you to {reminder_text}.")

           elif "shut down system" in query.lower():
                speak("Shutting down the system now.")
                os.system("shutdown /s /t 5")

           elif "restart system" in query.lower():
                speak("Restarting the system now.")
                os.system("shutdown /r /t 5")

           elif "open youtube" in query.lower():
                
                speak("Opening YouTube now.")
                import webbrowser
                webbrowser.open("https://www.youtube.com")

           elif "play youtube video" in query.lower():
                video_title = query.replace("play youtube video", "").strip()
                if video_title:
                    speak(f"Playing {video_title} on YouTube.")
                    search_url = f"https://www.youtube.com/results?search_query={video_title.replace(' ', '+')}"
                    import webbrowser
                    webbrowser.open(search_url)
                else:
                    speak("Please specify a video title to play on YouTube.")

           elif "stock analysis" in query.lower():
                
                stock_query = query.replace("stock analysis", "").strip()
                if stock_query:
                    from backend.feature import StockAnalyzer
                    speak(f"Analyzing stock data for {stock_query}.")
                    StockAnalyzer(stock_query)
                else:
                    speak("Please provide a stock symbol or company name for analysis.")

           else:
                from backend.feature import chatBot
                chatBot(query)


        else:
           speak("No command was given.")

    except Exception as e:
        print(f"An error occurred: {e}")
        speak("Sorry, something went wrong.")
    eel.ShowHood()
