from aiogram.utils.keyboard import ReplyKeyboardBuilder

def main_menu():

    kb = ReplyKeyboardBuilder()

    kb.button(text="📝 ثبت درخواست")

    kb.button(text="📋 خدمات")

    kb.button(text="📞 ارتباط با مدیر")

    kb.button(text="ℹ️ درباره ما")
kb.button(text="🔎 پیگیری سفارش")
    kb.adjust(2)

    return kb.as_markup(
        resize_keyboard=True
    )
