import streamlit as st

st.set_page_config(page_title="🔁 Unit Converter", layout="centered")
st.title("🔁 Unit Converter: Feet ⇄ Meters & Pounds ⇄ Kilograms")

st.markdown("Choose a conversion type and enter the value:")

# --- Conversion Functions ---
def feet_to_meters(feet):
    return feet * 0.3048

def meters_to_feet(meters):
    return meters / 0.3048

def pounds_to_kilograms(pounds):
    return pounds * 0.453592

def kilograms_to_pounds(kg):
    return kg / 0.453592

# --- User Inputs ---
conversion_type = st.selectbox(
    "📦 Select Conversion Type:",
    ("Feet ➡ Meters", "Meters ➡ Feet", "Pounds ➡ Kilograms", "Kilograms ➡ Pounds")
)

value = st.number_input("🔢 Enter value to convert:", format="%.4f")

# --- Conversion Logic ---
if st.button("Convert"):
    if conversion_type == "Feet ➡ Meters":
        result = feet_to_meters(value)
        st.success(f"{value} feet = {result:.4f} meters")
    elif conversion_type == "Meters ➡ Feet":
        result = meters_to_feet(value)
        st.success(f"{value} meters = {result:.4f} feet")
    elif conversion_type == "Pounds ➡ Kilograms":
        result = pounds_to_kilograms(value)
        st.success(f"{value} pounds = {result:.4f} kilograms")
    elif conversion_type == "Kilograms ➡ Pounds":
        result = kilograms_to_pounds(value)
        st.success(f"{value} kilograms = {result:.4f} pounds")
