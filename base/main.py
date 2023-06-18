from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from base.config import token
from database.users import Users

users = Users()
memory_storage = MemoryStorage()
bot = Bot(token=token, parse_mode="HTML")
dp = Dispatcher(storage=memory_storage)



