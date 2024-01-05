import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set(style="whitegrid")
sns.set_context('talk', font_scale=0.8)

data = pd.read_csv("./data/Water Intake.csv")

bins = st.slider('Bins', 5, 35, 5)

x = data["Water Intake"].values
hist_values, bin_edges = np.histogram(x, bins=bins)

bin_labels = [f"{round(bin_edges[i]/1000, 1)} ltrs - {round(bin_edges[i+1]/1000, 1)} ltrs" for i in range(len(bin_edges)-1)]

plt.figure(figsize=(10, 6))
bars = plt.bar(bin_labels, hist_values, color='#007acc', alpha=0.85)
plt.xticks(rotation=90, fontsize=12)
plt.xlabel('Water Intake (Liters)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.title('Frequency of Daily Water Intake', fontsize=16)

plt.grid(axis='x', alpha=0.2, linestyle='--')
plt.grid(axis='y', alpha=0.5, linestyle='--')

sns.despine()

st.pyplot(plt)
