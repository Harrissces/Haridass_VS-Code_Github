import streamlit as st
from datetime import date, datetime

st.set_page_config(page_title="📅 Leap Year & Age Calculator", layout="centered")
st.title("📅 Leap Year Checker & Age Calculator")

# --- Function to check leap year ---
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# --- Function to calculate age ---
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

# --- Leap Year Checker ---
st.header("🔁 Leap Year Checker")
year = st.number_input("Enter a year to check:", step=1, format="%d", min_value=1)

if st.button("Check Leap Year"):
    if is_leap_year(int(year)):
        st.success(f"✅ Yes, {int(year)} is a Leap Year!")
    else:
        st.error(f"❌ No, {int(year)} is not a Leap Year.")

# --- Age Calculator ---
st.header("🎂 Age Calculator")
dob = st.date_input("Select your Date of Birth:", min_value=date(1925, 1, 1), max_value=date.today(), value=date(2000, 1, 1))

if st.button("Calculate Age"):
    if dob > date.today():
        st.warning("🚫 Date of Birth cannot be in the future.")
    else:
        age = calculate_age(dob)
        st.success(f"🎉 You are {age} years old.")
