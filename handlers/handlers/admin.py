from aiogram.fsm.context import FSMContext

from states.broadcast import BroadcastState

from database.crud import get_all_users

from database.crud import get_stats
from aiogram.filters import Command
from keyboards.admin import admin_menu
from config import ADMIN_ID
from aiogram.filters import Command
from aiogram.types import Message

from config import ADMIN_ID
from database.crud import update_status
from aiogram.filters import Command

from database.crud import get_all_orders
@router.message(F.text == "📢 پیام همگانی")
async def broadcast_start(
    message: Message,
    state: FSMContext
):

    if message.from_user.id != ADMIN_ID:
        return


    await state.set_state(
        BroadcastState.waiting_message
    )


    await message.answer(
        "📢 متن پیام همگانی را ارسال کنید."
    )
@router.message(BroadcastState.waiting_message)
async def send_broadcast(
    message: Message,
    state: FSMContext
):

    if message.from_user.id != ADMIN_ID:
        return


    users = get_all_users()


    count = 0


    for user in users:

        try:

            await message.bot.send_message(
                user[0],
                message.text
            )

            count += 1

        except:

            pass


    await message.answer(
        f"""
✅ پیام ارسال شد.

👥 تعداد دریافت‌کنندگان:
{count}
"""
    )


    await state.clear()
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
@router.message(Command("done"))
async def done_order(message: Message):

    if message.from_user.id != ADMIN_ID:
        return


    try:

        order_id = int(
            message.text.split()[1]
        )

    except:

        await message.answer(
            "❌ فرمت درست:\n/done شماره سفارش"
        )

        return


    update_status(
        order_id,
        "انجام شده"
    )


    await message.answer(
        f"✅ سفارش {order_id} انجام شد."
    )@router.message(Command("pending"))
async def pending_order(message: Message):

    if message.from_user.id != ADMIN_ID:
        return


    try:

        order_id = int(
            message.text.split()[1]
        )

    except:

        await message.answer(
            "❌ فرمت درست:\n/pending شماره سفارش"
        )

        return


    update_status(
        order_id,
        "در انتظار"
    )


    await message.answer(
        f"⏳ سفارش {order_id} به حالت انتظار برگشت."
)
@router.message(Command("admin"))
async def admin_panel(message: Message):

    if message.from_user.id != ADMIN_ID:
        return


    await message.answer(
        """
🛠 پنل مدیریت کافی‌نت آنلاین

یکی از گزینه‌ها را انتخاب کنید:
        """,
        reply_markup=admin_menu()
    )
@router.message(F.text == "📊 آمار")
async def stats(message: Message):

    if message.from_user.id != ADMIN_ID:
        return


    orders, users, income = get_stats()


    await message.answer(
        f"""
📊 آمار کافی‌نت آنلاین

👥 کاربران:
{users}

📋 سفارش‌ها:
{orders}

💰 مجموع درآمد:
{income:,} تومان
"""
        )
