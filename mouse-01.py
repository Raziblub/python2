import pyautogui

offset=10
distance = 200-(2*offset)
speed=.1
ecart=10

pyautogui.moveTo(1200+offset, 400+offset)

while distance > ecart: # tant que distance > ecart
    print(distance)
    pyautogui.drag(distance, 0, duration=speed)   # move right
    distance = distance - ecart
    if distance < 0 : distance = 0
    pyautogui.drag(0, distance, duration=speed)   # move down
    pyautogui.drag(-distance, 0, duration=speed)  # move left
    distance -= ecart
    if distance < 0 : distance = 0
    pyautogui.drag(0, -distance, duration=speed)  # move up
