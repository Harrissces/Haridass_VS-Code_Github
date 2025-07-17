import streamlit as st

st.title("🔠 Vowel Counter")

# User input
text = st.text_input("Enter a word or sentence:")

# Define vowels
vowels = ['a', 'e', 'i', 'o', 'u']

if st.button("Count Vowels"):
    found_vowels = [char for char in text.lower() if char in vowels]

    if found_vowels:
        st.success(f"✅ Total vowels found: {len(found_vowels)}")
        st.write("📝 Vowels list:", found_vowels)
    else:
        st.warning("No vowels found in the input.")
