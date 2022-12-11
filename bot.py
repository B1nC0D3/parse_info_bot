import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.types import BotCommand
from dotenv import load_dotenv

from handlers import commands, upload_file
from states.states import UploadFile

load_dotenv()


API_TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


def register_commands_handlers(dp: Dispatcher):
    dp.register_message_handler(
        commands.start,
        commands='start'
    )
    dp.register_message_handler(
        commands.help,
        commands='help'
    )
    dp.register_message_handler(
        commands.cancel,
        commands='cancel',
        state='*'
    )
    dp.register_message_handler(
        commands.upload,
        commands='upload'
    )
    dp.register_message_handler(
        commands.upload,
        Text(equals='Загрузить файл', ignore_case=True)
    )


def register_upload_file_handlers(dp: Dispatcher):
    dp.register_message_handler(
        upload_file.upload_file,
        state=UploadFile.waiting_for_file,
        content_types='document',
    )


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='/start', description='Запуск бота'),
        BotCommand(command='/help', description='Помощь'),
        BotCommand(command='/cancel', description='Отмена действия'),
        BotCommand(command='/upload', description='Загрузить файл'),
    ]
    await bot.set_my_commands(commands)


async def main():
    register_commands_handlers(dp)
    register_upload_file_handlers(dp)
    await set_commands(bot)

    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
