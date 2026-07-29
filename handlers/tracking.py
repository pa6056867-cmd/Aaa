from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.tracking import TrackingState
from database.crud import get_order

router = Router()


@router.message(F.text == "🔎 پیگیری سفارش")
async def tracking(message: Message, state: FSMContext):

    await state.set_state(
        TrackingState.waiting_order_id
    )

    await message.answer(
        "🆔 کد رهگیری را وارد کنید."
    )


@router.message(TrackingState.waiting_order_id)
async def show_order(message: Message, state: FSMContext):

    if not message.text.isdigit():

        await message.answer(
            "❌ فقط عدد وارد کنید."
        )

        return

    order = get_order(
        int(message.text)
    )

    if order is None:

        await message.answer(
            "❌ سفارشی پیدا نشد."
        )

        await state.clear()

        return

    await message.answer(
        f"""
🆔 کد سفارش: {order[0]}

👤 نام:
{order[1]}

📱 شماره:
{order[2]}

📋 خدمت:
{order[3]}

📝 توضیحات:
{order[4]}

📌 وضعیت:
{order[5]}
"""
    )

    await state.clear()
