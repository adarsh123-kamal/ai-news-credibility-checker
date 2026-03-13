# 📰 AI News Credibility Checker

An intelligent web application that analyzes the credibility of news articles using **Machine Learning, Natural Language Processing (NLP), and real-time news verification**.

The system extracts the main claim from a news article, searches for supporting sources on the web, and combines **ML predictions + news coverage evidence** to estimate whether the news is likely real or fake.

---

## 🚀 Live Demo

Streamlit App:
https://ai-news-credibility-checker-6pwzkeinibjxcee3vxad66.streamlit.app/

---

## 🎯 Features

* 🔎 **Claim Extraction**
  Automatically detects the main claim from a news article.

* 🤖 **Machine Learning Prediction**
  Uses a trained NLP model to classify news as **REAL or FAKE**.

* 📊 **Credibility Score System**
  Combines ML prediction and number of supporting news articles.

* 🌍 **Real News Verification**
  Searches the internet to find related news sources.

* 📈 **Trending News Analysis**
  Analyzes current trending headlines and evaluates credibility.

* 📉 **Visualization Dashboard**
  Interactive charts showing credibility scores and evidence.

---

## 🧠 Machine Learning Pipeline

1. Data Collection (Fake & Real News Dataset)
2. Text Preprocessing
3. Stopword Removal
4. TF-IDF Vectorization
5. Model Training
6. Model Serialization
7. Real-time Prediction via Web App

---

## 🛠 Tech Stack

**Programming**

* Python

**Machine Learning**

* Scikit-learn
* TF-IDF Vectorizer
* NLP preprocessing (NLTK)

**Web App**

* Streamlit

**Visualization**

* Plotly

**Data Processing**

* Pandas
* NumPy

---


📊 Dataset

This project uses the Fake and Real News Dataset from Kaggle.

Dataset Link:
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

Dataset Overview

The dataset contains labeled news articles used for binary text classification (Fake vs Real). It includes approximately 45,000+ news articles collected from various news websites. ()

Files

Fake.csv – contains fake news articles

True.csv – contains real news articles

Dataset Features

Each news article includes the following attributes:

title – headline of the news article

text – full news article content

subject – news category

date – publication date

Dataset Usage in this Project

The dataset was used for:

Training the machine learning model

Text preprocessing and feature extraction

TF-IDF vectorization

Fake vs Real news classification

Due to GitHub file size limitations, the dataset is not included in this repository.
You can download it from Kaggle using the link above.

---


## 📂 Project Structure

```
fake_news_detection/
│
├── app/
│   └── app.py                # Streamlit application
│
├── models/
│   ├── model.pkl             # Trained ML model
│   └── vectorizer.pkl        # TF-IDF vectorizer
│
├── src/
│   ├── article_fetcher.py
│   ├── claim_extractor.py
│   ├── news_search.py
│   ├── preprocessing.py
│   ├── train_model.py
│   └── trending_news.py
│
├── notebooks/
│   └── eda.ipynb             # Data analysis notebook
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/adarsh123-kamal/ai-news-credibility-checker.git
cd ai-news-credibility-checker
```

Create virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the app:

```
streamlit run app/app.py
```

---

## 📊 Example Workflow

1. Enter a **news headline or article**
2. System extracts the **main claim**
3. Searches for **related news sources**
4. Runs **ML prediction**
5. Generates **credibility score**
6. Displays **supporting evidence**

---

📷 Application Screenshots
Homepage
![alt text](image.png)

News Credibility Analysis
![alt text](image-1.png)

Credibility Score Visualization
![alt text](image-2.png)
![alt text](image-3.png)
![alt text](image-4.png)

Trending News Dashboard
![alt text](image-5.png)
![alt text](image-6.png)
![alt text](image-7.png)
![alt text](image-8.png)

---

## 📌 Future Improvements

* Deep learning model (BERT / Transformer)
* Multi-language fake news detection
* Social media misinformation detection
* Explainable AI (XAI) for predictions
* Browser extension for real-time verification

---

## 👨‍💻 Author

**Adarsh Kamal**

GitHub:
https://github.com/adarsh123-kamal

---

## ⭐ If you like this project

Give it a **star** on GitHub to support the project.
