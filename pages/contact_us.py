import streamlit as st
from send_email import send_email
import pandas 

st.header("Contact me!")
df = pandas.read_csv("topics.csv")
with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    selectbox = st.selectbox("What topic do you want to discuss?", df["topic"])
    raw_user_message = st.text_area("Your message")
    user_message = f"""\
Subject: Portfolio website message from {user_email} 

From: {user_email}
Topic: {selectbox}
{raw_user_message}
    """
    button = st.form_submit_button("Submit")
    if button:
        send_email(user_message)
        st.info("Your email was sent successfully!")