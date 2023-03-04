# Import the streamlit library
import streamlit as st

# Cache the results of the function for 300 seconds
st.cache_data(ttl=300)

# Define a function called "put"
def put():
    # Create a container for the streamlit app
    with st.container():
        # Display an image from the specified URL and fit it to the column width
        st.image("https://app.dadosfera.ai/en-US/assets/images/identity/dadosfera-login.svg", use_column_width=True)
        # Display the specified text as Markdown
        st.markdown("**Data app** templates")