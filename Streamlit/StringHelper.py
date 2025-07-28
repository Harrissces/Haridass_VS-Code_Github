
import streamlit as st

st.set_page_config(page_title="🔤 String Helper", layout="centered")
st.title("🔤 String Functions: Capitalize | Reverse | Count Characters")

# --- Define Functions ---

def capitalize_text(text):
    return text.capitalize()

def reverse_text(text):
    return text[::-1]

def count_characters(text, include_spaces=True):
    if include_spaces:
        return len(text)
    else:
        return len(text.replace(" ", ""))

# --- User Input ---

input_text = st.text_input("Enter a word or sentence:")

if st.button("Apply String Functions"):
    if not input_text.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        st.subheader("✅ Results:")

        # Capitalized
        capitalized = capitalize_text(input_text)
        st.write(f"**Capitalized:** `{capitalized}`")

        # Reversed
        reversed_text = reverse_text(input_text)
        st.write(f"**Reversed:** `{reversed_text}`")

        # Character count
        count_with_spaces = count_characters(input_text)
        count_without_spaces = count_characters(input_text, include_spaces=False)

        st.write(f"**Character Count (with spaces):** {count_with_spaces}")
        st.write(f"**Character Count (without spaces):** {count_without_spaces}")
