import streamlit as st
from io import StringIO

st.set_page_config(page_title="📄 Text File Reader", layout="centered")
st.title("📄 Text File Analyzer: Line & Word Count")

# --- File Upload ---
uploaded_file = st.file_uploader("📤 Upload a text file (.txt)", type=["txt"])

if uploaded_file is not None:
    # Read the text file content
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    file_content = stringio.read()

    # Display preview
    st.subheader("📖 File Preview")
    st.text_area("Content:", value=file_content[:2000], height=250)

    # --- Count lines and words ---
    lines = file_content.strip().split("\n")
    words = file_content.split()

    total_lines = len(lines)
    total_words = len(words)

    # --- Show stats ---
    st.subheader("📊 File Statistics")
    st.write(f"📌 **Total Lines:** {total_lines}")
    st.write(f"📝 **Total Words:** {total_words}")
