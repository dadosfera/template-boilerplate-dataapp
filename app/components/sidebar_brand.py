import streamlit as st
import components.print_page_button as print_button
# This function is used to display an image and a markdown text in the sidebar.
# It is cached for 300 seconds (5 minutes) to avoid reloading it unnecessarily.
def put():
    st.sidebar.image("https://app.dadosfera.ai/en-US/assets/images/identity/dadosfera-login.svg", use_column_width=True)
    st.sidebar.markdown("**Data app** templates")
    print_button.put()
