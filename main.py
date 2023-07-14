import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg")

with col2:
    st.title("Eni Joseph Wanogho")
    content = """
    Hi, I am Joe, I am a Python Programmer, I graduated in 2018 with 
    a Bachelor of Science in Computer Science from the University of Benin"""
    st.info(content)

content = """ Find below information of some of the apps I have built using Python.
Feel free to contact me."""
st.write(content)

col3, col4 = st.columns(2)

df = pd.read_csv('data.csv', sep=",")
df.columns = df.columns.str.strip()

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
