import streamlit as st
import pandas as pd
import plotly.express as px
import theme.colors as colors
import streamlit as st
import plotly.graph_objects as go
import pandas as pd


def put(param1, param2, param3, param4, param5, param6, param7):
    with st.container():

        df = pd.DataFrame({
            'Series 1': [param1, param2, param3, param4, param5, param6, param7],
            'Category':['param1', 'param2', 'param3', 'param4',
                   'param5', 'param6', 'param7']})
        
        categories = df['Category']
        values1 = df['Series 1']


    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
            r=values1,
            theta=categories,
            fill='toself',
            name='Série 1',
            marker_color=colors.BLUE
        ))



    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
