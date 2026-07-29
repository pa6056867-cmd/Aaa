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
