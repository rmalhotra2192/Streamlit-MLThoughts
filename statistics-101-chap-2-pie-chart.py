import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
sns.set_context('talk', font_scale=0.8)

data = pd.read_csv("statistics-101-chap-2-data-fitness.csv")

exercise_counts = data['Exercise'].value_counts()

colors = ['#ff5757','#33658A']

plt.figure(figsize=(8, 6))
patches, texts, autotexts = plt.pie(exercise_counts, autopct='%1.1f%%', startangle=140, colors=colors, pctdistance=0.85)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_size('x-large')


centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  

plt.title('Exercise Distribution', fontsize=16)

plt.legend(patches, exercise_counts.index, loc='best')

st.pyplot(plt)