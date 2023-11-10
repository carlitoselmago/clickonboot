import pyautogui
import time

try:
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()
        
        # Print the position
        print(f"X: {x}, Y: {y}", end="\r")

        # Sleep for a short period to avoid flooding the console
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nExited.")
