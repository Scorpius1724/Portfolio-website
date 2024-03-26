import streamlit as st


st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        print("Hello world")