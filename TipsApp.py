import streamlit as st
import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from datetime import datetime, timedelta

tips = pd.read_csv('/home/konstantin/ds_bootcamp/ds-phase-0/learning/datasets/tips.csv')
df = tips.copy()

def generate_random_dates(start_date, end_date, n):
    delta_days = (end_date - start_date).days
    dates = np.array([start_date + timedelta(days=i) for i in range(delta_days)])
    return dates[np.random.randint(low=0, high=delta_days, size=n)]


dates = generate_random_dates(datetime(2023, 1, 1), datetime(2023, 2, 1), len(tips.index.values))
tips["time_order"] = dates


st.write("""
# Графики различных зависимостей из файла 'tips.csv' """)
st.write("""
### Первый график """)
fig1, ax1 = plt.subplots(figsize=(17, 8))
ax1 = sns.scatterplot(x = 'time_order', y = 'tip', data = tips)
plt.xlabel("01.01.23 - 01.02.23")
plt.ylabel("Чаевые /  $")
plt.grid(1)
plt.title("Динамика чаевых за месяц")
st.pyplot(fig1)

st.write("""
Второй график""")
tips1 = tips.groupby("time_order").sum()
fig2, ax2 = plt.subplots()
ax2 = sns.barplot(
    y='time_order', 
    x='total_bill',
    data=tips1.sort_values("time_order", ascending = True))
fig2 = ax2.get_figure()
fig2.set_size_inches(20, 10)
ax2 = plt.xlabel("Заработанная за день сумма"); plt.ylabel("Дата"); plt.title("Сумма всех заказов по дням за январь 2023 года")
st.pyplot(fig2)

st.write("""
### Третий график""")
fig3, ax3 = plt.subplots()
ax3 = sns.scatterplot(data=tips, x="tip", y="day", hue="sex")
ax3 = plt.title("Чаевые по дням недели в зависимости от пола")
ax3 = plt.xlabel("Чаевые")
ax3 = plt.ylabel("День недели")
st.pyplot(fig3)

st.write("""
### Последний из более менее удачных""")
#fig4, ax4 = plt.subplots()
fig = sns.jointplot(data = tips, x = "total_bill", y ="tip", hue ="size")
plt.title("Отношение суммы чаевых к сумме заказа, а так же плотность распредления по количесту посетителей за заказ\n\n\n\n\n")
plt.xlabel("Сумма заказа")
plt.ylabel("Чаевые")
st.pyplot(fig)
