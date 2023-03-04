import streamlit as st
import components.sleeper as sleeper
import components.examples.input.date_and_time as dat
import components.examples.input.number as number
import components.examples.input.text as text
import components.examples.input.file_uploader as fiUp
import components.examples.input.download_button as download
import components.examples.input.sliders as sliders


st.set_page_config(layout="wide")

st.header("Alguns modelos de inputs")

sleeper.put(10)

col1, col2, col3 = st.columns(3)

with col1:
    text.put()
    fiUp.put()
    
with col2:
    number.put()
    download.put()

with col3:
    dat.put()
    sliders.put()
