# It  might be helpful here to use a virtual environment
import pyautogui
import time

def keep_alive():
    try:
        while True:
            # Move in a single command instead of two
            pyautogui.moveRel(100, 100, duration=0.2)
            pyautogui.moveRel(-100, -100, duration=0.2)
            
            # Perform a click action
            pyautogui.click()
            
            # Adjust sleep time to control frequency of activity
            time.sleep(20)
    except KeyboardInterrupt:
        print("Script terminated by user")

if __name__ == "__main__":
    keep_alive()
