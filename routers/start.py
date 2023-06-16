from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

start = Router()


@start.message(Command("start"))
async def start_command(message: Message, state: FSMContext):
    await message.reply("Hello!")
