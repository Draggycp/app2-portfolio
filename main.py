import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Alexandre Camargo Pansera")
    content = """
    Meu nome é Alexandre, aspirante a dev de programas brabos
    """
    st.info(content)

st.write("Below you can find some of the apps I have built in Python. "
        "Feel free to contact me through the contact page!")

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[0:10].iterrows():
            st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
            st.header(row["title"])