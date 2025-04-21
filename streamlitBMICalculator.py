import streamlit as st

st.title("BMI Calculator")

height = st.number_input("Enter your height (in meters)")
weight = st.number_input("Enter your weight (in kilograms)")

if height > 0 and weight > 0:
    bmi = weight / (height ** 2)
    st.write("Your BMI is:", round(bmi, 2))
