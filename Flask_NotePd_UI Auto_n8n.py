from flask import Flask, request, jsonify
import pyautogui
import time
import os
import subprocess

app = Flask(__name__)

@app.route('/write-to-notepad', methods=['POST'])
def write_to_notepad():
    data = request.get_json()

    # Validate payload
    if not data or 'message' not in data:
        return jsonify({"error": "Payload must include 'message' field"}), 400

    user_input = data['message']
    filename = "Harrissces_Local_n8n test.txt"
    file_path = os.path.join(os.path.expanduser("~"), "Desktop", filename)

    try:
        # Step 1: Create file if it doesn't exist
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                pass
            print(f"📄 File created: {file_path}")
            time.sleep(1)

        # Step 2: Open file in Notepad
        os.startfile(file_path)
        time.sleep(3)

        # Step 3: Move to end and write message
        pyautogui.hotkey("ctrl", "end")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(0.3)
        pyautogui.write(user_input, interval=0.05)

        # Step 4: Save the file
        time.sleep(0.5)
        pyautogui.hotkey("ctrl", "s")
        time.sleep(1)

        return jsonify({"status": "success", "message": "Text written and saved successfully."}), 200

    except Exception as e:
        return jsonify({"status": "error", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
