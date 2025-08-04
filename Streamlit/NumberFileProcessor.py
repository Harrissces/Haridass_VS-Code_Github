import streamlit as st
from io import StringIO

st.set_page_config(page_title="🔢 Sum & Average from File", layout="centered")
st.title("📂 Number File Analyzer: Sum & Average")

# --- Upload file ---
uploaded_file = st.file_uploader("📤 Upload a text file with numbers (comma or newline separated)", type=["txt", "csv"])

if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    content = stringio.read()

    st.subheader("📄 File Content")
    st.code(content[:500])  # Preview

    # Try to parse numbers
    try:
        # Split by lines or commas
        raw_numbers = content.replace(",", "\n").split("\n")
        numbers = [float(x.strip()) for x in raw_numbers if x.strip() != ""]

        total = sum(numbers)
        avg = total / len(numbers) if numbers else 0

        # Results
        st.subheader("📊 Results")
        st.write(f"🔢 Total Numbers: `{len(numbers)}`")
        st.write(f"➕ Sum: `{total}`")
        st.write(f"📏 Average: `{avg}`")

    except ValueError:
        st.error("❌ Failed to parse numbers. Make sure your file contains only numbers separated by commas or newlines.")
