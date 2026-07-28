cafinet-online-bot
│
├── bot.py
├── config.py
├── requirements.txt
└── handlers
    └── start.py
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🌹 سلام!\n"
        "به ربات «کافی‌نت آنلاین» خوش اومدی.\n\n"
        "برای استفاده از خدمات، از منوی ربات استفاده کن."
    )
