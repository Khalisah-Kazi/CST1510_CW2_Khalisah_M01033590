import streamlit as st
from app.data.db import connect_database
from app.data.incidents import get_all_incidents

st.set_page_config(page_title="Dashboard", layout="wide")

# Ensure session state keys exist
st.session_state.setdefault("logged_in", False)
st.session_state.setdefault("username", "")

# ---------- AUTH GUARD ----------
if not st.session_state.get("logged_in", False):
    st.error("You must log in first.")
    if st.button("Go to login page"):
        try:
            st.switch_page("Home")
        except Exception:
            st.experimental_rerun()
    st.stop()

st.title("📊 Cyber Incidents Dashboard")
st.write(f"Welcome, **{st.session_state.get('username', '')}**")

# ---------- LOAD DATA ----------
try:
    conn = connect_database()
    df = get_all_incidents(conn)
    conn.close()
except Exception as e:
    st.error(f"Error loading incidents: {e}")
    st.stop()

if df is None or getattr(df, "empty", True):
    st.info("No incidents found.")
else:
    st.dataframe(df, use_container_width=True)

# ---------- LOGOUT ----------
if st.button("Logout"):
    # Clear session and return to login/home
    st.session_state.clear()
    try:
        st.switch_page("Home")
    except Exception:
        st.experimental_rerun()
