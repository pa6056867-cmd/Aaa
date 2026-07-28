from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "📝 ثبت درخواست")
async def request(message: Message):

    await message.answer(
"""
📝 ثبت درخواست

لطفاً اطلاعات زیر را برای مدیر ارسال کنید:

👤 نام و نام خانوادگی

📱 شماره تماس

📄 نوع خدمت

📝 توضیحات

📎 در صورت نیاز عکس یا فایل را هم ارسال کنید.
"""
  
    )
  
