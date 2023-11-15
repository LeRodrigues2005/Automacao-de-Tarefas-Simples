import pyautogui
import time

# abrir osu!
pyautogui.press("win")
pyautogui.write("osu")
pyautogui.press("enter")
time.sleep(10)

# local da tela em que está o botão de iniciar:
pyautogui.click(x=915, y=852)
time.sleep(1)
pyautogui.click(x=1919, y=238)
time.sleep(1)
pyautogui.click(x=1237, y=671)