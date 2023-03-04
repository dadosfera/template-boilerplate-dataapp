import streamlit as st
import plotly.express as px


# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )


percentage = st.slider('Percentage', 0, 100, 0)
st.write(percentage, '% completed.')

df = {'percentage': [percentage, 100-percentage],
      'names': ['ocupado', 'disponivel']}

st.dataframe(df)
st.table(df)

fig = px.pie(df, values='percentage', names='names', color='names',
             color_discrete_map={'disponivel': 'green',
                                 'ocupado': 'red'},
             title='Population of European continent', hole=.7)
st.plotly_chart(fig, use_container_width=True)
