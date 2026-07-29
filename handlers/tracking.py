from aiogram import Router, F
from aiogram.types import Message

from database.crud import get_order

router = Router()


@router.message(F.text == "🔎 پیگیری سفارش")
async def tracking(message: Message):

    await message.answer(
        "لطفاً کد رهگیری سفارش را ارسال کنید."
    )
