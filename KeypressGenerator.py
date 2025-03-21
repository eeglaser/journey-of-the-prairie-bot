from pynput.keyboard import Controller, Key
import time

""" This script generates keypresses based on an input sequence of 1s and 0s.
The sequence should always be 9 elements long.
If an element is a 1, then the key corresponding to that index will be pressed down.
If an element is a 0, then the corresponding key will be released.
The mapping for each index to its corresponding key are as follows:
[W, A, S, D, ArrowUp, ArrowLeft, ArrowDown, ArrowRight, Spacebar]
"""
keyboard = Controller()
# The index of a 1 or 0 determines the key it corresponds to.
# This sequence outlines that mapping.
KEY_MAPPING = [
    'w', 'a', 's', 'd', 
    Key.up, Key.left, Key.down, Key.right, 
    Key.space
]

# Track currently pressed keys
pressed_keys = set()

# TODO: constrain type of sequence to be the type outputted by the NN
def process_input(sequence):
    global pressed_keys
    time.sleep(0.01)

    for i, char in enumerate(sequence):
        if i >= len(KEY_MAPPING):  # Ignore extra input
            break
        
        key = KEY_MAPPING[i]

        if char == '1' and key not in pressed_keys:
            keyboard.press(key)
            pressed_keys.add(key)

        elif char == '0' and key in pressed_keys:
            keyboard.release(key)
            pressed_keys.remove(key)

# This is used to make outputs prettier in unit tests.
def press_enter():
    keyboard.press(Key.enter)