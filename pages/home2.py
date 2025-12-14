import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

# Ensure session state keys exist
st.session_state.setdefault("logged_in", False)
st.session_state.setdefault("username", "")

# Guard: if not logged in, prompt and stop
if not st.session_state["logged_in"]:
    st.error("You must be logged in to view the dashboard.")
    if st.button("Go to login page"):
        try:
            st.switch_page("Home")
        except Exception:
            st.experimental_rerun()
    st.stop()

# If logged in, show dashboard content
st.title("Dashboard")
st.success(f"Hello, {st.session_state['username']}! You are logged in.")
st.caption("📊")

# Example dashboard layout
st.caption("This is demo content — replace with your own dashboard.")

# Sidebar filters
with st.sidebar:
    st.header("Filters")
    n_points = st.slider("Number of data points", 10, 200, 50)

# Fake data
data = pd.DataFrame(
    np.random.randn(n_points, 3),
    columns=["A", "B", "C"]
)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Line chart")
    st.line_chart(data)
with col2:
    st.subheader("Bar chart")
    st.bar_chart(data)

with st.expander("See raw data"):
    st.dataframe(data)

# Logout button (sidebar keeps UI consistent)
st.markdown("---")
if st.sidebar.button("Log out"):
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""
    st.info("You have been logged out.")
    try:
        st.switch_page("Home")
    except Exception:
        st.experimental_rerun()