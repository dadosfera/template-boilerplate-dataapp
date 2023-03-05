import streamlit as st

# This function is used to display an image and a markdown text in the sidebar.
# It is cached for 300 seconds (5 minutes) to avoid reloading it unnecessarily.
@st.cache_data(ttl=300)
def put():
    st.sidebar.image("https://app.dadosfera.ai/en-US/assets/images/identity/dadosfera-login.svg", use_column_width=True)
    st.sidebar.markdown("**Data app** templates")
