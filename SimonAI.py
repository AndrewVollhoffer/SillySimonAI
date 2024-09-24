from pynput.keyboard import Key, Controller
from pynput import keyboard
import time
import os

def auto_press(key):
    Simon.press(key)
    Simon.release(key)
    time.sleep(0.2)

def on_press(key):
    # try:
        # print('alphanumeric key {0} pressed'.format(
            # key.char))
    # except AttributeError:
        # print('special key {0} pressed'.format(
            # key))
        
    if key == keyboard.Key.esc:
        os._exit(1)

def on_release(key):
    # print('{0} released'.format(
        # key))
    pass

Simon = Controller()

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

running = True

########START PROGRAM########

print("Program started...")


while(running):

    auto_press('a')

    

print("Program stopped.")