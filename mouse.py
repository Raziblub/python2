import pyautogui

currentMouseX, currentMouseY = pyautogui.position()
print (currentMouseX, currentMouseY)
pyautogui.click(500, 1000)

pyautogui.moveTo(1900, 10)
#pyautogui.click()