import streamlit as st
from app.services.user_services import login_user, register_user
from app.data.db import connect_database
from app.data.incidents import get_all_incidents

st.set_page_config(page_title="Cyber Incidents", layout="wide")

# ---- Session defaults ----
st.session_state.setdefault("logged_in", False)
st.session_state.setdefault("username", "")

# ---- DASHBOARD PAGE ----
if st.session_state.logged_in:
    st.title("📊 Cyber Incidents Dashboard")
    st.write(f"Welcome, **{st.session_state.username}**")

    # ---- Load data ----
    conn = connect_database()
    df = get_all_incidents(conn)
    conn.close()

    if df.empty:
        st.info("No incidents found.")
    else:
        st.dataframe(df, use_container_width=True)

    # ---- Logout ----
    st.divider()
    if st.button("Logout"):
        st.session_state.clear()
        st.rerun()

# ---- LOGIN PAGE ----
else:
    st.title("🔐 Login / Register")

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
                st.rerun()
            else:
                st.error(msg)

    # ---------- REGISTER ----------
    with tab_register:
        new_user = st.text_input("New username")
        new_pass = st.text_input("New password", type="password")

        if st.button("Register"):
            success, msg = register_user(new_user, new_pass)
            st.success(msg) if success else st.error(msg)

