from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from base.config import token
from routers import import_routers

memory_storage = MemoryStorage()
bot = Bot(token=token, parse_mode="HTML")
dp = Dispatcher(storage=memory_storage)


async def start():
    print("bot started!")
    import_routers(dp)
    await dp.start_polling(bot)
