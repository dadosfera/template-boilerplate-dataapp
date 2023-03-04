import streamlit as st
import pandas as pd
from models.Usage import Usage
from components import card_generic, card_presentation, sidebar_brand, sleeper

# Set up the Streamlit page layout and add the branding sidebar
st.set_page_config(layout="wide")
sidebar_brand.put()

# Define a list of Usage objects, each containing data for a different type of usage
usages = [
    Usage('CPU', 10, description='orem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut.'),
    Usage('Memory', 20, description='orem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut.'),
    Usage('Network', 30, description='orem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut.'),
    Usage('CPU2', 40, description='orem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut.'),
    Usage('Memory2', 50, description='orem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut.'),
    Usage('Network2', 50, description='orem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut.')
]

# Add a presentation card to the page
card_presentation.put()

# Add a 3-second delay to the page using the sleeper component
sleeper.put(3)

# Create a set of columns for displaying the usage data
columns = st.columns(spec=3, gap='medium')

# Loop through the usage data and add a card for each one to a different column
for usage in usages:
    df = pd.DataFrame(usage.data)

    # Add the card to a column based on the index of the usage in the list
    with columns[(usages.index(usage) + 1) % 3]:
        card_generic.put(df, usage.name, description=usage.description)
