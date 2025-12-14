import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("3. Charts Demo")
st.header("Line, area, and bar charts")

# Fake time series data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.subheader("Line chart")
st.line_chart(data)

st.subheader("Area chart")
st.area_chart(data)

st.subheader("Bar chart")
st.bar_chart(data)

st.divider()
st.header("Scatter chart & map")

# Scatter chart (use Altair for control)
scatter_data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=["x", "y", "size"]
)
st.subheader("Scatter chart (Altair)")
scatter_chart = (
    alt.Chart(scatter_data)
    .mark_circle(opacity=0.6)
    .encode(
        x="x",
        y="y",
        size=alt.Size("size", legend=None),
        tooltip=["x", "y", "size"],
        color=alt.value("#1f77b4"),
    )
    .interactive()
)
st.altair_chart(scatter_chart, use_container_width=True)

# Map (requires lat/lon columns)
st.subheader("Map")
map_data = pd.DataFrame({
    "lat": 51.5 + np.random.randn(100) * 0.01,
    "lon": -0.12 + np.random.randn(100) * 0.01,
})
st.map(map_data)

st.divider()
st.header("Altair example (line)")

chart = (
    alt.Chart(data.reset_index().rename(columns={"index": "t"}))
    .mark_line()
    .encode(
        x="t:Q",
        y="A:Q",
        tooltip=["t", "A"]
    )
)
st.altair_chart(chart, use_container_width=True)