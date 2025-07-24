import streamlit as st
import math

st.set_page_config(page_title="🧮 Area Calculator", layout="centered")
st.title("🧮 Area Calculator for Circle, Rectangle & Triangle")

# Area calculation functions
def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

# Circle Area
st.header("🟠 Circle Area")
radius = st.number_input("Enter radius of the circle:", min_value=0.0, step=0.1, key="circle")
if st.button("Calculate Circle Area"):
    if radius == 0:
        st.warning("Radius must be greater than 0.")
    else:
        result = area_circle(radius)
        st.success(f"Area of Circle: {result:.2f} square units")

# Rectangle Area
st.header("🟦 Rectangle Area")
length = st.number_input("Enter length of the rectangle:", min_value=0.0, step=0.1, key="rect_len")
width = st.number_input("Enter width of the rectangle:", min_value=0.0, step=0.1, key="rect_wid")
if st.button("Calculate Rectangle Area"):
    if length == 0 or width == 0:
        st.warning("Length and width must be greater than 0.")
    else:
        result = area_rectangle(length, width)
        st.success(f"Area of Rectangle: {result:.2f} square units")

# Triangle Area
st.header("🔺 Triangle Area")
base = st.number_input("Enter base of the triangle:", min_value=0.0, step=0.1, key="tri_base")
height = st.number_input("Enter height of the triangle:", min_value=0.0, step=0.1, key="tri_height")
if st.button("Calculate Triangle Area"):
    if base == 0 or height == 0:
        st.warning("Base and height must be greater than 0.")
    else:
        result = area_triangle(base, height)
        st.success(f"Area of Triangle: {result:.2f} square units")
