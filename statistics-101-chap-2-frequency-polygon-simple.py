import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set(style="whitegrid")
sns.set_context('talk', font_scale=0.8)

data = pd.read_csv("statistics-101-chap-2-data-food-intake.csv")

bins = st.slider('Bins', 5, 35, 5)

x = data["Water Intake"].values
x= x/1000

hist_values, bin_edges = np.histogram(x, bins=bins)

bin_centers = (0.5 * (bin_edges[:-1] + bin_edges[1:])).round(2)

plt.figure(figsize=(10, 6))
plt.plot(bin_centers, hist_values, marker='o', linestyle='-', color='#007acc')
plt.fill_between(bin_centers, hist_values, color='#007acc', alpha=0.85)

if bins > 15:
    plt.xticks(bin_centers, rotation=90, fontsize=12)
else:
    plt.xticks(bin_centers, fontsize=12)

plt.xlabel('Water Intake Bins Centers (Liters)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.title('Frequency of Daily Water Intake', fontsize=16)

plt.grid(axis='x', alpha=0.2, linestyle='--')
plt.grid(axis='y', alpha=0.5, linestyle='--')
plt.yticks(np.arange(0, max(hist_values)+1, step=1))

sns.despine()

st.pyplot(plt)
