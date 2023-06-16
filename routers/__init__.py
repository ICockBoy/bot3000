from aiogram import Dispatcher

from routers.start import start


def import_routers(dp: Dispatcher):
    dp.include_router(start)
