import streamlit as st
import yt_dlp
import openai
import os
from gtts import gTTS
from io import BytesIO
from PIL import Image
import requests
from dotenv import load_dotenv

# Set OpenAI API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to extract transcript
def get_youtube_transcript(youtube_url):
    ydl_opts = {
        'cookies-from-browser': 'chrome',
        'quiet': True,
        'skip_download': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en'],
        'outtmpl': '%(id)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        subtitles = info.get('automatic_captions', {}).get('en', [])
        if subtitles:
            transcript_url = subtitles[0]['url']
            transcript_text = requests.get(transcript_url).text
            return transcript_text[:5000]  # Limit words for token efficiency
    return None

# Function to generate a spinned article using AI
def generate_spinned_article(transcript):
    prompt = f"Rewrite this transcript as a fresh, **SEO-friendly** blog article with an engaging tone, **using markdown formatting**:\n\n{transcript}"
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Function to generate a title
def generate_title(article_text):
    prompt = f"Generate a catchy blog title for this content with an engaging tone, **using markdown formatting**:\n\n{article_text}"
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Function to generate an image using DALL·E
def generate_image(title):
    response = openai.images.generate(
        model="dall-e-3",
        prompt=f"A blog header image for: {title}, **modern, abstract style**",
        n=1,
        size="1024x1024"
    )
    return response.data[0].url

# Function to generate audio from text
def generate_audio(text):
    tts = gTTS(text)
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)   
    audio_fp.seek(0)
    return audio_fp

# Streamlit UI
st.title("📝 AI-Powered Blog Generator from YouTube Video")

youtube_link = st.text_input("Paste YouTube Video URL Here", "")

if youtube_link:
    with st.spinner("Extracting content..."):
        transcript = get_youtube_transcript(youtube_link)
        if transcript:
            spinned_article = generate_spinned_article(transcript)
            title = generate_title(spinned_article)
            image_url = generate_image(title)
            audio_fp = generate_audio(spinned_article)

            # Display results
            st.header(title)
            st.image(image_url, caption="AI-Generated Blog Image")
            st.write(spinned_article)
            st.audio(audio_fp, format="audio/mp3")
        else:
            st.error("Could not extract transcript. Try another video.")

