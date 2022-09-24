import pyautogui
import webbrowser
from time import sleep

phoneNumber = 'PHONE'

textToSend = 'text.txt'

webbrowser.open('https://api.whatsapp.com/send/?phone=34' + phoneNumber)

sleep(2)

with open(textToSend, 'r') as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
