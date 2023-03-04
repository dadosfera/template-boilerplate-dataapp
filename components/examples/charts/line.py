import streamlit as st
import plotly.express as px

def plot():
    df = px.data.gapminder().query("continent=='Oceania'")
    fig = px.line(df, x="year", y="lifeExp", color='country')
    st.plotly_chart(fig, use_container_width=True)