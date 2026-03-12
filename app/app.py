import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
import plotly.graph_objects as go

from src.news_search import search_news
from src.article_fetcher import get_article_text
from src.trending_news import get_trending_news
from src.claim_extractor import extract_claim

# ---------------- SESSION STATE ----------------
if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI News Credibility Checker",
    page_icon="📰",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main-title{
text-align:center;
font-size:42px;
font-weight:bold;
margin-bottom:10px;
}

.subtitle{
text-align:center;
color:gray;
margin-bottom:35px;
}

.score-card{
background:#f5f7fb;
padding:25px;
border-radius:12px;
margin-top:10px;
}

.news-card{
border:1px solid #e6e6e6;
border-radius:10px;
padding:15px;
margin-bottom:15px;
}

.news-card:hover{
background:#f9fafc;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="main-title">📰 AI News Credibility Checker</div>', unsafe_allow_html=True)

st.markdown(
'<div class="subtitle">Analyze news credibility using Machine Learning and real-time news verification</div>',
unsafe_allow_html=True
)

# ---------------- LOAD MODEL ----------------
nltk.download('stopwords')

model = pickle.load(open("models/model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

stop_words = set(stopwords.words("english"))

# ---------------- TEXT CLEANING ----------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

# ---------------- INPUT ----------------
news_text = st.text_area("Enter News Article or Headline")

# ---------------- ANALYSIS ----------------
if st.button("Analyze News"):

    st.session_state.analyzed = True

    if news_text.strip() == "":
        st.warning("Please enter some news text")

    else:

        # -------- Claim Extraction --------
        claim = extract_claim(news_text)

        st.subheader("Detected Claim")
        st.info(claim)

        with st.spinner("Analyzing news credibility..."):

            # -------- Search News using CLAIM --------
            results = search_news(claim)
            article_count = len(results)

            # -------- Get Article Text --------
            if article_count > 0:

                article_text = get_article_text(results[0]["link"])

                if article_text:
                    text_to_analyze = article_text[:2000]
                else:
                    text_to_analyze = claim

            else:
                text_to_analyze = claim

            # -------- ML Prediction --------
            cleaned = clean_text(text_to_analyze)
            vector = vectorizer.transform([cleaned])

            prediction = model.predict(vector)[0]

            # -------- ML Confidence --------
            proba = model.predict_proba(vector)[0]
            fake_prob = proba[0] * 100
            real_prob = proba[1] * 100

            # -------- Original Credibility Score Logic --------
            score = 0
            score += min(article_count * 15, 75)

            if prediction == "REAL":
                score += 25

        # ---------------- RESULTS ----------------
        st.subheader("Analysis Result")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("ML Prediction", prediction)

        with col2:
            st.metric("News Articles Found", article_count)

        # ---------------- MODEL CONFIDENCE ----------------
        st.subheader("Model Confidence")

        st.progress(real_prob / 100)

        col3, col4 = st.columns(2)

        with col3:
            st.metric("REAL Probability", f"{real_prob:.1f}%")

        with col4:
            st.metric("FAKE Probability", f"{fake_prob:.1f}%")

        # ---------------- GAUGE CHART ----------------
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            title={'text': "Credibility Score"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "blue"},
                'steps': [
                    {'range': [0, 40], 'color': "#ff4d4d"},
                    {'range': [40, 70], 'color': "#ffd633"},
                    {'range': [70, 100], 'color': "#66cc66"}
                ],
            }
        ))

        st.plotly_chart(fig, use_container_width=True)

        # ---------------- FINAL RESULT ----------------
        if score >= 70:
            st.success("Likely Real News")
        elif score >= 40:
            st.warning("Uncertain — Verify from multiple sources")
        else:
            st.error("Likely Fake News")

        # ---------------- EVIDENCE PIE CHART ----------------
        labels = ["News Coverage Evidence", "ML Confidence"]

        values = [
            article_count * 15,
            25 if prediction == "REAL" else 0
        ]

        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=.4
        )])

        st.subheader("Evidence Distribution")
        st.plotly_chart(fig, use_container_width=True)

        # ---------------- NEWS ARTICLES ----------------
        st.subheader("Related News Articles")

        if article_count == 0:
            st.info("No related articles found.")

        else:
            for r in results:

                st.markdown(
                    f"""
                    <div class="news-card">
                    <h4>📰 {r['title']}</h4>
                    <a href="{r['link']}" target="_blank">Read full article</a>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# ---------------- TRENDING NEWS (ONLY AFTER ANALYSIS) ----------------
if st.session_state.analyzed:

    st.divider()
    st.header("🔥 Trending News Analysis")

    trending = get_trending_news()

    titles = []
    scores = []

    for item in trending:

        results = search_news(item["title"])
        article_count = len(results)

        score = min(article_count * 15, 100)

        titles.append(item["title"][:50])
        scores.append(score)

        if score >= 70:
            label = "Likely Real"
            color = "green"
        elif score >= 40:
            label = "Uncertain"
            color = "orange"
        else:
            label = "Likely Fake"
            color = "red"

        st.markdown(f"""
        **{item['title']}**

        Credibility Score: **{score}%**

        Status: :{color}[{label}]

        ---
        """)

    fig = go.Figure()

    fig.add_bar(x=titles, y=scores)

    fig.update_layout(
        title="Trending News Credibility Dashboard",
        xaxis_title="News Headlines",
        yaxis_title="Credibility Score"
    )

    st.plotly_chart(fig, use_container_width=True)