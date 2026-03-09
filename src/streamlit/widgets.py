## create more interactive app
import streamlit as st
import pandas as pd
st.title("Streamlit Text Input")

name = st.text_input("Enter your name")
age = st.slider("Select you age:",0,100)
if name:
    st.write(f"Hello {name}")

st.write(f"your age is {age}")


### options drop down
options = ["JS","Java","Python","C++"]
choice = st.selectbox("Choose your favourite language", options)
st.write(f"You selected: {choice}")


### Displaying data frames
data = {
    "Name": ["John","Jane","Jake","Jill"],
    "Age": [28,24,35,40]
}

df = pd.DataFrame(data)
st.write(df)

## file updloader

uploaded_file = st.file_uploader("Choose a csv file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

