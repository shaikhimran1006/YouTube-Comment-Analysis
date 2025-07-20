# 🎬 YouTube Comment Sentiment Analysis App

🚀 **Live Demo:** [https://youtubecomment.streamlit.app/](https://youtubecomment.streamlit.app/)

---

## 📌 Overview

The **YouTube Comment Sentiment Analysis App** is a Streamlit-based web application that analyzes the sentiment of comments on any YouTube video. With a single YouTube link, it fetches top-level comments using the YouTube Data API and classifies each comment as **Positive**, **Negative**, or **Neutral** using NLP techniques. Results are displayed via charts and the video itself is embedded for reference.

---

## 🔍 Key Features

- 🔗 Extracts comments directly from YouTube video links
- ⚡ Real-time sentiment analysis using TextBlob
- 📊 Pie chart visualization of sentiment distribution
- 🎥 Embedded YouTube video playback
- ☁️ Deployed on Streamlit Cloud for public access

---

## 🧠 Sentiment Analysis Model

- **Model Used:** [TextBlob](https://textblob.readthedocs.io/en/dev/)
- **Approach:** Rule-based polarity scoring
- **Labels:**
  - `> 0`: Positive
  - `< 0`: Negative
  - `= 0`: Neutral
- TextBlob uses pretrained NLP corpora and lexicons to compute sentiment polarity scores.

---

## 🛠️ Tech Stack

| Component           | Technology                   |
|---------------------|-------------------------------|
| UI Framework        | Streamlit                    |
| Programming Language| Python                       |
| API Integration     | YouTube Data API v3          |
| Sentiment Analysis  | TextBlob                     |
| Visualization       | Matplotlib, Seaborn, WordCloud |
| Hosting             | Streamlit Cloud              |

---

## 📷 Sample UI

| Sentiment Pie Chart | Video Embed |
|---------------------|-------------|
| ![chart](https://i.imgur.com/XYZchart.png) | ![video](https://i.imgur.com/XYZvideo.png) |

_Replace above URLs with actual screenshots or use Streamlit’s screenshot tool._

---

## 🧪 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/shaikhimran1006/YouTube-Comment-Analysis.git
cd YouTube-Comment-Analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
