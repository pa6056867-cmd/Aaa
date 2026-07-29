from aiogram.fsm.state import State, StatesGroup


class TrackingState(StatesGroup):

    waiting_order_id = State()
