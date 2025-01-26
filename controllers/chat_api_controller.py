from services.chat_api_service import ChatAPIService
from utils.logger import Logger

class ChatAPIController:
    def __init__(self):
        self.chat_api_service = ChatAPIService()
        self.logger = Logger.setup_logging()

    def process_message(self, message):
        api_response = self.chat_api_service.make_request(message)
        if api_response:
            return api_response.get('result', 'Sorry! Can you say again?')
        else:
            self.logger.error("Failed to get response from chat API.")
            return "Error processing the request."

    async def new_member(self):
        await self.chat_api_service.new_member()