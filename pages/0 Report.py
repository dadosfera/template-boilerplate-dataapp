import streamlit as st
from components import card_interactive, chart_radar_interactive, sidebar_brand, chart_bars, info_markdown, table

st.set_page_config(layout="wide")
sidebar_brand.put()

tab1, tab2 = st.tabs(["Resume", "Continue"])

with tab1:
    col1, col2 = st.columns(2, gap='large')
    with col2:
        card_interactive.put('card-input-id', 'card-chart-title')
        col3, col4 = st.columns(2)
        with col3:
            param1 = st.number_input('Param1', min_value=0, max_value=7)
            param2 = st.number_input('Param2', min_value=0, max_value=7)
            param3 = st.number_input('Param3', min_value=0, max_value=7)
            param4 = st.number_input('Param4', min_value=0, max_value=7)
        with col4:
            param5 = st.number_input('Param5', min_value=0, max_value=7)
            param6 = st.number_input('Param6', min_value=0, max_value=7)
            param7 = st.number_input('Param7', min_value=0, max_value=7)

    with col1:
        st.title("Title")
        st.header("Header")
        st.subheader("Subheader")
        st.markdown('in eu mi bibendum neque egestas congue quisque egestas diam in arcu cursus euismod quis viverra nibh cras pulvinar mattis nunc sed blandit libero volutpat sed cras ornare arcu dui vivamus arcu felis bibendum ut tristique et egestas quis ipsum suspendisse ultrices gravida dictum fusce ut placerat orci nulla pellentesque dignissim enim sit amet venenatis urna cursus eget nunc scelerisque viverra mauris in aliquam sem fringilla ut morbi tincidunt augue interdum velit euismod in pellentesque massa placerat duis ultricies lacus sed turpis tincidunt id aliquet risus feugiat in ante metus dictum at tempor commodo ullamcorper a lacus vestibulum sed arcu non odio euismod lacinia at quis risus sed vulputate odio ut enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit scelerisque in dictum non consectetur a erat nam at lectus urna duis convallis convallis tellus id interdum velit laoreet id donec ultrices tincidunt arcu non sodales neque sodales ut etiam sit amet nisl purus in mollis nunc sed id semper risus in hendrerit gravida rutrum quisque non tellus orci ac auctor augue mauris augue neque gravida in fermentum et sollicitudin ac orci phasellus egestas tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum odio eu feugiat')
        chart_radar_interactive.put(
            param1, param2, param3, param4, param5, param6, param7)

with tab2:
    col1, col2 = st.columns(2, gap='large')
    with col1:
        chart_bars.plot()
        info_markdown.put()
    with col2:
        info_markdown.put()
        table.plot()
