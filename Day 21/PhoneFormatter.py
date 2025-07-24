import streamlit as st

st.set_page_config(page_title="📞 Phone Number Formatter", layout="centered")

st.title("📞 Format 10-Digit Number as (XXX) XXX-XXXX")

# Input from user
raw_number = st.text_input("Enter a 10-digit phone number (digits only):")

# Format function
def format_phone(number):
    return f"({number[:3]}) {number[3:6]}-{number[6:]}"

# Button action
if st.button("Format Number"):
    # Remove any non-digit characters
    digits_only = ''.join(filter(str.isdigit, raw_number))

    if len(digits_only) != 10:
        st.error("❌ Please enter exactly 10 digits.")
    else:
        formatted = format_phone(digits_only)
        st.success("✅ Formatted Number:")
        st.code(formatted, language="text")
