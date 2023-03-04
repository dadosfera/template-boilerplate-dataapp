import streamlit as st
from components import card_interactive, chart_radar_interactive, sidebar_brand, chart_bars, info_markdown, table

# Set page configuration
st.set_page_config(layout="wide")

# Display the sidebar brand component
sidebar_brand.put()

# Define two tabs with titles "Resume" and "Continue"
tab1, tab2 = st.tabs(["Resume", "Continue"])

# Define the content of the first tab
with tab1:
    # Define a two-column layout for the tab
    col1, col2 = st.columns(2, gap='large')

    # Define the content of the right column
    with col2: 
        # Display an interactive card with an input field and a title
        card_interactive.put('card-input-id', 'card-chart-title')
        # Define a two-column layout for the card
        col3, col4 = st.columns(2)
        # Define the content of the left column of the card
        with col3:
            # Display a number input field labeled "Param1" with minimum and maximum values of 0 and 7
            param1 = st.number_input('Param1', min_value=0, max_value=7)
            # Display a number input field labeled "Param2" with minimum and maximum values of 0 and 7
            param2 = st.number_input('Param2', min_value=0, max_value=7)
            # Display a number input field labeled "Param3" with minimum and maximum values of 0 and 7
            param3 = st.number_input('Param3', min_value=0, max_value=7)
            # Display a number input field labeled "Param4" with minimum and maximum values of 0 and 7
            param4 = st.number_input('Param4', min_value=0, max_value=7)
        # Define the content of the right column of the card
        with col4:
            # Display a number input field labeled "Param5" with minimum and maximum values of 0 and 7
            param5 = st.number_input('Param5', min_value=0, max_value=7)
            # Display a number input field labeled "Param6" with minimum and maximum values of 0 and 7
            param6 = st.number_input('Param6', min_value=0, max_value=7)
            # Display a number input field labeled "Param7" with minimum and maximum values of 0 and 7
            param7 = st.number_input('Param7', min_value=0, max_value=7)

    # Define the content of the left column of the tab
    with col1:
        # Display a title labeled "Title"
        st.title("Title")
        # Display a header labeled "Header"
        st.header("Header")
        # Display an info markdown component
        info_markdown.put()
        # Display a radar chart with the parameters defined in the card component
        chart_radar_interactive.put(
            param1, param2, param3, param4, param5, param6, param7)

# Define the content of the second tab
with tab2:
    # Define a two-column layout for the tab
    col1, col2 = st.columns(2, gap='large')

    # Define the content of the left column of the tab
    with col1:
        # Display a bar chart
        chart_bars.plot()
        # Display an info markdown component
        info_markdown.put()

    # Define the content of the right column of the tab
    with col2:
        # Display an info markdown component
        info_markdown.put()
        table.plot()
