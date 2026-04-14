# 📰 Fake News Detection App

![Python](https://img.shields.io/badge/Python-3.10-blue)
![NLP](https://img.shields.io/badge/NLP-Fake%20News%20Detection-purple)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Logistic%20Regression-green)
![Vectorizer](https://img.shields.io/badge/Vectorizer-TF--IDF-orange)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)
![API](https://img.shields.io/badge/API-GNews-yellow)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit%20Cloud-brightgreen)
![Status](https://img.shields.io/badge/Status-Live-success)

---

## 🚀 Live Demo

👉 https://fake-news-detector-ujjawal.streamlit.app

---

## 📌 Problem Statement

In today’s digital world, misinformation spreads rapidly through social media and online platforms.  
It becomes difficult for users to verify whether a news article is genuine or fake.

👉 This project aims to **automatically detect fake news using Machine Learning and NLP techniques.**

---

## 💡 Solution

We built an **AI-powered web application** that:

- Analyzes news text  
- Extracts content from URLs  
- Classifies news as **Real or Fake**  
- Provides a confidence score  
- Shows trending real-world news  

---

## 🎯 Features

- 📝 Text-based fake news detection  
- 🌐 URL-based article analysis  
- 📊 Confidence score with progress bar  
- 🔍 Article preview for better understanding  
- 🔥 Live trending news using GNews API  
- 🎨 Interactive and modern UI (Streamlit)

---

## 🧠 Tech Stack

### 🔹 Programming
- Python  

### 🔹 Machine Learning
- Logistic Regression  

### 🔹 NLP
- TF-IDF Vectorization  

### 🔹 Frontend
- Streamlit  

### 🔹 APIs
- GNews API (for trending news)

### 🔹 Libraries Used
- scikit-learn  
- pandas  
- numpy  
- newspaper3k  
- requests  

---

## 📂 Project Structure

```
fake_news_project/
│
├── app/
│   └── app.py              # Streamlit application
│
├── data/
│   ├── Fake.csv           # Fake news dataset
│   └── True.csv           # Real news dataset
│
├── model/
│   ├── model.pkl          # Trained ML model
│   └── vectorizer.pkl     # TF-IDF vectorizer
│
├── main.py                # Model training script
├── requirements.txt       # Dependencies
└── README.md              # Documentation
```

---

## ⚙️ How It Works (Step-by-Step)

### 1️⃣ Data Collection
- Used two datasets:
  - Fake News  
  - Real News  

---

### 2️⃣ Data Preprocessing
- Converted text to lowercase  
- Removed special characters using regex  
- Cleaned noise and unwanted symbols  

---

### 3️⃣ Feature Engineering
- Applied **TF-IDF Vectorizer**
- Converted text into numerical vectors  

---

### 4️⃣ Model Training
- Used **Logistic Regression**
- Split dataset into training and testing  
- Achieved high accuracy (~99%)  

---

### 5️⃣ Prediction Pipeline
User input → Clean text → Transform (TF-IDF) → Model prediction  

Output:
- Real / Fake  
- Confidence score  

---

## 🌐 URL Processing

- Uses `newspaper3k` library  
- Extracts full article text automatically  
- Applies same ML pipeline for prediction  

---

## 🔥 Trending News Feature

- Integrated with **GNews API**
- Fetches real-time headlines  
- Displays:
  - Title  
  - Source  
  - Link  

---

## 📊 Model Performance

- Accuracy: ~99%  
- Precision: High  
- Recall: High  

👉 Note: High accuracy is due to dataset characteristics.

---

## ⚠️ Limitations

- Model trained on specific dataset → may not generalize fully  
- Cannot verify factual correctness (pattern-based prediction)  
- Sensitive to writing style differences  

---

## 🚀 Future Improvements

- Use BERT / Transformers for better understanding  
- Add explainability (why prediction is fake/real)  
- Improve UI with dashboard design  
- Add multilingual support  
- Store prediction history  

---

## ▶️ Run Locally

### 1. Clone Repository
```
git clone https://github.com/your-username/fake-news-project.git
cd fake-news-project
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3. Run App
```
streamlit run app/app.py
```

---

## ☁️ Deployment

Deployed using **Streamlit Community Cloud**

---

## 👨‍💻 Author

**Ujjawal Shrivastava**  
Aspiring Data Scientist  

---

## ⭐ Conclusion

This project demonstrates how **Machine Learning + NLP** can be applied to solve real-world problems like fake news detection.

It showcases:
- End-to-end ML pipeline  
- Real-time API integration  
- Interactive UI development  
- Cloud deployment  
