import streamlit as st

st.title("My First Streamlit Web App")
st.write("Welcome to my simple Streamlit website!")

name = st.text_input("Enter your name")
if name:
    st.write("Hello,", name + "!")
    
number = st.slider("Pick a number", 1, 100)
st.write("You selected:", number)
