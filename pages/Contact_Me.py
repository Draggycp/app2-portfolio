import streamlit as st


st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your e-mail address")
    message = st.text_area("Your message")
    email_button = st.form_submit_button("Submit")
    if email_button:
        message = message + user_email
            print("Pressed")
