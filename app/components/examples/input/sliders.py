import streamlit as st
from datetime import datetime

def put():
    # Create a slider for age selection
    age = st.slider('How old are you?', 0, 130, 25)
    st.write("I'm ", age, 'years old')

    # Create a slider for selecting a range of values
    values = st.slider(
        'Select a range of values',
        0.0, 100.0, (25.0, 75.0))
    st.write('Values:', values)

    # Create a slider for selecting a start time
    start_time = st.slider(
        "When do you start?",
        value=datetime(2020, 1, 1, 9, 30),
        format="MM/DD/YY - hh:mm")
    st.write("Start time:", start_time)
