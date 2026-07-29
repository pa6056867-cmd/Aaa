from aiogram.filters import Command

from database.crud import get_all_orders


@router.message(Command("orders"))
async def orders(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    orders = get_all_orders()

    if not orders:

        await message.answer("هیچ سفارشی ثبت نشده است.")

        return

    text = "📋 لیست سفارش‌ها\n\n"

    for order in orders:

        text += (
            f"🆔 {order[0]}\n"
            f"👤 {order[1]}\n"
            f"📋 {order[2]}\n"
            f"📌 {order[3]}\n\n"
        )

    await message.answer(text)
