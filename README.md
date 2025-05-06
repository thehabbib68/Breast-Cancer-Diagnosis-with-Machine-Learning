# Breast Cancer Diagnosis with Machine Learning

This project aims to predict whether a breast tumor is benign or malignant using machine learning techniques. It leverages the Breast Cancer Wisconsin dataset and is deployed as a Streamlit web application for interactive predictions.

---

## 🧪 Problem Statement

Early and accurate diagnosis of breast cancer is crucial for effective treatment. This project builds a machine learning pipeline to assist medical professionals by providing instant predictions based on tumor characteristics.

---

## 📊 Dataset

- **Source**: UCI Machine Learning Repository  
- **Dataset**: [Breast Cancer Wisconsin (Diagnostic)](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))  
- **Features**: 30 numeric features (mean, standard error, and worst values of radius, texture, etc.)  
- **Target**: Diagnosis (`M` = Malignant, `B` = Benign)

---

## 🔍 Project Workflow

### 1. **Data Preprocessing**
- Removed unnecessary columns (`id`, `Unnamed: 32`)
- Encoded target variable (`M` → 1, `B` → 0)
- Checked for null values and corrected data types

### 2. **Exploratory Data Analysis (EDA)**
- Distribution of target classes
- Correlation heatmap for top features
- Pair plots for selected features
- Outlier and skewness detection

### 3. **Feature Engineering**
- Standardized all numeric features using `StandardScaler`
- No missing values or categorical features to encode

### 4. **Model Building**
Tested multiple models:
- Logistic Regression
- K-Nearest Neighbors
- Support Vector Machine
- Random Forest (Best performing)
- Gradient Boosting

### 5. **Hyperparameter Tuning**
- Used `GridSearchCV` and `RandomizedSearchCV` to tune models
- Best parameters selected for Random Forest

### 6. **Evaluation**
- Evaluated using Accuracy, Precision, Recall, F1-score
- Visualized Confusion Matrix and ROC-AUC Curve

### 7. **Deployment**
- Built an interactive web application using **Streamlit**
- Users input 30 feature values
- Model outputs "Benign" or "Malignant" in real time

### 8.  **Results**
  -  Best Performing Model: Random Forest Classifier
  -  Accuracy: ~98%
  -  Precision: ~98%
  -  Recall: ~97%
  -  ROC-AUC Score: ~0.99
  -  Achieved strong balance between sensitivity and specificity

### 9.  **Tools Used**
  -  Languages: Python
  -  Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn
  -  Deployment: Streamlit
  -  Model Selection: GridSearchCV, RandomizedSearchCV
  -  Preprocessing: StandardScaler

### 10.   👨‍💻 Author

Syed Habib Haider
Data Scientist & AI Consultant
🔗 LinkedIn
🔗 GitHub
