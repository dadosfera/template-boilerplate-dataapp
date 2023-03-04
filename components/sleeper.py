import streamlit as st
import time

def put(sec):
    time_element = st.empty()
    for seconds in range(sec):
        time_element.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    time_element.write(f"✔️ {sec}  seconds over!")
    time.sleep(1)
    time_element.empty()