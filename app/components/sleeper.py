import streamlit as st
import time

def put(sec):
    """
    A function that displays a timer in Streamlit for a specified number of seconds.

    Parameters:
        sec (int): The number of seconds to display the timer for.

    Returns:
        None
    """
    # Create a Streamlit element to display the timer
    time_element = st.empty()

    # Loop through the specified number of seconds and update the timer element each second
    for seconds in range(sec):
        time_element.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)

    # Display a message indicating that the timer is over
    time_element.write(f"✔️ {sec} seconds over!")
    time.sleep(1)

    # Clear the timer element
    time_element.empty()
