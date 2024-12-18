import streamlit as st
import pandas as pd
import numpy as np

st.write("# My Cool Chart")

chart_Data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.bar_chart(chart_Data)
st.line_chart(chart_Data)

