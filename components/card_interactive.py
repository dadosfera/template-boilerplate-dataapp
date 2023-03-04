import streamlit as st
import pandas as pd
import plotly.express as px
from models.Usage import Usage
import theme.colors as colors

def put(card_id, card_title):
    with st.container():
        percentage = st.slider(card_id, 0, 100, 0) #slider component with 0-100 range satarting in 0

        usage = Usage('chart-generic-title', percentage)
        df = pd.DataFrame(usage.get_data())

        

        cardColumn1, cardColumn2 = st.columns(2)
        with cardColumn1:
            fig = px.pie(df, values='percentage', names='name', color='name',
                    color_discrete_map={'available': colors.BLUE,
                                        'used': colors.YELLOW},
                    title=usage.name, hole=.7)
            st.plotly_chart(fig, use_container_width=True)
            
        with cardColumn2:
            st.write('###', str(percentage), '%')
            st.dataframe(df)
