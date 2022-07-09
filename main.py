 import os
import webbrowser
import pyautogui
import time

def ancii():
    print("""
██     ██ ██   ██  █████  ████████ ███████  █████  ██████  ██████  
██     ██ ██   ██ ██   ██    ██    ██      ██   ██ ██   ██ ██   ██ 
██  █  ██ ███████ ███████    ██    ███████ ███████ ██████  ██████  
██ ███ ██ ██   ██ ██   ██    ██         ██ ██   ██ ██      ██      
 ███ ███  ██   ██ ██   ██    ██    ███████ ██   ██ ██      ██      
    """)

def sent():
    print("""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌ ▀▀▀▀█░█▀▀▀▀ 
▐░▌          ▐░▌          ▐░▌▐░▌    ▐░▌     ▐░▌     
▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌     ▐░▌     
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌     ▐░▌     
 ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌     ▐░▌     
          ▐░▌▐░▌          ▐░▌    ▐░▌▐░▌     ▐░▌     
 ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌     ▐░▌     
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌     ▐░▌     
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀       ▀      
    """)

while 69 < 420:

    os.system("cls")
    ancii()
    number = input("What number would you like to send the message to: ")
    message = input("What is the message you want to send: ")

    os.system("cls")
    ancii()
    webbrowser.open(f"https://web.whatsapp.com/send?phone={number}&text={message}")
    time.sleep(10)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'f4')

    os.system("cls")
    sent()
