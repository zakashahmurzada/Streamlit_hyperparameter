import time
import streamlit as st
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

st.title('Train Model on Iris Data')

if 'data' in st.session_state:
    df = st.session_state['data']

    x = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    st.session_state['x'] = x
    st.session_state['y'] = y

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    st.session_state['x_test'] = x_test
    st.session_state['y_test'] = y_test
    st.session_state['x_train'] = x_train
    st.session_state['y_train'] = y_train

    option = st.selectbox(
        'Select your favorite model:',
        ('--', 'SVC', 'KNN', 'Decision Tree'))

    if option == 'SVC':
        if st.button('Train Now!'):
            progress_text = "Model training in progress ..."
            my_bar = st.sidebar.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            my_bar.empty()
            best_kernel = st.session_state['best_kernel']
            best_value = st.session_state['best_value']
            model = SVC(C=best_value, kernel=best_kernel)
            model.fit(x_train, y_train)
            st.session_state['model'] = model
            st.success('SVC is trained successfully')

    elif option == 'KNN':
        if st.button('Train Now!'):
            model = KNeighborsClassifier(n_neighbors=3)
            model.fit(x_train, y_train)
            st.session_state['model'] = model
            st.success('KNN is trained successfully')

    elif option == 'Decision Tree':
        if st.button('Train Now!'):
            model = DecisionTreeClassifier()
            model.fit(x_train, y_train)
            st.session_state['model'] = model
            st.success('Decision Tree is trained successfully')

    st.session_state['option'] = option
else:
    st.error('You need to upload the data before training the model!')
