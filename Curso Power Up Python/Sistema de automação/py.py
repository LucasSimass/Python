import pyautogui as py
import time 

py.PAUSE = 1.0
py.press("win")
py.write("Chrome")
py.press("enter")
time.sleep(2)
py.write("Gemini")
py.press("enter")
time.sleep(10)
py.click(x=620, y=670)
py.write("Sou um bot que está escrevendo isso agora")
py.press("enter")
time.sleep(2)
py.scroll(-5000)
time.sleep(30)
py.click(x=1342, y=13)
