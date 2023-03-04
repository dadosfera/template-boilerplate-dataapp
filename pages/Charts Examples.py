import streamlit as st
import components.sleeper as sleeper
import components.examples.charts.radar as radar
import components.examples.charts.chart1 as chart1
import components.examples.charts.chart2 as chart2
import components.examples.charts.threeD as threeD
import components.examples.charts.line as line
import components.examples.charts.pie as pie

st.set_page_config(layout="wide")

st.header("Alguns modelos de gráficos")

col1, col2, col3 = st.columns(3)

sleeper.put(5)

with col1:
    chart1.plot()
    pie.plot()
    
with col2:
    chart2.plot()
    line.plot()

with col3:
    radar.plot()
    threeD.plot()
