import streamlit as st
import plotly.express as px
import theme.colors as colors


# Cache data for 5 minutes to prevent unnecessary computations
st.cache_data(ttl=300)
def put(data_frame, card_title, description=''):
    with st.container():
        
        # Display card title and description
        st.subheader(card_title)
        st.markdown(description)
        
        # Create pie chart using Plotly Express
        fig = px.pie(data_frame, values='percentage', names='name', color='name',
                   hole=.7)
        st.plotly_chart(fig, use_container_width=True)
        
        # Display table with data frame
        st.markdown('### Table Title')
        st.table(data_frame)
