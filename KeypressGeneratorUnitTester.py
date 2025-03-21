from KeypressGenerator import process_input, press_enter
from pynput.keyboard import Listener, Key
import time

# Press this key to begin tests.
# Recommended to open a notepad, doc, or the game first, so that you can see the inputs happen.
START_KEY = Key.enter

# TESTS ------------------------------------------------------------------------------------------

# Test should press "wasd "
def test_keypresses_characters_each():
    test_sequences = [
        "100000000", # Press only W
        "010000000", # Press only A
        "001000000", # Press only S
        "000100000", # Press only D
        "000000001", # Press only Spacebar
        "000000000" # Release all
    ]
    for seq in test_sequences:
        process_input(seq)

# Test should process "w" many times
def test_keypresses_characters_repeated():
    for i in range(50):
        process_input("100000000")
    process_input("000000000")

# Test should press "awawawa"
def test_keypresses_characters_alternating():
    test_sequences = [
        "010000000",
        "100000000",
        "010000000",
        "100000000",
        "010000000",
        "100000000",
        "010000000",
        "000000000" # Release all
    ]
    for seq in test_sequences:
        process_input(seq)

# test should press "s" a lot
def test_keypresses_characters_held():
    for i in range(500):
        process_input("001000000")
    process_input("000000000")

def test_keypresses_arrows_held():
    process_input("000010000")
    time.sleep(2)
    process_input("000000000")

def test_keypresses_arrows_repeated():
    for i in range(100):
        process_input("000010000")
    process_input("000000000")

# STUFF TO RUN TESTS ------------------------------------------------------------------------------------------

def run_all_tests():
    tests_sequence = [
        test_keypresses_characters_each,
        test_keypresses_characters_repeated,
        test_keypresses_characters_alternating,
        test_keypresses_characters_held,
        test_keypresses_arrows_held,
        test_keypresses_arrows_repeated
    ]
    print("Start key detected. Beginning tests.\n")
    for func in tests_sequence:
        func()
        time.sleep(1)
        #press_enter() 
    print("Finished tests.\n")

def on_press(key):
    if key == START_KEY: 
        run_all_tests()
        return False

def listen_for_start_key():
    print("Listening for start key: {START_KEY}\n")
    with Listener(on_press=on_press) as listener:
        listener.join()  # Keeps listening until manually stopped

if __name__ == "__main__":
    listen_for_start_key()
    