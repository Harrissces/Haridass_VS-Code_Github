import streamlit as st

st.title("Email Username Extractor")

# Input field for email address
email = st.text_input("Enter your email address:")

# Extract and display username
if email:
    if "@" in email:
        username = email.split("@")[0]
        st.success(f"Username: {username}")
    else:
        st.error("Invalid email address. Please include '@'.")
