import re
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS
from googleapiclient.discovery import build

# 🔹 Function to Extract Video ID from YouTube URL
def extract_video_id(youtube_url):
    """Extracts the YouTube video ID from a given URL."""
    pattern = r"(?:v=|\/|vi\/|embed\/|shorts\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, youtube_url)
    return match.group(1) if match else None

# 🔹 Function to Fetch YouTube Comments Using API
def get_youtube_comments(video_id, api_key, max_results=100):
    """Fetches comments from a YouTube video using YouTube Data API v3."""
    try:
        youtube = build("youtube", "v3", developerKey=api_key)
        comments = []
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            maxResults=max_results
        )
        response = request.execute()
        
        for item in response.get("items", []):
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)
        
        return comments
    except Exception as e:
        st.error(f"Error fetching comments: {e}")
        return []

# 🔹 Function to Perform Sentiment Analysis
def analyze_sentiment(comment):
    """Analyzes sentiment of a comment using TextBlob."""
    sentiment = TextBlob(comment).sentiment.polarity
    return "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"

# 🔹 Streamlit UI with Compact Layout
st.set_page_config(layout="wide")  # Set layout to wide mode
st.title("🎬 YouTube Comment Sentiment Analysis")

API_KEY = "AIzaSyCqOyUDQxMac1uOF3lqYHqSptE6mANvqXM"

# Input Section
youtube_url = st.text_input("🔗 Enter YouTube Video URL:")
if st.button("🔍 Analyze"):
    if youtube_url:
        video_id = extract_video_id(youtube_url)

        if video_id:
            st.markdown(f"<p style='font-size:12px; color:gray;'>✅ Extracted Video ID: <b>{video_id}</b></p>", unsafe_allow_html=True)

            # Display YouTube Video Thumbnail
            video_thumbnail = f"https://img.youtube.com/vi/{video_id}/0.jpg"

            # Fetch comments
            comments = get_youtube_comments(video_id, API_KEY)

            if comments:
                st.markdown(f"<p style='font-size:12px; color:gray;'>✅ Fetched <b>{len(comments)}</b> comments.</p>", unsafe_allow_html=True)

                # Create DataFrame
                df = pd.DataFrame(comments, columns=["Comment"])
                df["Sentiment"] = df["Comment"].apply(analyze_sentiment)

                # 🔹 Arrange UI for Single Screenshot View
                col1, col2, col3 = st.columns([1, 1.5, 1.5])  # Three columns layout

                with col1:
                    st.image(video_thumbnail, caption="🎥 Video Thumbnail", use_column_width=True)

                with col2:
                    st.subheader("📊 Sentiment Distribution")
                    fig, ax = plt.subplots(figsize=(3, 3))  # Set graph size to 3x3
                    sns.countplot(x=df["Sentiment"], palette="viridis", ax=ax)
                    plt.xlabel("Sentiment")
                    plt.ylabel("Count")
                    st.pyplot(fig)


            else:
                st.warning("⚠ No comments found on this video.")
        else:
            st.error("❌ Invalid YouTube URL. Please enter a valid one.")
