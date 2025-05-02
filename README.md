# Grocery Chatbot Powered by Gemini AI

This is a Telegram-based grocery chatbot that leverages Google's Gemini AI to interact with users, answer queries, and assist with grocery-related tasks.

## Features

- Natural language understanding using Gemini AI
- Telegram integration for real-time communication
- Easy setup and deployment

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/TMBTCOER/ideal-memory/tree/master
   cd grocery-chatbot

2.  For Windows
    ```bash
    python -m venv venv
    venv\Scripts\activate

3. **Install Dependencies

    ```bash
    pip install -r requirements.txt

4. **Configure environment variables:
   Create a .env file in the root directory with the following content:
    ```bash
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token
    GEMINI_API_KEY=your_gemini_api_key

5. **Run the bot

    ```bash
    python main.py
