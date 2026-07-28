import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

ADMIN_ID = int(os.getenv("ADMIN_ID", 221048265))

CHANNEL_USERNAME = os.getenv(
    "CHANNEL_USERNAME",
    "@cafinet_online"
)

BOT_NAME = "کافی‌نت آنلاین"
