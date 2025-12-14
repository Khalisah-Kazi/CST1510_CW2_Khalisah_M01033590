import streamlit as st
from app.services.user_services import register_user, login_user

st.set_page_config(page_title="Login", layout="centered")

st.title("🔐 Intelligence Platform")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    st.success("Already logged in!")
    st.switch_page("pages/mini_dashboard.py")

tab1, tab2 = st.tabs(["Login", "Register"])

# ---------- LOGIN ----------
with tab1:
    st.subheader("Login")

    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")

    if st.button("Login"):
        success, msg = login_user(username, password)
        if success:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(msg)
            st.switch_page("pages/mini_dashboard.py")
        else:
            st.error(msg)

# ---------- REGISTER ----------
with tab2:
    st.subheader("Register")

    new_user = st.text_input("Username", key="reg_user")
    new_pass = st.text_input("Password", type="password", key="reg_pass")

    if st.button("Register"):
        success, msg = register_user(new_user, new_pass)
        if success:
            st.success(msg)
        else:
            st.error(msg)
