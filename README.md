# **Jarvis AI Assistant**

Jarvis is a powerful AI assistant developed by **Faizan Khan**. Designed to streamline everyday tasks, Jarvis is equipped with a wide array of features such as system monitoring, file management, volume control, web browsing, and even stock analysis. It is user-friendly, versatile, and can be controlled via both voice commands and text inputs.

---

## **Features Overview**

The table below summarizes the various features of Jarvis AI Assistant:

| **Feature Category**       | **Commands**                                                  | **Description**                                                                 |
|----------------------------|--------------------------------------------------------------|---------------------------------------------------------------------------------|
| **Personal Info**           | `Who is your developer?`                                     | Displays developer info and opens Instagram profile of Faizan Khan.            |
|                            | `Tell me about yourself`                                     | Provides an introduction to Jarvis and its features.                           |
| **System Information**      | `Battery status`                                             | Displays battery percentage and charging status.                               |
|                            | `System specifications`                                      | Provides OS, processor, and CPU core details.                                  |
| **File Management**         | `Create folder [name]`                                       | Creates a new folder with the specified name.                                  |
|                            | `Delete file [name]`                                         | Deletes the specified file.                                                    |
| **Volume Control**          | `Increase volume`                                            | Increases system volume by 5%.                                                 |
|                            | `Mute volume`                                                | Mutes system volume.                                                           |
| **Clipboard Management**    | `Show clipboard`                                             | Displays the current clipboard content.                                        |
|                            | `Copy to clipboard [text]`                                   | Copies specified text to the clipboard.                                        |
| **Reminders**               | `Set a reminder [task]`                                     | Sets a reminder with a message for 1 minute from the current time.             |
| **System Control**          | `Shut down system`                                           | Shuts down the system after a 5-second delay.                                  |
|                            | `Restart system`                                             | Restarts the system after a 5-second delay.                                    |
| **Web Browsing**            | `Open YouTube`                                               | Opens YouTube in a web browser.                                                |
|                            | `Play YouTube video [title]`                                 | Searches and plays the specified YouTube video.                                |
| **Stock Analysis**          | `Stock analysis [symbol]`                                   | Analyzes stock data for the specified company or stock symbol.                 |
| **General Queries**         | Any other queries                                           | Uses a chatbot to respond appropriately.                                       |

---

## **Technologies Used**

Jarvis leverages various Python modules and libraries to offer its extensive range of features:

1. **Core Technologies**
   - `Python 3.x`: The primary programming language for the assistant.
   - `Eel`: Enables web integration and UI features for better interactivity.
   - `SpeechRecognition`: For voice command recognition (optional).
   - `pyttsx3`: Converts text to speech for voice responses.

2. **System Operations**
   - `os`: For managing files and folders (e.g., creating and deleting files).
   - `platform`: Retrieves detailed system information.
   - `psutil`: Used to check battery status.

3. **Clipboard Management**
   - `pyperclip`: Allows copying and pasting of clipboard data.

4. **Web Browsing**
   - `webbrowser`: Opens URLs in a web browser (e.g., YouTube, Instagram).

5. **Error Handling**
   - Custom exception handling to ensure smooth execution.

6. **Stock Analysis**
   - `requests`: For fetching stock data from APIs or external services (expandable as needed).

---

## **Installation Instructions**

Follow these steps to install and run Jarvis AI Assistant:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/faizan-khanx/jarvis
   cd jarvis
   ```

2. **Cookies**
   - Install Any Cookies Editor
   - go to hugging face and select any model
   - and copy its cookies in json format
   - open any code editor and in backend folder create a json file with name cookie.json
   - paste cookies in cookie.json and save it
   - **Example JSON Structure for Cookies**:
  ```json
  [
    {
        "domain": "huggingface.co",
        "expirationDate": xyz,
        "hostOnly": true,
        "httpOnly": true,
        "name": "hf-chat",
        "path": "/",
        "sameSite": "lax",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "xyz"
    },
    {
        "domain": "huggingface.co",
        "expirationDate": xyz,
        "hostOnly": true,
        "httpOnly": true,
        "name": "token",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "xyz"
    }
 ]
   ```
   - open the folder in cmd install require pips and you are set to go with
  
  To enhance the **Jarvis AI Assistant** documentation, you can add **examples for coding usage**, showing how each feature or module is used in different scenarios. Below are examples to include for different categories:

---

### **Code Examples for Feature Usage**

#### **1. System Information**
- **Battery Status**  
This command fetches and displays the battery percentage and charging status.  
**Code Snippet**:
```python
import psutil

def battery_status():
    battery = psutil.sensors_battery()
    percent = battery.percent
    charging = "Charging" if battery.power_plugged else "Not Charging"
    print(f"Battery: {percent}% | Status: {charging}")

battery_status()
```

---

#### **2. File Management**
- **Create Folder**  
You can create a new folder using the following code:
```python
import os

def create_folder(folder_name):
    os.makedirs(folder_name, exist_ok=True)
    print(f"Folder '{folder_name}' created successfully.")

create_folder("MyNewFolder")
```

- **Delete File**  
This code snippet demonstrates how to delete a file:
```python
import os

def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    else:
        print(f"File '{file_name}' not found.")

delete_file("sample.txt")
```

---

#### **3. Volume Control**
- **Increase Volume**  
To control system volume, you can use:
```python
import pycaw  # Example for Windows users

# Code to increase volume using the system's audio management APIs
```

---

#### **4. Web Browsing**
- **Open YouTube**  
This demonstrates opening a web page:
```python
import webbrowser

def open_youtube():
    webbrowser.open("https://www.youtube.com")

open_youtube()
```

---

#### **5. Clipboard Management**
- **Copy to Clipboard**  
Example to copy text to the clipboard:
```python
import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)
    print(f"Copied to clipboard: {text}")

copy_to_clipboard("Hello, Jarvis!")
```

- **Show Clipboard Content**  
Displays the current clipboard content:
```python
def show_clipboard():
    content = pyperclip.paste()
    print(f"Clipboard Content: {content}")

show_clipboard()
```

---

#### **6. Stock Analysis**
- **Stock Data Fetching**  
To fetch and analyze stock data:
```python
import requests

def stock_analysis(symbol):
    api_url = f"https://api.example.com/stock/{symbol}"  # Replace with a real API
    response = requests.get(api_url)
    data = response.json()
    print(f"Stock Data for {symbol}: {data}")

stock_analysis("AAPL")
```
## Contributing
Contributions are welcome! To contribute, fork the repository and submit a pull request with your improvements.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [E-Mail Me](mailto:fk776794@gmail.com?subject=Feedback%20on%20Faizan%20Net&body=Hello%20Faizan,%0A%0AI%20have%20some%20feedback%20to%20share%20about%20your%20Faizan%20Net%20tool.%0A%0A%2D%20Issue%2FComplaint%3A%20[Please%20describe%20the%20issue%20or%20complaint]%0A%2D%20Suggestions%2FChanges%3A%20[Please%20provide%20your%20suggestions%20or%20changes]%0A%0AThank%20you!%0A%0ARegards,%0A[Your%20Name])

<!-- display the social media buttons in your README -->

[![instagram](https://github.com/shikhar1020jais1/Git-Social/blob/master/Icons/Instagram.png (Instagram))][2]
[![twitter](https://github.com/shikhar1020jais1/Git-Social/blob/master/Icons/Twitter.png (Twitter))][3]
[![linkedin](https://github.com/shikhar1020jais1/Git-Social/blob/master/Icons/LinkedIn.png (LinkedIn))][4]
[![github](https://github.com/shikhar1020jais1/Git-Social/blob/master/Icons/Github.png (Github))][5]

<!-- To Link your profile to the media buttons -->

[2]: https://www.instagram.com/EthicalFaizan
[3]: https://www.twitter.com/EthicalFaizan
[4]: https://www.linkedin.com/in/EthicalFaizan
[5]: https://www.github.com/faizan-khanx

## GITHUB STATS

![Faizan's GitHub stats](https://github-readme-stats.vercel.app/api?username=faizan-khanx&show=reviews,discussions_started,discussions_answered,prs_merged,prs_merged_percentage&theme=dark#gh-dark-mode-only)
