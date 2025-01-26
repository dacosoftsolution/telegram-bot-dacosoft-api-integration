from controllers.telegram_bot_controller import TelegramBotController
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def main():
    bot_token = getenv("TELEGRAM_API_KEY")
    bot_controller = TelegramBotController(bot_token)
    bot_controller.run()

if __name__ == "__main__":
    main()