# -------------------------------
# TITLE
# -------------------------------
st.markdown('<p class="big-title">📰 Fake News Detector</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Analyze news credibility using AI</p>', unsafe_allow_html=True)

st.divider()

# -------------------------------
# TEXT ANALYZER
# -------------------------------
st.subheader("📝 Analyze Text")

text_input = st.text_area("Paste News Text:", height=150)

if st.button("Analyze Text"):
    if text_input:
        cleaned = clean_text(text_input)
        transformed = vectorizer.transform([cleaned])

        prediction = model.predict(transformed)[0]
        proba = model.predict_proba(transformed)[0]
        confidence = max(proba)

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

if st.button("Analyze URL"):
    if url_input:
        try:
            article_text = get_article_text(url_input)

            cleaned = clean_text(article_text)
            transformed = vectorizer.transform([cleaned])

            prediction = model.predict(transformed)[0]
            proba = model.predict_proba(transformed)[0]
            confidence = max(proba)

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
# TRENDING NEWS (STATIC)
# -------------------------------
st.subheader("🔥 Trending Real News")

news_list = [
    "https://www.reuters.com/",
    "https://www.bbc.com/news",
    "https://apnews.com/",
    "https://www.thehindu.com/"
]

for link in news_list:
    st.markdown(f"- [{link}]({link})")