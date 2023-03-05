import streamlit as st
import pandas as pd
import numpy as np

def plot():
    # Create random DataFrame
    df = pd.DataFrame(
        np.random.randn(10, 5),
        columns=('col %d' % i for i in range(5)))

    # Display DataFrame as a table
    st.table(df)
