import streamlit as st 
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import mean

st.title('Exploratry Data Analysis')

if 'data' in st.session_state:
    df = st.session_state['data']
    option = st.selectbox(
        'Select your favorite visualization:',
        ('--', 'Scatter Plot', 'Histogram', 'Heatmap'))
    if option == 'Scatter Plot':
        fig, ax = plt.subplots()
        sns.scatterplot(x=df['6'], y=df['0'], hue=df['1'])
        st.pyplot(fig)

    elif option == 'Histogram':
        fig, ax = plt.subplots()
        sns.histplot(x=df['6'], y=df['0'], hue=df['1'])
        st.pyplot(fig)

    elif option == 'Heatmap':
        fig, ax = plt.subplots()
        sns.heatmap(data=df.corr())
        st.pyplot(fig)
