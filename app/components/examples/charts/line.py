import streamlit as st  # Importing the Streamlit library
import plotly.express as px  # Importing the Plotly Express library

# The following function defines a cached function to display a Plotly Line chart of the life expectancy of Oceania countries over the years
# The data is first filtered to include only countries in Oceania
# A line chart is then created using Plotly and displayed using the Streamlit function st.plotly_chart()
st.cache_data(ttl=300)
def plot():
    df = px.data.gapminder().query("continent=='Oceania'")
    fig = px.line(df, x="year", y="lifeExp", color='country')
    st.plotly_chart(fig, use_container_width=True)
