import numpy as np
import pandas as pd
import streamlit as st

st.title('Counter Example')
if 'counter' not in st.session_state:
    st.session_state['counter'] = 0

increment = st.button('Increment')
if increment:
    st.session_state['counter'] += 1
    st.write(st.session_state['counter'])
