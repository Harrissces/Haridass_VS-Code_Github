import streamlit as st
from pathlib import Path

# File to store names
FILE_PATH = "saved_names.txt"

st.set_page_config(page_title="📝 Name Saver App", layout="centered")
st.title("📝 Save and Display Names")

# --- Function to save name to file ---
def save_name(name):
    with open(FILE_PATH, "a", encoding="utf-8") as f:
        f.write(name.strip() + "\n")

# --- Function to read all names ---
def read_names():
    if Path(FILE_PATH).exists():
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    return []

# --- UI to add a new name ---
with st.form("name_form"):
    new_name = st.text_input("✍️ Enter a name to save:")
    submitted = st.form_submit_button("Save Name")

    if submitted:
        if new_name.strip():
            save_name(new_name)
            st.success(f"✅ '{new_name}' has been saved!")
        else:
            st.warning("⚠️ Please enter a valid name.")

# --- Display all saved names ---
st.subheader("📃 Saved Names")

names = read_names()

if names:
    st.info(f"Total Names Saved: {len(names)}")
    st.write("🧾 List of Names:")
    for i, name in enumerate(names, 1):
        st.write(f"{i}. {name}")
else:
    st.info("No names saved yet. Add one above!")
