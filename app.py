import streamlit as st
import numpy as np
import pickle

# Load trained model and scaler
model = pickle.load(open('best_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title('🩺 Breast Cancer Diagnosis Predictor')
st.markdown('Enter the tumor measurements below to predict if it is **Benign** or **Malignant**.')

# Feature names
feature_names = [
    'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
    'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
    'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
    'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 'fractal_dimension_se',
    'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst',
    'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst'
]

# Create input fields in pairs
features = []
for i in range(0, len(feature_names), 2):
    cols = st.columns(2)
    for j in range(2):
        if i + j < len(feature_names):
            value = cols[j].number_input(f'{feature_names[i + j]}', step=0.01, format="%.4f")
            features.append(value)

# Convert to array and scale
features = np.array([features])
features_scaled = scaler.transform(features)

# Predict
if st.button('Predict'):
    prediction = model.predict(features_scaled)
    if prediction[0] == 1:
        st.error('⚠️ The tumor is **Malignant**.')
    else:
        st.success('✅ The tumor is **Benign**.')