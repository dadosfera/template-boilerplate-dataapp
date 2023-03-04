import streamlit as st
import plotly.express as px
import pandas as pd


st.cache_data(ttl=300)
def plot():
    df = pd.DataFrame(dict(
    r=[1, 5, 2, 2, 3],
    theta=['processing cost','mechanical properties','chemical stability',
           'thermal stability', 'device integration']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)