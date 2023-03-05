import streamlit as st
import plotly.express as px

# Cache the data to reduce loading time
st.cache_data(ttl=300)
def plot():
    # Load Gapminder dataset
    df = px.data.gapminder()

    # Create scatter plot with size of bubbles proportional to population and colored by continent
    fig = px.scatter(
        df.query("year==2007"), # Filter the dataset for year 2007
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        hover_name="country",
        log_x=True,
        size_max=60,
    )

    # Create two tabs for different themes
    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    
    # Use the Streamlit theme in the first tab
    with tab1:
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    
    # Use the native Plotly theme in the second tab
    with tab2:
        st.plotly_chart(fig, theme=None, use_container_width=True)
