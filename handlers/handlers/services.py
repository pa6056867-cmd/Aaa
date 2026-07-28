from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "📋 خدمات")
async def services(message: Message):

    await message.answer(
"""
🌐 خدمات کافی‌نت آنلاین

🎓 ثبت‌نام کنکور
📝 ثبت‌نام آزمون استخدامی
🏦 خدمات بانکی
🪪 کارت ملی هوشمند
🛂 گذرنامه
🚗 تعویض پلاک
📄 تایپ و ترجمه
🖨 پرینت و اسکن
📧 ساخت ایمیل
💳 ثبت‌نام سامانه‌های دولتی

برای ثبت درخواست روی
📝 ثبت درخواست
بزن.
"""
    )
