import streamlit as st
import pandas as pd
import numpy as np

def plot():
    # Create a pandas DataFrame with 20 rows and 3 columns of random data
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["a", "b", "c"])

    # Create a bar chart using the chart_data DataFrame
    st.bar_chart(chart_data)
