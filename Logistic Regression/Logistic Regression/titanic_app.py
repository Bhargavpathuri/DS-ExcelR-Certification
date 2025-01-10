# -*- coding: utf-8 -*-
"""titanic_app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UZgl3nJ-XCbNJlYeVf9PUPTamcQMyupM
"""

import streamlit as st
import numpy as np
import joblib

# Loading the trained logistic regression model
@st.cache_resource
def load_model():
    return joblib.load('logistic_model.pkl')

model = load_model()
st.title("Titanic Survival Prediction App")
# App description
st.markdown("""
This application predicts the survival probability of a Titanic passenger based on their details.
Fill in the form below and click 'Predict Survival' to see the result.
""")
# User inputs
pclass = st.selectbox("Passenger Class (Pclass)", [1, 2, 3], help="1: First class, 2: Second class, 3: Third class")
sex = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", min_value=0.42, max_value=100.0, value=30.0, step=0.1)
sibsp = st.number_input("Number of Siblings/Spouses Aboard (SibSp)", min_value=0, max_value=10, value=0, step=1)
parch = st.number_input("Number of Parents/Children Aboard (Parch)", min_value=0, max_value=10, value=0, step=1)
fare = st.slider("Fare Paid", min_value=0.0, max_value=600.0, value=15.0, step=0.1)
embarked = st.selectbox("Port of Embarkation", ["Southampton", "Cherbourg", "Queenstown"])
# Mapping categorical inputs to numerical values
sex_mapping = {"Male": 1, "Female": 0}
embarked_mapping = {"Southampton": 0, "Cherbourg": 1, "Queenstown": 2}
# Converting inputs to numeric values
sex = sex_mapping[sex]
embarked = embarked_mapping[embarked]
# Prediction button
if st.button("Predict Survival"):
    input_data = np.array([[pclass, sex, age, sibsp, parch, fare, embarked]])
    survival_probability = model.predict_proba(input_data)[0][1]  # Probability of survival
    # Displaying the result
    st.write(f"### Survival Probability: **{survival_probability * 100:.2f}%**")
    if survival_probability >= 0.5:
        st.success("This passenger is likely to survive.")
    else:
        st.error("This passenger is unlikely to survive.")