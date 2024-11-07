#!/usr/bin/bash

# Note: modifier keys include Shift, Control, Alt, Windows keys

# Test 1: test single key presses (alphanumeric characters only)
echo "Hello my name is Phoebe and I am 20 years old" | python3 keylogger.py
echo "Hello my name is Phoebe and I am 20 years old" > expected_keylog.txt
./keylogger_interpreter.sh > actual_keylog.txt
if ! diff expected_keylog.txt received_logs.txt; then
    echo "Test 1: successful implementation of single key presses (alphanumeric characters only)"
else
    echo "Test 1: implementation of single key presses (alphanumeric characters only) has failed."
fi

# Test 2: test single key presses (any ASCII characters without shift)
echo "Hello my name is Phoebe and I like eating pizza (Supreme is suuuper 'yummers' ;/.,'][]" | python3 keylogger.py
echo "Hello my name is Phoebe and I like eating pizza (Supreme is suuuper 'yummers' ;/.,'][]" > expected_keylog.txt
./keylogger_interpreter.sh > actual_keylog.txt
if ! diff expected_keylog.txt received_logs.txt; then
    echo "Test 2: successful implementation of single key presses (any ASCII characters without shift)"
else
    echo "Test 2: implementation of single key presses (any ASCII characters without shift) has failed."
fi

# Test 3: test double key presses (shift key + other characters)
echo "Hello!!! my name is Phoebe and I like eating pizza (Supreme is suuuper "*yummers*" :))" | python3 keylogger.py
echo "Hello!!! my name is Phoebe and I like eating pizza (Supreme is suuuper "*yummers*" :))" > expected_keylog.txt
./keylogger_interpreter.sh > actual_keylog.txt
if ! diff expected_keylog.txt received_logs.txt; then
    echo "Test 3: successful implementation of double key presses (shift key + other characters)"
else
    echo "Test 3: implementation of double key presses (shift key + other characters) has failed."
fi

# Test 4: test double key presses (two modifiers at a time)
echo "Hello!!! my name is Phoebe and I like eating pizza (Supreme is suuuper "*yummers*" :))" | python3 keylogger.py
echo "Hello!!! my name is Phoebe and I like eating pizza (Supreme is suuuper "*yummers*" :))" > expected_keylog.txt
./keylogger_interpreter.sh > actual_keylog.txt
if ! diff expected_keylog.txt received_logs.txt; then
    echo "Test 4: successful implementation of double key presses (two modifiers at a time)"
else
    echo "Test 4: implementation of double key presses (two modifiers at a time) has failed."
fi

# Test 5: test triple key presses (three modifiers at a time)