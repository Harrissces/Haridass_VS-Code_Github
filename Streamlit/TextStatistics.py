import streamlit as st
import re

st.title("Paragraph Analyzer")
st.write("Counts the number of words, sentences, and characters.")

# Input text area
paragraph = st.text_area("Enter your paragraph here:")

if paragraph:
    # Count characters (excluding spaces)
    char_count = len(paragraph.replace(" ", ""))

    # Count words
    words = paragraph.split()
    word_count = len(words)

    # Count sentences using basic punctuation rule
    sentences = re.split(r'[.!?]+', paragraph.strip())
    sentence_count = len([s for s in sentences if s.strip()])

    # Display results
    st.subheader("Analysis Result:")
    st.write(f"**Words:** {word_count}")
    st.write(f"**Sentences:** {sentence_count}")
    st.write(f"**Characters (excluding spaces):** {char_count}")
