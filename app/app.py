# -------------------------------
# IMPORTS
# -------------------------------
import streamlit as st
import pickle
import re
import requests
from newspaper import Article

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Fake News Detector", page_icon="📰")

# -------------------------------
# LOAD MODEL
# -------------------------------
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

# -------------------------------
# FUNCTIONS
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def get_article_text(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def get_trending_news():
    api_key = "f2927f68e4202fedd000f77203c204e0"

    url = f"https://gnews.io/api/v4/top-headlines?lang=en&country=in&max=5&token={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        articles = []
        for item in data.get("articles", []):
            articles.append({
                "title": item.get("title", "No title"),
                "source": item.get("source", {}).get("name", "Unknown"),
                "link": item.get("url", "#")
            })

        return articles
    except:
        return []

# -------------------------------
# CSS (🔥 FIXED TITLE UI)
# -------------------------------
st.markdown("""
<style>
.big-title {
    text-align: center;
    font-size: 65px;
    font-weight: 800;
    margin-bottom: 5px;
}

.logo {
    font-size: 55px;
    margin-right: 10px;
}

.sub-text {
    text-align: center;
    color: #9ca3af;
    font-size: 18px;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# TITLE (🔥 FIXED ALIGNMENT)
# -------------------------------
st.markdown("""
<h1 class="big-title">
<span class="logo">📰</span> Fake News Detector
</h1>
""", unsafe_allow_html=True)

st.markdown('<p class="sub-text">Analyze news credibility using AI</p>', unsafe_allow_html=True)

st.divider()

# -------------------------------
# TEXT ANALYZER
# -------------------------------
st.subheader("📝 Analyze Text")

text_input = st.text_area("Paste News Text:", height=150)

if st.button("🔍 Analyze Text"):
    if text_input:
        cleaned = clean_text(text_input)
        transformed = vectorizer.transform([cleaned])

        prediction = model.predict(transformed)[0]
        proba = model.predict_proba(transformed)[0]
        confidence = max(proba)

        st.progress(float(confidence))

        if prediction == 1:
            st.success(f"✅ Real News ({confidence*100:.2f}%)")
        else:
            st.error(f"❌ Fake News ({confidence*100:.2f}%)")
    else:
        st.warning("Enter text")

st.divider()

# -------------------------------
# URL ANALYZER
# -------------------------------
st.subheader("🌐 Analyze URL")

url_input = st.text_input("Paste News URL:")

if st.button("🔍 Analyze URL"):
    if url_input:
        try:
            article_text = get_article_text(url_input)

            st.info(article_text[:300] + "...")

            cleaned = clean_text(article_text)
            transformed = vectorizer.transform([cleaned])

            prediction = model.predict(transformed)[0]
            proba = model.predict_proba(transformed)[0]
            confidence = max(proba)

            st.progress(float(confidence))

            if prediction == 1:
                st.success(f"✅ Real News ({confidence*100:.2f}%)")
            else:
                st.error(f"❌ Fake News ({confidence*100:.2f}%)")

        except:
            st.error("⚠️ Could not process URL")
    else:
        st.warning("Enter URL")

st.divider()

# -------------------------------
# TRENDING NEWS
# -------------------------------
st.subheader("🔥 Trending Real News")

news_list = get_trending_news()

if not news_list:
    st.warning("⚠️ Unable to load news. Check API or internet.")
else:
    for news in news_list:
        st.markdown(f"""
        <div style="
            background-color:#111827;
            padding:15px;
            border-radius:10px;
            margin-bottom:10px;
            border:1px solid #333;
        ">
            <h4 style="margin:0;">📰 {news['title']}</h4>
            <p style="color:gray; margin:5px 0;">Source: {news['source']}</p>
            <a href="{news['link']}" target="_blank" style="color:#4CAF50;">
                🔗 Read full article
            </a>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------
# REFRESH BUTTON
# -------------------------------
if st.button("🔄 Refresh News"):
    st.rerun()
