import streamlit as st
import time

st.set_page_config(page_title="⏳ Countdown Timer", layout="centered")
st.title("🚀 Countdown Timer")

if st.button("Start Countdown"):
    countdown_container = st.empty()

    for i in range(10, -1, -1):
        # Choose color and size for effect
        color = "red" if i <= 3 else "green" if i > 5 else "orange"

        countdown_container.markdown(
            f"<h1 style='text-align: center; color: {color}; font-size: 100px;'>{i}</h1>",
            unsafe_allow_html=True
        )
        time.sleep(1)

    # Display a final message
    countdown_container.markdown(
        "<h1 style='text-align: center; color: blue;'>🎉 Time's Up! 🎉</h1>",
        unsafe_allow_html=True
    )
