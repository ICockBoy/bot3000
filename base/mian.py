from aiogram import Bot, Dispatcher, executor, types

from base.config import token

bot = Bot(token=token)
dp = Dispatcher(bot)


def start():
    executor.start_polling(dp, skip_updates=True)
