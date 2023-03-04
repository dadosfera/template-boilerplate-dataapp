import streamlit as st
import plotly.express as px


st.cache_data(ttl=300)
def plot():
    df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
    df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
    fig = px.pie(df, values='pop', names='country', title='Population of European continent', hole=.7)
    st.plotly_chart(fig, use_container_width=True)