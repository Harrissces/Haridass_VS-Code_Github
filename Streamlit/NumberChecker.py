import streamlit as st

st.set_page_config(page_title="📊 List Statistics", layout="centered")
st.title("📊 List Analyzer: Max, Min, Sum & Average")

st.markdown("Enter a list of numbers (comma-separated) like: `10, 25, 7, 42, 3`")

# --- Define Functions ---
def get_max(numbers):
    return max(numbers)

def get_min(numbers):
    return min(numbers)

def get_sum(numbers):
    return sum(numbers)

def get_average(numbers):
    return sum(numbers) / len(numbers)

# --- User Input ---
user_input = st.text_input("🔢 Enter numbers separated by commas:")

if st.button("Calculate Statistics"):
    if not user_input.strip():
        st.warning("⚠️ Please enter some numbers.")
    else:
        try:
            # Convert input to a list of floats
            numbers = [float(x.strip()) for x in user_input.split(",") if x.strip()]

            if len(numbers) == 0:
                st.warning("⚠️ The list is empty after cleaning.")
            else:
                st.subheader("✅ Results:")
                st.write(f"🔺 Maximum: `{get_max(numbers)}`")
                st.write(f"🔻 Minimum: `{get_min(numbers)}`")
                st.write(f"➕ Sum: `{get_sum(numbers)}`")
                st.write(f"📏 Average: `{get_average(numbers):.2f}`")

        except ValueError:
            st.error("❌ Please enter only valid numbers separated by commas.")
