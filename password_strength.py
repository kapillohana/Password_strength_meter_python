import re
import random
import string
import streamlit as st

# Blocking comon passwords
weak_passwords = ["password", "password1234", "12345678", "admin", "12344321"]

# Function to generate a strong password
def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# Function to check password strength
def check_password_strength(password):
    # First check if password is in weak passwords list
    if password.lower() in weak_passwords:
        st.error("🚫 This password is too common, Hackers can easily guess it.")
        return
    
    score = 0  # Start with score 0

    if len(password) >= 8:
        score += 1
    else:
        st.warning("❌ Password should be at least 8 characters long")

      # Cheking for uppercase and lowercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        st.warning("Include both uppercase and lowercase characters")

    # Checks for at least one digi (0-9)
    if re.search(r"\d", password):
        score += 1
    else:
        st.warning("Add at least one number (0-9)")

    # Checking for special Character
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        st.warning("Add at least one special character")

    # Assigning Strength Score
    if score == 4:
        st.success("✅ Strong Password")
    elif score == 3:
        st.warning("⚠️ Average Password, consider adding more features")
    else:
        st.error("❌ Weak Password - improve it using suggestions")

st.title("Password Strength Checker")

# Password suggestion section
if st.button("Generate Strong Password", key= "generate btn"):
    suggested_pwd = generate_strong_password()
    st.session_state.suggested_password = suggested_pwd

if 'suggested_password' in st.session_state:
    st.code(st.session_state.suggested_password)
    if st.button("Use This Password", key= "use btn"):
        st.session_state.password = st.session_state.suggested_password

# Asing user to Enter pasword
password = st.text_input("Enter your password:", 
                        type="password",
                        value=st.session_state.get('password', ''),
                        key= "pswd input")

# Checking strength of pswrd
if st.button("Check Strength", key="check_strength_btn"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please enter a password first")

