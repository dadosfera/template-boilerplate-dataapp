import streamlit as st
import components.sleeper as sleeper
from components import sidebar_brand

# charts
from components.examples.charts import radar, chart1,chart2, threeD, line, pie
# inputs
from components.examples.input import date_and_time, number, text, file_uploader, download_button, sliders

st.set_page_config(layout="wide")
sidebar_brand.put()

tab1, tab2 = st.tabs(["Charts", "Inputs"])

with tab1:
    st.header("Alguns modelos de gráficos")

    sleeper.put(5)

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

with tab2:
    st.header("Alguns modelos de inputs")

    sleeper.put(10)

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

