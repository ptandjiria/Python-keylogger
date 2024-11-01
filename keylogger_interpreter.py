#!/usr/bin/env python3

import re

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
        
        print(content)

except IOError:
    print(f"An error occurred")