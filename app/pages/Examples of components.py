import streamlit as st
import components.sleeper as sleeper
from components import sidebar_brand

# Importing chart components
from components.examples.charts import radar, chart1, chart2, threeD, line, pie

# Importing input components
from components.examples.input import date_and_time, number, text, file_uploader, download_button, sliders

# Set page configuration and add brand sidebar
st.set_page_config(layout="wide")
sidebar_brand.put()

# Create tabs for charts and inputs
tab1, tab2 = st.tabs(["Charts", "Inputs"])

# First tab: charts
with tab1:
    st.header("Alguns modelos de gráficos") # Portuguese for "Some chart models"

    # Sleep for 5 seconds to simulate loading time
    sleeper.put(5)

    # Create three columns for displaying charts
    col1, col2, col3 = st.columns(3)

    with col1:
        chart1.plot()
        pie.plot()
        
    with col2:
        chart2.plot()
        line.plot()

    with col3:
        radar.plot()
        threeD.plot()

# Second tab: inputs
with tab2:
    st.header("Alguns modelos de inputs") # Portuguese for "Some input models"

    # Sleep for 10 seconds to simulate loading time
    sleeper.put(10)

    # Create three columns for displaying input components
    col1, col2, col3 = st.columns(3)

    with col1:
        text.put()
        file_uploader.put()
        
    with col2:
        number.put()
        download_button.put()

    with col3:
        date_and_time.put()
        sliders.put()
