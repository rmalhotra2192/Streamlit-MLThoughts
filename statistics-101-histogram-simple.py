import streamlit as st
import numpy as np

num_elements = st.slider('Total Number of Elements in the Histogram', 1000, 20000, 1000)
bins = st.slider('Bins', 0, 100, 20)
x = np.random.randn(num_elements)
hist = np.histogram(x, bins=bins)[0]
st.bar_chart(hist)