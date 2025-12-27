import streamlit as st
from app.data.db import connect_database
from app.data.incidents import get_all_incidents

st.set_page_config(page_title="Dashboard", layout="wide")

# ---- Guard ----
st.session_state.setdefault("logged_in", False)
st.session_state.setdefault("username", "")

if not st.session_state.logged_in:
    st.error("You must log in first.")
    if st.button("Go to login"):
        st.switch_page("Home.py")
    st.stop()

# ---- Page ----
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
    st.switch_page("Home.py")

