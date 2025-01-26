from controllers.chat_api_controller import ChatAPIController
from telegram import Update

class TelegramBotService:
    def __init__(self):
        self.chat_api_controller = ChatAPIController()

    def handle_user_message(self, user_message):
        return self.chat_api_controller.process_message(user_message)
        
    @staticmethod
    async def new_member(self, update: Update, context):
        for member in update.chat_members:
            if member.new_chat_member:
                new_user = member.new_chat_member
                if new_user.is_bot:
                    return

                welcome_message = "Hello! Welcome to the group!"

                await update.chat.send_message(welcome_message)