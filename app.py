import streamlit as st

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Streamlit app
st.title("Celsius to Fahrenheit Converter")

# Input for Celsius temperature
celsius_temp = st.number_input("Enter temperature in Celsius:", value=0.0)

# Convert and display result
if st.button("Convert"):
    fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
    st.write(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")
