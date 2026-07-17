
# 🤖 Gemini LLM Application

An AI-powered web application built with **Streamlit** and **Google Gemini API** that enables users to interact with Google's Large Language Models through an intuitive interface. The application supports both **text generation** and **image understanding** using Gemini's multimodal capabilities.

## ✨ Features

- 💬 AI-powered conversational chatbot
- 🖼️ Image analysis and description using Gemini Vision
- ❓ Question Answering interface
- ⚡ Fast responses using Google's Gemini models
- 🎨 Clean and responsive Streamlit UI
- 🔒 Secure API key management using environment variables

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Google Gemini API**
- **Pillow (PIL)**
- **python-dotenv**

---

## 📂 Project Structure

```
Gemini-LLM-Application/
│
├── app.py              # Text Chatbot
├── vision.py           # Image Understanding
├── qachat.py           # Question Answering
├── requirements.txt
├── .env
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/vrindaaguptaa/Gemini-LLM-Application.git

cd Gemini-LLM-Application
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

You can obtain an API key from **Google AI Studio**.

---

## ▶️ Running the Application

### Text Chatbot

```bash
streamlit run app.py
```

### Image Understanding

```bash
streamlit run vision.py
```

### Question Answering

```bash
streamlit run qachat.py
```

---

## 📸 Features

### 💬 Chatbot

- Ask general-purpose questions
- Generate text responses
- Content generation
- Summarization

### 🖼️ Vision

- Upload JPG, JPEG, or PNG images
- Analyze image content
- Describe objects and scenes
- Answer questions about uploaded images

### ❓ Question Answering

- Natural language question answering
- Informative AI-generated responses

---

## 📦 Dependencies

- streamlit
- google-generativeai
- Pillow
- python-dotenv

Install using

```bash
pip install -r requirements.txt
```

---

## 📌 Future Improvements

- Conversation history
- Multi-turn chat
- PDF document analysis
- Voice input
- Image generation
- Modern UI/UX
- Chat export functionality

---

## 👩‍💻 Author

**Vrinda Gupta**

GitHub: https://github.com/vrindaaguptaa
