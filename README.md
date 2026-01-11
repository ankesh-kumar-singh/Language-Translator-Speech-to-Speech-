#  Voice Translator using Python (Speech → Text → Translation → Speech)

A Python-based **Voice Translator GUI application** that listens to user speech in English, translates it into a selected target language, and speaks the translated output aloud. The project uses **speech recognition**, **machine translation**, and **text-to-speech synthesis**, all wrapped in a **Tkinter GUI**.

---

##  Features

- Speech-to-text using microphone
- Translate spoken English into multiple languages
- Convert translated text into speech
- Simple and interactive Tkinter GUI
- Supports multiple languages (Hindi, French, German, Japanese, etc.)

---

##  Technologies & Libraries Used

- **Python 3.x**
- **Tkinter** – GUI framework
- **SpeechRecognition** – Voice input
- **Google Speech API** – Speech recognition backend
- **mtranslate** – Language translation
- **gTTS (Google Text-to-Speech)** – Speech synthesis
- **playsound** – Audio playback

---

##  Supported Languages (Sample)

| Language | Code |
|--------|------|
| English | en |
| Hindi | hi |
| French | fr |
| German | de |
| Spanish | es |
| Japanese | ja |
| Chinese | zh |
| Arabic | ar |
| Russian | ru |
| Korean | ko |
| Portuguese | pt |
| Turkish | tr |
| Zulu | zu |

> You can easily add more languages in the `languages` dictionary.

---

## Application Workflow

1. User speaks in English
2. Speech is converted to text
3. Text is translated to the target language
4. Translated text is converted to speech
5. Output text is displayed in the GUI

---

## Installation & Setup

### Clone the Repository
```bash
git clone https://github.com/your-username/voice-translator-python.git
cd voice-translator-python