from aiogram.fsm.state import State, StatesGroup


class OrderState(StatesGroup):

    full_name = State()

    phone = State()

    service = State()

    description = State()
