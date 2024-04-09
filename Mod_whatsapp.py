# Whatsapp MOD
"""
Abre el whatsapp web y envia un mensaje 
a el numero ingresado
"""

import pyautogui,webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/send?phone=+573223980752')
sleep(10)
for i in range(1):
    pyautogui.typewrite('mensaje')
    pyautogui.press('enter')