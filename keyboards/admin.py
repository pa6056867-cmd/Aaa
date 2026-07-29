from aiogram.utils.keyboard import InlineKeyboardBuilder

def admin_panel():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🆕 سفارش‌های جدید",
        callback_data="new_orders"
    )

    kb.button(
        text="📋 همه سفارش‌ها",
        callback_data="all_orders"
    )

    kb.button(
        text="💰 حسابداری",
        callback_data="money"
    )

    kb.button(
        text="📢 اخبار",
        callback_data="news"
    )

    kb.button(
        text="📨 پیام همگانی",
        callback_data="broadcast"
    )

    kb.adjust(2)

    return kb.as_markup()
