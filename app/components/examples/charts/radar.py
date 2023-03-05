import streamlit as st  # Importing the Streamlit library for building web apps
import plotly.express as px  # Importing the Plotly Express library for data visualization
import pandas as pd  # Importing the Pandas library for data manipulation and analysis

# Caching the function output to improve performance by storing it in memory for a specified time
# To enable caching, we use the st.cache_data function and set the time-to-live (TTL) to 300 seconds (5 minutes)
st.cache_data(ttl=300)

# Defining a function for generating a polar line plot using Plotly Express
def plot():
    # Creating a Pandas DataFrame with sample data
    df = pd.DataFrame(dict(
        r=[1, 5, 2, 2, 3],
        theta=['processing cost','mechanical properties','chemical stability',
               'thermal stability', 'device integration']
    ))
    
    # Creating a polar line plot using Plotly Express
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    
    # Displaying the plot in the Streamlit app using the st.plotly_chart function
    # We also set the theme to "streamlit" and use_container_width to True for responsive sizing
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)