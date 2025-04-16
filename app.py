import streamlit as st

from password_strength import check_password_strength

st.title("🔒 Password Strength Checker")
password = st.text_input("Enter a password:", type="password")

if st.button("Check Strength"):
    check_password_strength(password)