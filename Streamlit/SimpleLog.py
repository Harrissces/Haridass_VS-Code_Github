import streamlit as st
from datetime import datetime
from pathlib import Path

# Log file path
LOG_FILE = "activity_log.txt"

st.set_page_config(page_title="📅 Daily Activity Logger", layout="centered")
st.title("📝 Daily Activity Logger")

# --- Function to save activity with timestamp ---
def log_activity(activity_text):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{now}] {activity_text}\n")

# --- Function to read log ---
def read_log():
    if Path(LOG_FILE).exists():
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            return file.read()
    return "No activities logged yet."

# --- Input Form ---
with st.form("log_form"):
    activity = st.text_area("✍️ Write your activity:")
    submitted = st.form_submit_button("✅ Log Activity")

    if submitted:
        if activity.strip():
            log_activity(activity)
            st.success("Activity logged successfully!")
        else:
            st.warning("Please enter something before submitting.")

# --- Display Log History ---
st.subheader("📜 Activity History")
log_data = read_log()
st.text_area("Your Daily Activity Log", value=log_data, height=300)
