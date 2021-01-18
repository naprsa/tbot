import os
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admins = [
    "321136249",
]

IP = os.getenv("IP")

aiogram_redis = {"host": IP}

redis = {"address": (IP, 6379), "encoding": "utf8"}
