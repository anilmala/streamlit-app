# Import the necessary libraries
import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Basic Streamlit App")

# Sidebar
st.sidebar.title("Sidebar")
name = st.sidebar.text_input("Enter your name")
age = st.sidebar.number_input("Enter your age", min_value=0, max_value=100, step=1)

# Display a greeting
if name:
    st.write(f"Hello, {name}! You are {age} years old.")

# Displaying data
st.header("Random Data")
data = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['Column 1', 'Column 2']
)
st.write("Here is a table of random data:")
st.dataframe(data)

# Plotting a chart
st.header("Line Chart of Random Data")
st.line_chart(data)

# Slider
st.header("Slider Example")
slider_value = st.slider("Select a value", 0, 100)
st.write(f"The slider value is {slider_value}")

# Button
if st.button("Click me!"):
    st.write("Button clicked!")
