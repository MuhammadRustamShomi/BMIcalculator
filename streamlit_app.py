import streamlit as st

# Title
st.title("Simple BMI Calculator")

# User inputs
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (m):", min_value=0.1, step=0.01)

# Calculate BMI when button is clicked
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is {bmi:.2f}")
    else:
        st.error("Height must be greater than 0.")

