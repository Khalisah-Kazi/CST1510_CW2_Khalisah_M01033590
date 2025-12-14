imimport streamlit as st
from app.data.db import connect_database
from app.data.incidents import get_all_incidents

st.set_page_config(page_title="Dashboard", layout="wide")

# ---------- AUTH GUARD ----------
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must log in first.")
    st.stop()

st.title("📊 Cyber Incidents Dashboard")
st.write(f"Welcome, **{st.session_state.username}**")

# ---------- LOAD DATA ----------
conn = connect_database()
df = get_all_incidents(conn)
conn.close()

if df.empty:
    st.info("No incidents found.")
else:
    st.dataframe(df, use_container_width=True)

# ---------- LOGOUT ----------
if st.button("Logout"):
    st.session_state.clear()
    st.switch_page("pages/home2.py")
