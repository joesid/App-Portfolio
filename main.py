import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg", width=300)


with col2:
    st.title("Eni Joseph Wanogho")
    content = """
    Hi, I am Joe, I am a Python Programmer, I am a graduate
    of Computer Science, University of Benin"""
    st.info(content)