import pyautogui
import time
pyautogui.PAUSE = 0.6
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("google")
pyautogui.press("enter")
pyautogui.click(x=331, y=287)
pyautogui.write("whatsapp")
pyautogui.press("enter")
pyautogui.click(x=71, y=476)
time.sleep(15)
pyautogui.click(x=257, y=410)
pyautogui.write("Isso aqui foi escrito totalmente por um bot!")
pyautogui.press("enter")
