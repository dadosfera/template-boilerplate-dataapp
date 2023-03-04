import streamlit as st
import pandas as pd
import time
from models.Usage import Usage
from components import card_generic
from components import card_presentation
from components import sleeper

st.set_page_config(layout="wide")
# usage = [Use('available', 100-percentage), Use('used', percentage)]


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
