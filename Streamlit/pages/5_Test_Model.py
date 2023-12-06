import streamlit as st
import numpy as np
from sklearn.metrics import accuracy_score

st.title('Test Accuracy of Model')

if 'model' in st.session_state:

    model = st.session_state['model']
    x_test = st.session_state['x_test']
    y_test = st.session_state['y_test']

    option = st.selectbox(
        'How do you want to test?',
        ('--', 'Test Data', 'Custom Values'))

    if option == 'Test Data':

        y_pred = model.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)

        st.info('The accuracy of our model is ' + str(accuracy))

    elif option == 'Custom Values':

        SepalLengthCm = st.text_input('Sepal Length (Cm)', "-1")
        SepalLengthCm = float(SepalLengthCm)
        SepalWidthCm = st.text_input('Sepal Width (Cm)', "-1")
        SepalWidthCm = float(SepalWidthCm)
        PetalLengthCm = st.text_input('Petal Length (Cm)', "-1")
        PetalLengthCm = float(PetalLengthCm)
        PetalWidthCm = st.text_input('Petal Width (Cm)', "-1")
        PetalWidthCm = float(PetalWidthCm)

        test = np.array([SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]).reshape(1, -1)

        score = model.predict(test)[0]

        result = ''

        if score == 0:
            result = 'Iris-setosa'
        elif score == 1:
            result = 'Iris-versicolor'
        elif score == 2:
            result = 'Iris-virginica'
        if -1 not in test:
            st.info('The predicted flower is ' + result)


else:
    st.error('The model is not trained yet!')