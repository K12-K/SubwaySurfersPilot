import pyautogui
import time

print("Move your mouse to the target point. Coordinates will show in real time:")
while True:
    x, y = pyautogui.position()
    print(f"X: {x} Y: {y}", end="\r")
    time.sleep(0.1)
