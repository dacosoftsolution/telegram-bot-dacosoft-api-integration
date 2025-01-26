import requests
from langdetect import detect
from os import getenv
from dotenv import load_dotenv
from logging import Logger

load_dotenv()

class ChatAPIService:
    API_URL = 'https://dacosoft.pro/api/chat-call'
    API_KEY = getenv("DACOSOFT_SOLUTION_API_KEY")
    ASSISTANT_ID = getenv("DACOSOFT_SOLUTION_ROBOT_ID")

    @staticmethod
    def make_request(message):
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': ChatAPIService.API_KEY
        }
        payload = {
            'assistant_id': ChatAPIService.ASSISTANT_ID,
            'messages': message,
            'lang': detect(message)
        }
        try:
            response = requests.post(ChatAPIService.API_URL, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger = Logger.setup_logging()
            logger.error(f'Error making request: {e}')
            return None