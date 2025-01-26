from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, ChatMemberHandler
from services.telegram_bot_service import TelegramBotService
from telegram import Update

class TelegramBotController:
    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.telegram_bot_service = TelegramBotService()

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user_message = update.message.text
        response = self.telegram_bot_service.handle_user_message(user_message)
        await update.message.reply_text(response)

    def initialize_application(self):
        from telegram.ext import Application
        self.application = Application.builder().token(self.bot_token).build()
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        self.application.add_handler(ChatMemberHandler(self.new_member))

    def run(self):
        self.initialize_application()
        self.application.run_polling()

    async def new_member(self, update: Update, context):
        self.telegram_bot_service.new_member(update=update, context=context)