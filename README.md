# Iris Species Classifier – GCP Deployment

This project demonstrates the end-to-end deployment of a machine learning model using **Google Cloud Platform (GCP)**. The model predicts the species of an Iris flower based on sepal and petal dimensions. It includes both a **web interface** and an **API endpoint** for prediction.

## 🚀 Live Demo

🔗 Web App: [https://eminent-sunrise-459216-v2.el.r.appspot.com](https://eminent-sunrise-459216-v2.el.r.appspot.com)

## 🧠 Model Details

- **Algorithm**: Random Forest Classifier
- **Dataset**: Iris dataset (Week 4 toy data)
- **Framework**: Flask
- **Deployment**: GCP App Engine

## 📂 Project Structure
├── app.py # Flask application
├── app.yaml # GCP App Engine config
├── iris_model.pkl # Trained ML model
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Web UI for input and prediction

## 📡 API Endpoint

**URL**  
`POST /api`  
`https://eminent-sunrise-459216-v2.el.r.appspot.com/api`

**Sample JSON Input**
```json
{
  "feature1": 5.1,
  "feature2": 3.5,
  "feature3": 1.4,
  "feature4": 0.2
}

```markdown
```json
{
  "prediction": 0
}
```


✅ Features
Web app for user input and prediction

JSON API for integration

Fully hosted on GCP using App Engine (free tier)

Lightweight and scalable

🧑‍💻 Author
Ankita Roy
