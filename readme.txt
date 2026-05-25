# Language Translator

A full-stack web application that translates text between 100+ languages and 
delivers results as both **readable text** and **spoken audio** — built with HTML, CSS, JavaScript and a Flask backend.

---

## Features

- **Text Translation** — Translate between 100+ languages using Google Translate
- **Speech Output** — Listen to translated text via gTTS (Google Text-to-Speech)
- **Auto Language Detection** — Detects the source language automatically

---

##  Tech Stack

| Layer     | Technology                  |
|-----------|-----------------------------|
| Frontend  | HTML5, CSS3, JavaScript     |
| Backend   | Python - Flask 3.0.3        |
| Translation | googletrans 4.0.0rc1      |
| Text-to-Speech | gTTS 2.5.1             |

---

## Project Structure

```
language-translator/
│
├── app.py                  # Flask application & API routes
├── requirements.txt        # Python dependencies
│
├── static/
│   ├── css/
│   │   └── style.css       # Stylesheet
│   ├── js/
│   │   └── script.js       # Frontend logic
│   └── audio/              # Temporary TTS audio files
│
└── templates/
    └── index.html          # Main HTML template
```

---

##  Prerequisites

- Python **3.8+**
- pip (Python package manager)
- Internet connection for Google Translate & gTTS APIs

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/language-translator.git
cd language-translator
```

### 2. Create a Virtual Environment

```bash
# Create venv
python -m venv venv

# Activate — macOS/Linux
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask App

```bash
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000
```

---

##  requirements.txt

```
googletrans==4.0.0rc1
Flask==3.0.3
gTTS==2.5.1
```

---

## API Endpoints

### `POST /translate`

Translates the provided text into the target language.

**Request Body (JSON):**

```json
{
  "text": "Hello, how are you?",
  "target_lang": "ta"
}
```

**Response (JSON):**

```json
{
  "translated_text": "வணக்கம், எப்படி இருக்கீங்க?",
  "source_lang": "en"
}
```

---

### `POST /speak`

Converts translated text into an audio file and returns it.

**Request Body (JSON):**

```json
{
  "text": "வணக்கம், எப்படி இருக்கீங்க?",
  "lang": "ta"
}
```

**Response:** Returns an `.mp3` audio file (`audio/mpeg`).

---

##  Working

```
User enters text
       │
       ▼
JavaScript sends POST → /translate
       │
       ▼
Flask calls googletrans to translate text
       │
       ▼
Translated text returned & displayed in UI
       │
       ▼
User clicks speak button to "Listen"
       │
       ▼
JavaScript sends POST → /speak
       │
       ▼
Flask calls gTTS → generates .mp3
       │
       ▼
Audio file streamed back → played in browser
```

---

## Supported Languages (Sample)

| Code | Language   |
|------|------------|
| `en` | English    |
| `ta` | Tamil      |
| `hi` | Hindi      |
| `fr` | French     |
| `de` | German     |
| `es` | Spanish    |
| `ja` | Japanese   |
| `zh-cn` | Chinese |
| `ar` | Arabic     |
| `ru` | Russian    |

---

## 📄 License

This project is licensed under the **MIT License**
Copyright (c) 2026 Ashwathi E

---


## 👨‍💻 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
