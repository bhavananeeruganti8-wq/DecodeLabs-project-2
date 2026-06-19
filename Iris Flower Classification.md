# 🌸 Iris Flower Classification

## 📌 Project Overview
This project is a Machine Learning classification model that predicts the species of an Iris flower based on its measurements.

The model classifies flowers into the following categories:
- Setosa
- Versicolor
- Virginica

The project uses the K-Nearest Neighbors (KNN) algorithm from Scikit-learn.

---

## 🎯 Objective
To build a Machine Learning model that can accurately classify Iris flower species using supervised learning techniques.

---

## 📂 Dataset Information
The project uses the built-in Iris Dataset provided by Scikit-learn.

- Total Samples: 150
- Features: 4
- Classes: 3

### Features Used
1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width

---

## 🛠 Technologies Used
- Python
- Scikit-learn
- NumPy

---

## 🤖 Machine Learning Algorithm
**K-Nearest Neighbors (KNN)**

KNN classifies a flower by comparing its features with the nearest data points in the dataset.

---

## 🚀 Project Workflow
1. Load Iris Dataset
2. Extract Features and Labels
3. Apply Feature Scaling
4. Split Dataset into Training and Testing Sets
5. Train KNN Model
6. Predict Flower Species
7. Evaluate Model Performance
8. Display Accuracy, Confusion Matrix, and Classification Report

---

## 📊 Output
The program displays:

- Dataset Information
- Flower Categories
- Model Accuracy
- Confusion Matrix
- Classification Report

### Sample Result

```text
Accuracy: 100.0%

Confusion Matrix:
[[10 0 0]
[0 9 0]
[0 0 11]]
```

---

##️ How to Run

### Activate Virtual Environment

```bash
source venv/bin/activate
```

### Run the Project

```bash
python3 Iris.py
```

---

## 📈 Performance
- Accuracy: 100%
- Precision: 100%
- Recall: 100%
- F1-Score: 100
