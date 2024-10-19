#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 00:03:00 2024

@author: nitinpatil
"""

import pickle
import streamlit as st
import pandas as pd  # Import pandas for DataFrame

# Load the saved model
with open('/Users/nitinpatil/Downloads/Drilling/Drilling.sav', 'rb') as file:
    model_cat = pickle.load(file)  # Make sure 'model_cat' is the correct name

st.title("Rate of Penetration (ROP) Prediction")

st.write("Enter the drilling parameters to predict ROP:")

depth_of_drilling = st.number_input("Depth of Drilling", value=0.0, step=0.000001, format="%.6f")
weight_on_bit = st.number_input("Weight on Bit", value=0.0, step=0.000001, format="%.6f")
Rotation_Per_Minute = st.number_input("Rotation Per Minute", value=0.0, step=0.000001, format="%.6f")
Porosity = st.number_input("Porosity", value=0.0, step=0.000001, format="%.6f")
Volume_of_Shale = st.number_input("Volume of Shale", value=0.0, step=0.000001, format="%.6f")
Water_Saturation = st.number_input("Water Saturation", value=0.0, step=0.000001, format="%.6f")
KLOGH = st.number_input("KLOGH", value=0.0, step=0.000001, format="%.6f")


# Create a DataFrame for the user input
user_input = pd.DataFrame({
    'depth_of_drilling': [depth_of_drilling],
    'weight_on_bit': [weight_on_bit],
    'Rotation_Per_Minute': [Rotation_Per_Minute],
    'Porosity': [Porosity],
    'Volume_of_Shale': [Volume_of_Shale],
    'Water_Saturation': [Water_Saturation],
    'KLOGH': [KLOGH]
})

if st.button("Predict ROP"):
    prediction = model_cat.predict(user_input)
    st.write(f"Predicted Rate of Penetration: {prediction[0]}")

