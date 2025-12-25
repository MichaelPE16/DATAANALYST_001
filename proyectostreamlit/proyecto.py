# examine the required libraries
from re import X
from tarfile import data_filter
from turtle import color
from plotly.graph_objs.surface.contours import x
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

data = pd.read_csv(r'D:\Last\1.DATAENGINEER\PYSPTS\csv\StudentsPerformance.csv')

# print(data.head())
data['promedio'] = data[['math score', 'reading score', 'writing score']].mean(axis=1).round(2)
# print(data['promedio'].head())
def selectLevel(promedio):
    if promedio >= 90: 
        return 'A'
    elif promedio >= 80: 
        return 'B'
    elif promedio >= 70: 
        return 'C'
    elif promedio >= 60: 
        return 'D'
    else: 
        return 'F'
data['level'] = data['promedio'].apply(selectLevel)  
# print(data['level'].head())
pct_levels = data['level'].value_counts(normalize=True) * 100
# print(pct_levels)

#setting up the app on streamlit
st.set_page_config(page_title='Students Score', layout='wide')
st.title('Students Performance Dashboard')
with st.sidebar:
    gender = st.selectbox('Select-Gender', options=['All', 'male', 'female'], index=0)
    st.markdown('[Data-Link](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)')
#filtering the data
filtered_data = data if gender == 'All' else data[data['gender'] == gender]

#creating the columns
col1, col2, col3 = st.columns(3)
col1.metric(label='Math Score Mean', value=filtered_data['math score'].mean().round(2))
col2.metric(label='Writing Score Mean', value=filtered_data['writing score'].mean().round(2))
col3.metric(label='Reading Score Mean', value=filtered_data['reading score'].mean().round(2))
# print(data['gender'].value_counts())

#Bar grafic

st.subheader('Parents Education Level')
mean_level = filtered_data.groupby('parental level of education')['promedio'].mean().reset_index()
st.bar_chart(mean_level, x='parental level of education', y='promedio')
col_r, col_l = st.columns(2)
#correlation matrix
with col_r:
    st.subheader('Subjects Correlation Chart')
    colr = scatter_matrix(filtered_data[['math score', 'reading score', 'writing score']],
    diagonal= 'hits', 
    color='teal')
st.pyplot(plt.gcf()) # this will add the correlation matrix to the streamlit app

with col_l:
    st.subheader('Level % Distribution')
    levels = filtered_data['level'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(levels, labels=levels.index, autopct='%1.1f%%')
    st.pyplot(fig)