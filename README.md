# 🎙️ Python Voice Assistant

A smart, beginner-friendly Python Voice Assistant that interacts with users through voice commands. It can recognize speech, respond using text-to-speech, provide date and time information, search the web, check weather information, and answer general queries using an NLP-based chatbot.

## ✨ Features

- 🎤 **Voice Recognition:** Recognizes user commands using SpeechRecognition.
- 🔊 **Text-to-Speech:** Responds through voice using pyttsx3.
- 👋 **Greeting:** Responds to greetings such as Hello and Hi.
- 🕒 **Time and Date:** Provides the current time and date.
- 🌦️ **Weather Information:** Fetches weather details using the OpenWeatherMap API.
- 🔎 **Web Search:** Searches Google using voice commands.
- 🤖 **AI Chatbot:** Uses NLP and Machine Learning to generate responses.
- 🛑 **Exit Command:** Stops the assistant when the user says Stop or Exit.

## 🛠️ Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- Requests
- python-dotenv
- OpenWeatherMap API

## 📁 Project Structure

```text
Python-Voice-Assistant/
│
├── main.py
├── chatbot.py
├── wether.py
├── test_voice.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/PunitPatil1029/Python-Voice-Assistant.git
```

**2. Open the project folder**

```bash
cd Python-Voice-Assistant
```

**3. Create a virtual environment**

```bash
python -m venv .venv
```

**4. Activate the virtual environment**

Windows:

```bash
.venv\Scripts\activate
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

**6. Configure the weather API**

Create a `.env` file in the project folder and add your own OpenWeatherMap API key:

```env
WEATHER_API_KEY=your_api_key_here
```

Keep your `.env` file private. Never upload it to GitHub.

**7. Run the application**

```bash
python main.py
```

## 🚀 Project Status

Currently under development. More features and improvements may be added in future updates.

## 👨‍💻 Author

**Punit Patil**

GitHub: [PunitPatil1029](https://github.com/PunitPatil1029)

---

⭐ If you find this project interesting, consider giving it a star!