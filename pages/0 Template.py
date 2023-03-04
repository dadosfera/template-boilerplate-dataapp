import streamlit as st
import plotly.express as px
from datetime import datetime

percentage = st.slider('Percentage', 0, 100, 0)
st.write(percentage, '% completed.')

df = {'percentage': [percentage, 100-percentage],
      'names': ['ocupado', 'disponivel']}

# df = px.data.tips()
print(df)
# Represent only large countries
fig = px.pie(df, values='percentage', names='names', color='names',
             color_discrete_map={'disponivel': 'green',
                                 'ocupado': 'red'},
             title='Population of European continent', hole=.7)
st.plotly_chart(fig, use_container_width=True)
