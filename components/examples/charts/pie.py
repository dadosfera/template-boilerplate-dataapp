import streamlit as st        # Importing the Streamlit library
import plotly.express as px   # Importing the Plotly Express module

st.cache_data(ttl=300)        # Caching the data for 300 seconds to speed up the app performance

def plot():                  # Defining a function called plot
    df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")    # Selecting data from the gapminder dataset for the year 2007 and European countries
    df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries'      # Grouping small countries under a single category
    fig = px.pie(df, values='pop', names='country', title='Population of European continent', hole=.7)   # Creating a pie chart with population as values, country as names, title as "Population of European continent" and a hole in the middle of 0.7 radius
    st.plotly_chart(fig, use_container_width=True)   # Plotting the chart using Plotly in Streamlit with container width set to True
