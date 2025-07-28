import streamlit as st
import math

st.set_page_config(page_title="🧮 Math Functions: Factorial, Power, Square Root", layout="centered")
st.title("🧮 Math Calculator Functions")

# --- Define Functions ---

def calculate_factorial(n):
    try:
        return math.factorial(n)
    except ValueError:
        return "❌ Factorial is not defined for negative numbers."
    except:
        return "❌ Invalid input."

def calculate_power(base, exponent):
    return math.pow(base, exponent)

def calculate_sqrt(x):
    if x < 0:
        return "❌ Square root of negative number is not real."
    return math.sqrt(x)

# --- Factorial ---
st.header("🔢 Factorial (n!)")
n = st.number_input("Enter a non-negative integer (n):", min_value=0, step=1, format="%d")
if st.button("Calculate Factorial"):
    result = calculate_factorial(n)
    st.success(f"Factorial of {n} is: {result}")

# --- Power ---
st.header("⚡ Power (xⁿ)")
base = st.number_input("Enter base (x):", key="base")
exponent = st.number_input("Enter exponent (n):", key="exp")
if st.button("Calculate Power"):
    result = calculate_power(base, exponent)
    st.success(f"{base} raised to the power of {exponent} is: {result}")

# --- Square Root ---
st.header("√ Square Root")
value = st.number_input("Enter a number to find its square root:", key="sqrt")
if st.button("Calculate Square Root"):
    result = calculate_sqrt(value)
    st.success(f"Square root of {value} is: {result}")
