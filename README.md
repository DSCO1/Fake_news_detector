# 📰 Fake News Detection App

![Python](https://img.shields.io/badge/Python-3.10-blue)
![NLP](https://img.shields.io/badge/NLP-Fake%20News%20Detection-purple)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Logistic%20Regression-green)
![Vectorizer](https://img.shields.io/badge/Vectorizer-TF--IDF-orange)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)
![API](https://img.shields.io/badge/API-GNews-yellow)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit%20Cloud-brightgreen)
![Status](https://img.shields.io/badge/Status-Completed-success)

An AI-powered web application that detects whether a news article is **Real or Fake** using Machine Learning.

---

## 🚀 Project Overview

This project uses **Natural Language Processing (NLP)** and **Machine Learning** to classify news content.  
Users can:

- Paste news text  
- Provide a news article URL  
- Get prediction with confidence score  
- View trending real-time news  

---

## 🎯 Features

- 📝 Text-based fake news detection  
- 🌐 URL-based article analysis  
- 📊 Confidence score visualization  
- 🔍 Article preview (for URL input)  
- 🔥 Live trending news (via API)  
- 🎨 Clean and modern UI (Streamlit)

---

## 🧠 Tech Stack

- Frontend: Streamlit  
- Backend: Python  
- ML Model: Logistic Regression  
- Vectorization: TF-IDF  

### Libraries Used:
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
│   └── app.py
│
├── data/
│   ├── Fake.csv
│   └── True.csv
│
├── model/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

### 1. Data Processing
- Combined Fake.csv and True.csv  
- Cleaned text using regex  
- Removed special characters  

### 2. Feature Extraction
- Used TF-IDF Vectorizer  
- Converted text into numerical format  

### 3. Model Training
- Algorithm: Logistic Regression  
- Split data into train/test  
- Achieved ~99% accuracy  

### 4. Prediction
- Input → Clean → Vectorize → Predict  
- Output:
  - Real / Fake  
  - Confidence score  

---

## 🌐 URL Processing

- Uses `newspaper3k`  
- Extracts full article text automatically  

---

## 🔥 Trending News

- Uses GNews API  
- Fetches live headlines  
- Displays:
  - Title  
  - Source  
  - Link  

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

You can deploy this project on:

- Streamlit Community Cloud (Recommended)  
- Render  
- Hugging Face Spaces  
- GCP  

---

## 🔐 API Configuration

1. Get API key from: https://gnews.io/  
2. Add in code:
```
api_key = "YOUR_API_KEY"
```

---

## 📊 Sample Output

- ✅ Real News (92.45%)  
- ❌ Fake News (87.12%)  

---

## ⚠️ Limitations

- Model trained on limited dataset  
- May not generalize perfectly  
- Uses TF-IDF (no deep understanding of context)  

---

## 🚀 Future Improvements

- Use BERT / Transformers  
- Add explanation for predictions  
- Improve UI  
- Add multilingual support  
- Store prediction history  

---

## 👨‍💻 Author

Ujjawal Shrivastava  
Aspiring Data Scientist  

---

## ⭐ Conclusion

This project demonstrates how Machine Learning and NLP can be used to detect fake news and combat misinformation.
