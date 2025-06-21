# 💳 Credit Default Detection System

This project is an end-to-end machine learning application to predict whether a customer will default on their credit payment. It includes model training, deployment via FastAPI, and a user-friendly Streamlit frontend. The solution is fully containerized with Docker for scalable and reproducible deployment.

---

## 🚀 Key Features

- ✅ Predict customer default risk using credit history and demographic features.
- ⚡ FastAPI backend serving a trained machine learning model.
- 🌐 Streamlit UI for interactive predictions.
- 🐳 Dockerized setup for easy deployment and portability.
- 📊 Model trained using a Random Forest classifier with good performance metrics.

---

## 📌 Project Objective

To help financial institutions assess the creditworthiness of customers by predicting the likelihood of default using historical payment behavior, credit limits, education, and marital status.

---

## 🛠️ Tech Stack

- **Python**
- **Scikit-learn** – ML modeling
- **FastAPI** – API backend
- **Streamlit** – Frontend web app
- **Docker** – Containerization
- **Joblib** – Model serialization

---

## 🔍 Model & Results

- **Model Used**: Random Forest Classifier
- **Input Features**: 26 (e.g., payment history, bill amounts, demographic info)
- **Target Variable**: Default (Yes/No)
- **Train/Test Split**: 75/25

### 📈 Evaluation Metrics:

| Metric         | Score   |
|----------------|---------|
| Accuracy       | **74%** |
| Precision      | **38%** |
| Recall         | **68%** |
| F1-Score       | **49%** |


The model performs well as the dataset was highly imbalance, especially in identifying customers who are likely to default, making it useful in real-world financial risk applications.

---

## 🖥️ How to Run

### 🔹 1. Clone the repository

```bash
git clone https://github.com/your-username/credit-default-detector.git
cd credit-default-detector
```
### 2. Build Docker image
```bash
docker build -t credit-default-api .
```
### 3. Run Docker container
```bash
docker run -d -p 8000:8000 credit-default-api
```
This will start the FastAPI backend server at: http://localhost:8000

### 4. Start streamlit app
```bash
streamlit run frontend.py
```
You can now interact with the model through a UI at http://localhost:8501


