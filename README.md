# 🎯 Interview Coach

An AI-powered interview preparation tool that helps you practice technical interviews with personalized questions based on your job description and experience level.

## ✨ Features

- **AI-Powered Questions**: Get realistic technical interview questions tailored to your position
- **Customizable Interviews**: Specify job type, experience level, and focus areas
- **Conversation Memory**: System remembers previous answers for context-aware follow-ups
- **Local LLM Support**: Uses Ollama for fast, private inference—no external API calls needed
- **Interactive Interface**: Real-time feedback and conversation history

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai) installed and running
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Somu9966/Interview_Coach.git
   cd Interview_Coach
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and set your model:
   ```
   MODEL=llama2
   ```

### Running the Interview Coach

```bash
python3 main.py
```

Follow the interactive prompts to start your interview practice session.

## 📋 Configuration

Edit the `config` dictionary in `main.py` to customize your interview:

```python
config = {
    "interview_type": "technical Python",
    "level": "senior",
    "focus_area": "Python fundamentals and design patterns",
}
```

Available levels: `junior`, `mid`, `senior`, `lead`

## 📁 Project Structure

```
interview-coach/
├── main.py                 # Entry point
├── chains/
│   └── interviewer.py      # Interview chain logic
├── memory/
│   └── conversation.py     # Conversation memory management
├── README.md
├── requirements.txt
└── .env                    # Environment variables (create this)
```

## 🛠 Technologies Used

- **LangChain**: LLM orchestration and prompt management
- **Ollama**: Local language model inference
- **LangChain Core**: Chat history and runnable chains
- **Python 3.12+**: Language

## 📝 Common Commands

| Command | Purpose |
|---------|---------|
| `python3 main.py` | Start interview session |
| `git push` | Push changes to GitHub |
| `pip install -r requirements.txt` | Install dependencies |

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## ⚙️ Troubleshooting

**"Model not found" error?**
```bash
ollama pull llama2  # or your preferred model
```

**Module import errors?**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 📞 Support

For issues or questions, open a GitHub issue or contact the maintainers.

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.
