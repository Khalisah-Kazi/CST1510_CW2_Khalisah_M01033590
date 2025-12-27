import streamlit as st
from app.services.user_services import login_user, register_user

st.set_page_config(page_title="Login", layout="centered")

# ---- Session defaults ----
st.session_state.setdefault("logged_in", False)
st.session_state.setdefault("username", "")

st.title("🔐 Login / Register")

# Already logged in → dashboard
if st.session_state.logged_in:
    st.success(f"Logged in as {st.session_state.username}")
    if st.button("Go to dashboard"):
        st.switch_page("pages/1_Dashboard.py")
    st.stop()

tab_login, tab_register = st.tabs(["Login", "Register"])

# ---------- LOGIN ----------
with tab_login:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login", type="primary"):
        success, msg = login_user(username, password)
        if success:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(msg)
            st.switch_page("pages/1_Dashboard.py")
        else:
            st.error(msg)

# ---------- REGISTER ----------
with tab_register:
    new_user = st.text_input("New username")
    new_pass = st.text_input("New password", type="password")

    if st.button("Register"):
        success, msg = register_user(new_user, new_pass)
        st.success(msg) if success else st.error(msg)

