import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("Не вдалося знайти токен в файлі .env. Перевірте, чи існує BOT_TOKEN.")

import logging

def log_message(func):
    def wrapper(message, *args, **kwargs):
        logging.info(f"Отримано повідомлення від {message.chat.id}: {message.text}")
        return func(message, *args, **kwargs)
    return wrapper
