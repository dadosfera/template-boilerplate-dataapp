import streamlit as st

def put():
    number = st.number_input('Insert a number')
    st.write('The current number is ', number)