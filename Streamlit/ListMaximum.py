import streamlit as st

st.title("🔍 Find the Largest Number in a List (Without using max())")

# Input list from user
user_input = st.text_area("Enter numbers separated by commas (e.g. 12, 4, 56, 32, 8):")

if st.button("Find Largest"):
    try:
        # Convert input to list of integers
        numbers = [int(x.strip()) for x in user_input.split(",") if x.strip() != ""]

        # Initialize the first number as the largest
        largest = numbers[0]

        # Loop through the list to find the largest number
        for num in numbers[1:]:
            if num > largest:
                largest = num

        # Display result
        st.success(f"✅ The largest number in the list is: {largest}")

    except ValueError:
        st.error("❌ Please enter valid integers separated by commas.")
    except IndexError:
        st.warning("⚠️ Please enter at least one number.")
