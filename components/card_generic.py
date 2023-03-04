import streamlit as st
import plotly.express as px
import theme.colors as colors


st.cache_data(ttl=300)
def put(data_frame, card_title, description=''):
    with st.container():
        

            st.subheader(card_title)
            st.markdown(description)
            fig = px.pie(data_frame, values='percentage', names='name', color='name',
                    # color_discrete_map={'available': colors.BLUE,
                    #                     'used': colors.YELLOW},
                   hole=.7)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('### Table Title')
            st.table(data_frame)

