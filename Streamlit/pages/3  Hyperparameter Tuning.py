import streamlit as st
import pandas as pd
from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV

df = st.session_state['data']
x = df.iloc[:, :-1]
y = df.iloc[:, -1]

number1 = st.number_input('Insert first parameter', step=1, value=3, min_value=3)

number2 = st.number_input('Insert second parameter', step=1, value=2, min_value=2)

number3 = st.number_input('Insert third parameter', step=1, value=1, min_value=1)

if st.button('Tune now'):
    with st.spinner('Tuning is in the process...'):
        clf = GridSearchCV(svm.SVC(gamma='auto'), {  # Hyperparameter tuning part
            'C': [number1, number2, number3],
            'kernel': ['rbf', 'linear']
        }, cv=5, return_train_score=False)

        clf.fit(x, y)
        df = pd.DataFrame(clf.cv_results_)
        st.info(clf.best_params_)
        st.info(clf.best_score_)

        dictionary = clf.best_params_
        best_value = dictionary['C']
        best_kernel = dictionary['kernel']
        st.session_state['best_value'] = best_value
        st.session_state['best_kernel'] = best_kernel
