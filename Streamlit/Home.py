import streamlit as st # pip install streamlit

st.title('Welcome to Iris Classification')

# Range input for n_neighbors
# n_start, n_end = st.slider("Select Range for n_neighbors", min_value=1, max_value=10, value=(3, 7))

st.write("""
The Iris dataset was used in R.A. Fisher's classic 1936 paper, The Use of Multiple Measurements in Taxonomic Problems, and can also be found on the UCI Machine Learning Repository.

It includes three iris species with 50 samples each as well as some properties about each flower. One flower species is linearly separable from the other two, but the other two are not linearly separable from each other.

The columns in this dataset are:

- Id
- SepalLengthCm
- SepalWidthCm
- PetalLengthCm
- PetalWidthCm
- Species
""")