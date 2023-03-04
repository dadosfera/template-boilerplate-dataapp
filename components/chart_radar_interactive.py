import streamlit as st
import pandas as pd
import theme.colors as colors
import streamlit as st
import plotly.graph_objects as go
import pandas as pd


def put(param1, param2, param3, param4, param5, param6, param7):
    # create a container to hold the visualizations
    with st.container():
        # create a DataFrame with the data to be plotted
        df = pd.DataFrame({
            'Series 1': [param1, param2, param3, param4, param5, param6, param7],
            'Category':['param1', 'param2', 'param3', 'param4',
                   'param5', 'param6', 'param7']})
        
        # get the categories and values from the DataFrame
        categories = df['Category']
        values1 = df['Series 1']

    # create a polar plot using Plotly
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
            r=values1,
            theta=categories,
            fill='toself',
            name='Série 1',
            marker_color=colors.BLUE
        ))

    # display the plot using Streamlit's plotly_chart method
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
