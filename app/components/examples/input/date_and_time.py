import datetime
import streamlit as st

def put():
    """
    Displays a date and a time input widget, and outputs the selected date and time.

    Returns:
    None
    """
    d = st.date_input(
        "When's your birthday", 
        datetime.date(2019, 7, 6)
    )
    st.write('Your birthday is:', d)

    t = st.time_input('Set an alarm for', datetime.time(8, 45))
    st.write('Alarm is set for', t)
