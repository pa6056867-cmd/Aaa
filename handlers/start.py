from keyboards.main_menu import main_menu
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
    await message.await message.answer(
    """
🌹 سلام، به کافی‌نت آنلاین خوش اومدی.

لطفاً یکی از گزینه‌های زیر رو انتخاب کن.
""",
    reply_markup=main_menu()
    )

