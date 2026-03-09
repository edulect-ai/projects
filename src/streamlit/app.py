import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("hello stream lit")

## Display a simple text
st.write("This is a simple text")

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10, 20, 30, 40]
})

## Display the data from
st.write("Here is the data from")
st.write(df)

## create line chart

chart_data = pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])
st.line_chart(chart_data)