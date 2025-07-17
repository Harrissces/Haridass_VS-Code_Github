import streamlit as st

st.title("🧾 Full Name Formatter")

# Input: Full name with at least two spaces
full_name = st.text_input("Enter your full name (at least 3 parts, e.g. John Michael Smith):")

if st.button("Format Name"):
    # Split the name by spaces
    parts = full_name.strip().split()

    if len(parts) >= 3:
        first = parts[0]
        middle = " ".join(parts[1:-1])
        last = parts[-1]

        # Different formats
        format1 = f"{first} {middle} {last}"                      # First Middle Last
        format2 = f"{last}, {first} {middle}"                    # Last, First Middle
        format3 = f"{first[0]}. {' '.join([m[0]+'.' for m in parts[1:-1]])} {last}"  # F. M. Last
        format4 = f"{last}, {first[0]}.{''.join([m[0] for m in parts[1:-1]])}."      # Last, F.M.

        st.subheader("📌 Name Formats:")
        st.write("1️⃣ First Middle Last:", format1)
        st.write("2️⃣ Last, First Middle:", format2)
        st.write("3️⃣ F. M. Last:", format3)
        st.write("4️⃣ Last, F.M.:", format4)
    else:
        st.error("❌ Please enter at least a First, Middle, and Last name (minimum 2 spaces).")
