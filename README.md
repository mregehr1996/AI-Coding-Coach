# AI Coding Coach

AI Coding Coach is a beginner-friendly Python app that helps users explain code, check bugs, get code feedback, generate quizzes, and ask general coding questions using the Google Gemini API.

## Features

- Explain pasted code
- Check code for bugs
- Get improvement feedback
- Generate programming quizzes
- Ask general coding questions
- Organized modular Python file structure

## Project Structure

```text
ai-coding-coach/
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
└── ai_coding_coach/
    ├── __init__.py
    ├── ai_client.py
    ├── bug_checker.py
    ├── code_explainer.py
    ├── feedback_engine.py
    └── quiz_generator.py
```

## Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

Mac or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Copy `.env.example` and rename it to `.env`.

Inside `.env`, add your Gemini API key:

```text
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.0-flash
```

### 5. Run the app

```bash
python main.py
```

## Resume Bullet

Built an AI-powered coding coach using Python and the Google Gemini API that explains code, checks for bugs, gives code feedback, and generates programming quizzes through a command-line interface.

## Future Improvements

- Add Flask web version
- Add SQLite database storage
- Add login accounts
- Save user questions and AI responses
- Add GitHub code review integration
