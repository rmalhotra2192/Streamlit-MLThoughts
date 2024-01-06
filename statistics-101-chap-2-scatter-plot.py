import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set(style="whitegrid")
sns.set_context('talk', font_scale=0.8)

data = pd.read_csv("statistics-101-chap-2-data-fitness.csv")

plt.figure(figsize=(10, 6))
plt.scatter(data['Calorie Intake'], data['Water Intake'], color='#ff5757', alpha=0.85, label='Water Intake', s=50, edgecolor='#33658A', linewidth=1.0)

plt.xlabel('Calorie Intake', fontsize=14)
plt.ylabel('Water Intake (Liters)', fontsize=14)

plt.ylim(bottom=0, top=5000)

plt.title('Water Intake vs. Calorie Intake', fontsize=16)

plt.grid(axis='y', alpha=0.5, linestyle='--')

sns.despine()

st.pyplot(plt)