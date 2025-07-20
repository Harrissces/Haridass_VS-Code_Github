import streamlit as st

st.set_page_config(page_title="🔤 Letter Shifter", layout="centered")

st.title("🔤 Shift Each Letter by 1 Position")

st.markdown("""
This app shifts each **alphabet letter** in your input **forward by 1** in the alphabet.  
- `a` → `b`, `z` → `a`, `Y` → `Z`  
- Non-letters like `1`, `!`, and spaces are **not changed**
""")

# Input box
user_input = st.text_input("✍️ Enter a word or sentence:")

def shift_letter(char):
    if char.isalpha():
        if char.islower():
            return chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
        else:
            return chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
    else:
        return char  # Non-alphabet characters stay unchanged

# Action button
if st.button("🔁 Shift Letters"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        shifted = "".join(shift_letter(c) for c in user_input)
        st.subheader("✅ Shifted Result:")
        st.code(shifted, language="text")
