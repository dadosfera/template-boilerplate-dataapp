import streamlit as st
import pandas as pd
import plotly.express as px
from models.Usage import Usage #importing custom module
import theme.colors as colors #importing custom module

st.cache_data(ttl=300) # caching function results for 300 seconds
def put(card_id, card_title):
    with st.container():
        # Creating a slider component with a range of 0-100, starting at 0
        percentage = st.slider(card_id, 0, 100, 0)

        # Creating an instance of the Usage class, passing chart title and percentage as arguments
        usage = Usage('chart-generic-title', percentage)
        df = pd.DataFrame(usage.get_data())

        # Splitting the card into two columns
        cardColumn1, cardColumn2 = st.columns(2)
        with cardColumn1:
            # Creating a pie chart with the data
            fig = px.pie(df, values='percentage', names='name', color='name',
                    color_discrete_map={'available': colors.BLUE,
                                        'used': colors.YELLOW},
                    title=usage.name, hole=.7)
            st.plotly_chart(fig, use_container_width=True)
            
        with cardColumn2:
            # Displaying the percentage value and the data in a DataFrame
            st.write('###', str(percentage), '%')
            st.dataframe(df, use_container_width=True)
