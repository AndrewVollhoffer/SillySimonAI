import keyboard
import time

running = "true"

def check_escape():
    print("check escape")
    if keyboard.read_key() == 'esc':
        "SimonAI.py".stop()

def auto_keyboard():
    print("auto keyboard")
    keyboard.press_and_release('a')
    time.sleep(0.5)


print("Program started...")

while(running == "true"):
    
    check_escape()
    auto_keyboard()

print("Program stopped.")