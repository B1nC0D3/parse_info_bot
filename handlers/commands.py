from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from keys.keys import keyboard
from states.states import UploadFile


async def start(message: Message):
    await message.answer(
        'Это бот записывающий информацию '
        'из Excel-документа в базу данных, '
        'для отправки файла выполните /upload',
        reply_markup=keyboard)


async def help(message: Message):
    await message.answer(
        '/start - стартовое сообщение бота \n'
        '/upload - загрузить файл для выгрузки его содержимого в бд'
    )


async def cancel(message: Message, state: FSMContext):
    await state.finish()
    await message.answer('Отменено')


async def upload(message: Message, state: FSMContext):
    await state.set_state(UploadFile.waiting_for_file.state)
    await message.answer('Отправьте эксель файл в формате: '
                         'name, URL, xpath')
