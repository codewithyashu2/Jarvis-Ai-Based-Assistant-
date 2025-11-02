# 🤖 JARVIS - Advanced AI Voice Assistant

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

A powerful, feature-rich AI voice assistant built with Python that can perform various tasks through voice commands. Inspired by Iron Man's JARVIS!

## ✨ Features

### 🤖 AI Brain
- Intelligent conversations using OpenAI API
- Context-aware responses
- Fallback mode for basic queries

### 📧 Communication
- WhatsApp integration
- Email management
- Quick message sending

### 💻 Advanced Computer Control
- System information (CPU, RAM, Battery)
- Screen brightness control
- File and folder management
- System shutdown/restart
- Screenshot capabilities

### 📊 Information & Updates
- Real-time stock prices
- Cryptocurrency prices
- Latest news headlines (general & tech)
- Language translation
- Weather updates

### 📚 Learning & Knowledge
- Math problem solver
- Word definitions
- Wikipedia integration
- Study timer (Pomodoro technique)

### 🎮 Fun Features
- Random jokes
- Motivational quotes
- Fun facts
- Number guessing game
- Coin flip & dice roll

### 🌐 Web Integration
- Google search
- YouTube search and playback
- Quick website access
- Web browsing automation

## 🎥 Demo

> Add a demo GIF or video here showcasing your assistant in action!

## 📋 Prerequisites

- Python 3.8 or higher
- Windows OS (for full functionality)
- Microphone for voice input
- Internet connection

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/jarvis-ai-assistant.git
cd jarvis-ai-assistant
```

### 2. Install required packages

```bash
pip install -r requirements.txt
```

### 3. Additional setup for Windows

```bash
pip install pywin32
pip install screen-brightness-control
```

## ⚙️ Configuration

### API Keys (Optional but Recommended)

1. **OpenWeather API** (for weather features)
   - Get free API key from [OpenWeatherMap](https://openweathermap.org/api)
   - Add to `jarvis.py`: `self.WEATHER_API_KEY = "your_key"`

2. **News API** (for news features)
   - Get free API key from [NewsAPI](https://newsapi.org/)
   - Add to `jarvis.py`: `self.NEWS_API_KEY = "your_key"`

3. **OpenAI API** (for AI brain features)
   - Get API key from [OpenAI](https://platform.openai.com/api-keys)
   - Add to `jarvis.py`: `self.OPENAI_API_KEY = "your_key"`

**Note:** The assistant works without API keys, but with limited features.

## 🎯 Usage

### Starting Jarvis

```bash
python jarvis.py
```

### Voice Commands Examples

#### Basic Commands
```
"What time is it"
"What's the date"
"Tell me a joke"
"Take a screenshot"
```

#### AI & Intelligence
```
"Ask what is machine learning"
"Define artificial intelligence"
"Solve 25 plus 37"
```

#### Computer Control
```
"System info"
"Brightness 70"
"Open downloads"
"Shutdown"
```

#### Information
```
"Weather in New York"
"Stock price AAPL"
"Crypto price bitcoin"
"Tech news"
```

#### Fun
```
"Motivate me"
"Fun fact"
"Play game"
"Flip coin"
```

#### Web & Search
```
"Search Google for Python tutorials"
"Open YouTube"
"Wikipedia artificial intelligence"
```

### Exiting
Say: `"Exit"`, `"Quit"`, or `"Goodbye"`

Or press: `Ctrl + C`

## 📁 Project Structure

```
jarvis-ai-assistant/
│
├── jarvis.py              # Main assistant code
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── LICENSE               # License file
├── .gitignore            # Git ignore file
│
├── screenshots/          # Screenshots for documentation
│   └── demo.gif
│
└── docs/                 # Additional documentation
    ├── INSTALLATION.md
    ├── COMMANDS.md
    └── API_SETUP.md
```

## 🛠️ Tech Stack

- **Python 3.8+**
- **SpeechRecognition** - Voice input
- **pyttsx3 / win32com** - Text-to-speech
- **psutil** - System monitoring
- **requests** - API calls
- **wikipedia-api** - Wikipedia integration
- **pyautogui** - Screenshot & automation
- **pyjokes** - Joke generation

## 🔧 Troubleshooting

### Microphone not working
- Check microphone permissions in Windows Settings
- Ensure microphone is set as default recording device

### Speech recognition not working
- Check internet connection (Google Speech API requires internet)
- Speak clearly and closer to the microphone

### PyAudio installation fails
```bash
pip install pipwin
pipwin install pyaudio
```

### Text-to-speech not working
- Ensure Windows SAPI is enabled
- Try reinstalling pywin32: `pip install --upgrade pywin32`

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Ideas for Contribution
- Add more voice commands
- Improve speech recognition accuracy
- Add support for other languages
- Create a GUI interface
- Add more integrations (Spotify, Smart Home, etc.)

## 📝 To-Do

- [ ] Add Spotify integration
- [ ] Support for multiple languages
- [ ] Create GUI interface
- [ ] Add reminder/alarm functionality
- [ ] Integrate with smart home devices
- [ ] Add voice customization options
- [ ] Create mobile app version
- [ ] Add conversation history logging

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Inspired by Iron Man's JARVIS
- Thanks to all open-source contributors
- Built with ❤️ using Python

## ⭐ Star History

If you find this project useful, please consider giving it a star!

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/jarvis-ai-assistant&type=Date)](https://star-history.com/#yourusername/jarvis-ai-assistant&Date)

## 📞 Support

If you have any questions or need help, feel free to:
- Open an [issue](https://github.com/yourusername/jarvis-ai-assistant/issues)
- Start a [discussion](https://github.com/yourusername/jarvis-ai-assistant/discussions)
- Contact me via email

---

**Made with 💙 by [Your Name]**

*Don't forget to ⭐ this repo if you found it helpful!*
