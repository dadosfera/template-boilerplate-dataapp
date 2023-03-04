import streamlit as st
import components.input.date_and_time as dat
import components.input.number as number
import components.input.text as text
import components.input.file_uploader as fiUp
import components.input.download_button as download
import components.input.sliders as sliders


st.set_page_config(layout="wide")

st.header("Alguns modelos de inputs")

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
