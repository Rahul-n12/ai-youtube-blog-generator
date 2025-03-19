# 🎙️ AI-Powered Blog Generator from YouTube Videos

This project extracts **transcripts from YouTube videos**, rewrites them into **SEO-friendly blog articles**, generates **AI-powered images (DALL·E)**, and creates **text-to-speech audio** for accessibility.

---

## 🚀 Features
- 🎥 **Extract YouTube Transcripts**: Automatically fetches captions (manual & auto-generated).
- ✍️ **AI-Powered Blog Generation**: Converts transcripts into engaging blog articles using **OpenAI GPT-4o**.
- 🏆 **Generate a Catchy Title**: AI creates an attractive blog title.
- 🎨 **AI-Generated Image (DALL·E 3)**: Blog header image creation.
- 🔊 **Convert Blog to Audio**: Uses `gTTS` to generate an MP3 voiceover.
- 🖥 **Streamlit Web Interface**: Easy-to-use interface.

---

## 🛠 Installation

### **Prerequisites**
Ensure you have the following installed:
- Python 3.x
- `pip install -r requirements.txt`

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Rahul-n12/ai-youtube-blog-generator.git
cd ai-youtube-blog-generator

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Set Up OpenAI API Key
Create a .env file in the project directory.
Add your OpenAI API key inside:

OPENAI_API_KEY=your_api_key_here

🖥 Usage
Run the Streamlit App

	streamlit run app.py

Using the App
1.Enter a YouTube Video URL in the input box.
2.Click "Generate Blog" to process the video.
3.The bot will:
	Extract the transcript.
	Rewrite it into a SEO-friendly blog.
	Generate an AI-powered image.
	Convert the text into audio (MP3).
	Download the blog, image, or audio as needed!

📂 Project Structure

ai-youtube-blog-generator/
│── app.py                 # Main application script
│── requirements.txt        # Dependencies
│── .env                    # API Key (not included in repo)
│── README.md               # Project documentation
│── generated/              # Folder for blog outputs
