import pyautogui
import time
import os
import subprocess
import sys

# ✅ Step 1: Get message from command-line argument
if len(sys.argv) < 2:
    print("Usage: python Harrissces_Localn8n_Test.py \"Your message here\"")
    sys.exit()

user_input = sys.argv[1]
filename = "Harrissces_Local_n8n test.txt"
file_path = os.path.join(os.path.expanduser("~"), "Desktop", filename)

# ✅ Step 2: Create the file if it does not exist
if not os.path.exists(file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        pass  # Empty file just to initialize
    print(f"📄 File created: {file_path}")
    time.sleep(1)

# ✅ Step 3: Open the file using Notepad
os.startfile(file_path)
time.sleep(3)  # Let Notepad fully load and get focus

# ✅ Step 4: Move to end, add newline, then write the message
pyautogui.hotkey("ctrl", "end")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(0.3)
pyautogui.write(user_input, interval=0.05)

# ✅ Step 5: Save the file
time.sleep(0.5)
pyautogui.hotkey("ctrl", "s")
time.sleep(1)

print("✅ Message written and file saved successfully.")
