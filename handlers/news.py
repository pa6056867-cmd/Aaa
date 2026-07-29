from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from services.news_service import get_news


router = Router()


@router.message(Command("news"))
async def news(message: Message):

    items = get_news()


    text = "📰 آخرین اخبار\n\n"


    for item in items:

        text += (
            f"🔹 {item['title']}\n"
            f"{item['link']}\n\n"
        )


    await message.answer(text)
