# Currently written for Smash Remix.

from pynput.keyboard import Key, Controller
from pynput import keyboard
import time
import os
import random


############# DECLARATIONS #############


LEFT = 'a'
RIGHT = 'd'
UP = 'w'
DOWN = 's'

SPECIAL = 'j'
ATTACK = 'k'
ACTION = 'l'
L1 = 'q'
R1 = 'e'

# ~ 14 TOTAL METHODS ~ # 
############# INPUT METHODS #############


def auto_press(key, length = 0.2):
    Simon.press(key)
    time.sleep(length)
    Simon.release(key)


### MOVEMENT ###


def move_right_short():
    auto_press(RIGHT, 0.25)

def move_right_long():
    auto_press(RIGHT, .5)

def move_left_short():
    auto_press(LEFT, .25)

def move_left_long():
    auto_press(LEFT, .5)

# Jumping is VERY risky.
def jump():
    auto_press(UP)

def duck():
    auto_press(DOWN)


### TAUNT/ROLL/GRAB ###


def taunt():
    auto_press(L1)

def guard():
    auto_press(ACTION)

def grab():
    direction = random.randint(0, 1)
    with Simon.pressed(ACTION):
        auto_press(ATTACK)

    time.sleep(1)
    if direction == 0:
        move_right_short()
    else:
        move_left_short()

def roll():
    direction = random.randint(0, 1)
    with Simon.pressed(ACTION):
        if direction == 0:
            move_right_short()
        else:
            move_left_short()


### NORMAL ATTACKS ###


def jab():
    auto_press(ATTACK)

def smash_attack():
    direction = random.randint(0, 2)
    if direction == 0:
        with Simon.pressed(LEFT):
            auto_press(ATTACK)
    elif direction == 1:
        with Simon.pressed(RIGHT):
            auto_press(ATTACK)
    elif direction == 2:
        with Simon.pressed(UP):
            auto_press(ATTACK)


### SPECIAL ATTACKS ###


def special():
    auto_press(SPECIAL)

def special_attack():
    direction = random.randint(0, 1)
    if direction == 0:
        with Simon.pressed(UP):
            auto_press(SPECIAL)
    elif direction == 1:
        with Simon.pressed(DOWN):
            auto_press(SPECIAL)


############# KEYBOARD LISTENING METHODS #############


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


############# INITIALIZATION #############


Simon = Controller()

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

running = True

######## START PROGRAM ########


print("Program started...")

while(running):

    choice = random.randint(0, 13)

    match(choice):
        case 0:
            move_right_short()
        case 1:
            move_right_long()
        case 2:
            move_left_short()
        case 3:
            move_left_long()
        case 4:
            jump()
        case 5:
            duck()
        case 6:
            taunt()
        case 7:
            guard()
        case 8:
            grab()
        case 9:
            roll()
        case 10:
            jab()
        case 11:
            smash_attack()
        case 12:
            special()
        case 13:
            special_attack()
        case _:
            taunt()       

    # time.sleep(1)

print("Program stopped.")