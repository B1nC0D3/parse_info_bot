from aiogram.dispatcher.filters.state import State, StatesGroup


class UploadFile(StatesGroup):
    waiting_for_file = State()
