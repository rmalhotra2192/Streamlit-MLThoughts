import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

sns.set(style="whitegrid")
sns.set_context('talk', font_scale=0.8)

lower_limit = st.slider('Water Intake (Y-axis Lower Limit)', 0, 2500, 0)
upper_limit = st.slider('Water Intake (Y-axis Upper Limit)', 5000, 10000, 5000)

data = pd.read_csv("statistics-101-chap-2-data-food-intake.csv")
data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')

data.sort_values('Date', inplace=True)

average_intake = data['Water Intake'].mean()

plt.figure(figsize=(10, 6))

plt.plot(data['Date'], data['Water Intake'], marker='o', linestyle='-', color='#ff5757', alpha=0.85, label='Water Intake', linewidth=2, markersize=4, markerfacecolor='#33658A', markeredgewidth=1.0, markeredgecolor='#33658A')

plt.axhline(y=average_intake, color='#6874E8', linestyle='--', label=f'Average: {average_intake:.2f} Liters')

locator = mdates.WeekdayLocator(byweekday=mdates.MO)
formatter = mdates.DateFormatter('%d-%b-%Y')

plt.gca().xaxis.set_major_locator(locator)
plt.gca().xaxis.set_major_formatter(formatter)

plt.xticks(rotation=45)

plt.xlabel('Date', fontsize=14)
plt.ylabel('Water Intake (Liters)', fontsize=14)
plt.ylim(bottom=lower_limit, top=upper_limit)
plt.title('Daily Water Intake Over Time', fontsize=16)

plt.legend(loc='lower left', bbox_to_anchor=(0.0, 0.0), fontsize=12)

plt.grid(axis='y', alpha=0.5, linestyle='--')

sns.despine()

st.pyplot(plt)
