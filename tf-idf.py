import numpy as np
import pandas as pd
import streamlit as st

st.title('TF-IDF Tool')
if 'counter' not in st.session_state:
    st.session_state['counter'] = 0

dictionary = []

add_doc = st.button('Add document')
if add_doc:
    st.session_state['counter'] += 1
    st.write(st.session_state['counter'])
    dictionary.append(st.text_input('Document #' + str(st.session_state['counter'])))

st.markdown('-------------------')

st.markdown('__Raw Frequency (TF)__: $f_{ij}$')
st.markdown('__Inverse Frequency (IDF)__: $idf_{i} = \log_{2}(\dfrac{N}{n_{i}})$')
st.markdown('__TF-IDF__: $w_{ij} = tf_{ij} * idf_{i} = (1 + \log_{2}(f_{ij})) * \log_{2}(\dfrac{N}{n_{i}})$')
st.markdown('__Cosine Similarity__: $\sum{k} (d_{kj} * q_{ki})$')

st.markdown('-------------------')

st.markdown('__Log Normalization as Term Frequency__: $tf_{ij} = f_{ij}$')
st.markdown('__Inverse Frequency as IDF__: $idf_{i} = \log_{2}(\dfrac{N}{n_{i}})$')

st.markdown('-------------------')

st.markdown('__Inverse Frequency Smoothing as IDF__: $idf_{i} = log_{2}(1 + \dfrac{N}{n_{i}})$')

