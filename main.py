import pyautogui
import time

def main():
    # Wait for 10 seconds (to allow everything to load after startup)
    time.sleep(30)

    # Coordinates where to click (x, y)
    x, y = 100, 200

    # Move the mouse to the specified coordinates and click
    pyautogui.click(x, y)

if __name__ == "__main__":
    main()