import streamlit as st

def put():
    """
    Displays a numeric input field in the Streamlit app, and displays the current number entered by the user.
    """
    # Define the numeric input field
    number = st.number_input('Insert a number')
    
    # Display the current number entered by the user
    st.write('The current number is ', number)
