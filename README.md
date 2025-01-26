# Telegram Bot

A modular Telegram bot built with Python that processes user messages using an external chat API and sends welcome messages to new group members.

## Features
- Responds to user messages using an external chat API.
- Sends welcome messages to new group members.
- Modular service and controller architecture.
- Basic error logging.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/telegram-bot.git
    cd telegram-bot
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables in `.env`:
    ```env
    TELEGRAM_BOT_API_KEY=your-telegram-bot-api-key
    CHAT_API_KEY=your-chat-api-key
    ASSISTANT_ID=your-assistant-id
    ```

4. (Optional) Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

## Usage

Run the bot:
```bash
python main.py
```

## File Strucutre
<br />
telegram-bot/ <br />
├── controllers/ <br />
│ └── chat_api_controller.py <br />
├── services/ <br />
│ └── chat_api_service.py <br />
│ └── telegram_bot_service.py <br />
├── utils/ <br />
│ └── logger.py <br />
├── .env <br />
├── main.py <br />
├── requirements.txt <br />
└── README.md <br />

## LICENCE

This project is licensed under the MIT License. This version keeps the main points clear and concise while omitting unnecessary details.