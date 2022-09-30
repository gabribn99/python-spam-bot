import pyautogui
import webbrowser
from time import sleep

phoneNumber = input('Indique el número de teléfono: ')
sendType = int(
    input('Indique el tipo de envío: \n0. Reiterado\n1. Por linea\n>'))

textToSend = 'text.txt'


def openWhatsapp():
    webbrowser.open('https://api.whatsapp.com/send/?phone=34' +
                    phoneNumber.replace(' ', ''))
    sleep(2)


if sendType == 0:
    times = int(
        input('Indique la cantidad de veces que desea enviar el mensaje: '))
    text = input('Indique el texto que desea enviar: ')
    openWhatsapp()
    for i in range(times):
        pyautogui.typewrite(text)
        pyautogui.press("enter")

if sendType == 1:
    openWhatsapp()
    with open(textToSend, 'r') as file:
        for line in file:
            for word in line.split(' '):
                pyautogui.typewrite(word)
                pyautogui.press("enter")
