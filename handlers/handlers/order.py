from database.crud import add_order
from config import ADMIN_ID
from database.crud import add_order
from config import ADMIN_ID
await message.bot.send_message(
    221048265,
    text
await message.bot.send_message(
    ADMIN_ID,
    text
)
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states import OrderState

router = Router()


@router.message(F.text == "📝 ثبت درخواست")
async def order_start(message: Message, state: FSMContext):

    await state.set_state(OrderState.full_name)

    await message.answer(
        "👤 لطفاً نام و نام خانوادگی خود را وارد کنید."
    )
@router.message(OrderState.full_name)
async def get_full_name(message: Message, state: FSMContext):

    await state.update_data(
        full_name=message.text
    )

    await state.set_state(
        OrderState.phone
    )

    await message.answer(
        "📱 شماره تماس خود را وارد کنید."
    )@router.message(OrderState.phone)
async def get_phone(message: Message, state: FSMContext):

    await state.update_data(
        phone=message.text
    )

    await state.set_state(
        OrderState.service
    )

    await message.answer(
        """
📋 نوع خدمت را وارد کنید.

مثال:

ثبت نام کنکور

یا

کارت ملی
"""
    )@router.message(OrderState.service)
async def get_service(message: Message, state: FSMContext):

    await state.update_data(
        service=message.text
    )

    await state.set_state(
        OrderState.description
    )

    await message.answer(
        "📝 توضیحات سفارش را بنویس."
    )@router.message(OrderState.description)
async def finish_order(message: Message, state: FSMContext):

    await state.update_data(
        description=message.text
    )

    data = await state.get_data()

    text = f"""
✅ سفارش جدید

👤 نام:
{data['full_name']}

📱 شماره:
{data['phone']}

📋 خدمت:
{data['service']}

📝 توضیحات:
{data['description']}
"""
order_id = add_order(
   message.from_user.id
    data["full_name"],
    data["phone"],
    data["service"],
    data["description"]
    )
    await message.answer(
        "✅ درخواست شما ثبت شد."
    )
order_id = add_order(

    data["full_name"],

    data["phone"],

    data["service"],

    data["description"]

    )
    await message.bot.send_message(
        221048265,
        text
    )
✅ سفارش جدید

🆔 کد سفارش:
{order_id}
    await state.clear()
await message.bot.send_message(
    ADMIN_ID,
    f"""
🆕 سفارش جدید

🆔 کد سفارش: {order_id}

👤 نام:
{data['full_name']}

📱 شماره:
{data['phone']}

📋 خدمت:
{data['service']}

📝 توضیحات:
{data['description']}

📌 وضعیت:
در انتظار
"""
)
await message.answer(
    f"""
✅ درخواست شما با موفقیت ثبت شد.

🆔 کد رهگیری شما:

{order_id}

این کد را نگه دارید.
"""
)
from database.crud import add_order
from config import ADMIN_ID
