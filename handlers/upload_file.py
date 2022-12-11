import re

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from database import add_item
from parse_file import get_file_data


async def upload_file(message: Message, state: FSMContext):
    file_name = message.document.file_name
    if not re.match(r'.*.xls*', file_name):
        await message.answer('Загрузите Excel-файл')
        return
    await message.document.download(destination_file='documents/tmp.xls')
    try:
        file_data = get_file_data('documents/tmp.xls')
    except FileNotFoundError:
        await message.answer('Не удалось загрузить файл, попробуйте еще раз')
        return
    except KeyError:
        await message.answer('Файл не заполнен по шаблону либо он пуст')
        return
    name = file_data['name']
    url = file_data['URL']
    xpath = file_data['xpath']
    await message.answer('Вот содержимое файла:')
    for counter in range(len(name)):
        await message.answer(
            f'Имя: {name[counter]} \n'
            f'Ссылка: {url[counter]} \n'
            f'Xpath: {xpath[counter]} \n')
        add_item(name[counter], url[counter], xpath[counter])
