import streamlit as st

st.title("🔠 Extract Initials from Full Name")

# User input for full name
full_name = st.text_input("Enter your full name:")

if st.button("Get Initials"):
    if full_name.strip() == "":
        st.warning("Please enter a valid full name.")
    else:
        # Split the name and extract the first character of each part
        name_parts = full_name.strip().split()
        initials = "".join([part[0].upper() for part in name_parts if part])

        st.subheader("🧾 Your Initials:")
        st.write(initials)
