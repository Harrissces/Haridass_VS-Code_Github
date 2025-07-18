import streamlit as st

st.title("🔁 Reverse Each Word in a Sentence")

# User input
sentence = st.text_input("Enter a sentence:")

if st.button("Reverse Words"):
    if sentence.strip() == "":
        st.warning("Please enter a sentence.")
    else:
        # Split sentence into words, reverse each word, then join back
        reversed_words = " ".join([word[::-1] for word in sentence.split()])
        
        st.subheader("📝 Reversed Words Sentence:")
        st.write(reversed_words)
