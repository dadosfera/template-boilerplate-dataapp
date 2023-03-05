import streamlit as st

def put():
    """
    Renders a container with a header, subheader, and text for a presentation.
    """
    with st.container():
        st.header('Presentation Title')
        st.subheader('Presentation subtitle')
        st.text('Presentation resume')
