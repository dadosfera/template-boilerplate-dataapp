import streamlit as st
import pandas as pd
from models.Usage import Usage
from components import card_generic, card_presentation, sidebar_brand, sleeper


st.set_page_config(layout="wide")
sidebar_brand.put()


usages = [
    Usage('CPU', 10, description='orem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut.'),
    Usage('Memory', 20, description='orem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut.'),
    Usage('Network', 30, description='orem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut.'),
    Usage('CPU2', 40, description='orem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut.'),
    Usage('Memory2', 50, description='orem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut.'),
    Usage('Network2', 50,
          description='orem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut.')
]

card_presentation.put()
sleeper.put(3)

columns = st.columns(spec=3, gap='medium')

for usage in usages:
    df = pd.DataFrame(usage.data)

    with columns[(usages.index(usage) + 1) % 3]:
        card_generic.put(df, usage.name, description=usage.description)
