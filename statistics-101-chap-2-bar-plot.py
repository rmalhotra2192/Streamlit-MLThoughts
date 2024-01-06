import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
sns.set_context('talk', font_scale=0.8)

data = pd.read_csv("statistics-101-chap-2-data-fitness.csv")

exercise_data = data[data['Exercise Category'] != 'NA']

exercise_counts = exercise_data['Exercise Category'].value_counts()

plt.figure(figsize=(10, 6))
bars = plt.bar(exercise_counts.index, exercise_counts.values, color='#ff5757', alpha=0.85)

plt.xlabel('Exercise Category', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.title('Frequency of Exercise Categories', fontsize=16)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom', ha='center', fontsize=10)

plt.grid(axis='y', alpha=0.5, linestyle='--')

sns.despine()

st.pyplot(plt)