import streamlit as st

st.cache_data(ttl=300)
def put():
    st.sidebar.image("https://app.dadosfera.ai/en-US/assets/images/identity/dadosfera-login.svg", use_column_width=True)
    st.sidebar.markdown("**Data app** templates")