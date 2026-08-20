import joblib
import numpy as np
import pandas as pd
import streamlit as st

# Loading the model
ml_model = joblib.load('model.pkl')

st.title('Water Potability Detection')

ph = st.number_input('PH of Water', value = None, placeholder="0 - 14")

hardness = st.number_input('Hardness of Water', value = None, placeholder="47 - 323")

solids = st.number_input('Solids in Water', value = None, placeholder="320 - 61227")

chloramines = st.number_input('Chloramines of Water', value = None, placeholder="0.35 - 13.13")

sulfate = st.number_input('Sulfate of Water', value = None, placeholder="129 - 481")

conductivity = st.number_input('Conductivity of Water', value = None, placeholder="181.48 - 753.34")

organic_carbon = st.number_input('Organic_carbon of Water', value = None, placeholder="2.20 - 28.30")

trihalomethanes = st.number_input('Trihalomethanes of Water', value = None, placeholder="0.73 - 124")

turbidity = st.number_input('Turbidity of Water', value = None, placeholder="1.45 - 6.74")

input_data = np.array([ph, hardness, solids, chloramines, sulfate, 
        conductivity, organic_carbon, trihalomethanes, turbidity])



if st.button('Predict'):
    result = ml_model.predict([input_data])
    if result[0] == 1:
        st.success('The water is potable.')
    else:
        st.error('The water is not potable.')
