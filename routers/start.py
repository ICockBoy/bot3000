from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states import start_state

start = Router()


@start.message(Command("start"))
async def start_command(message: Message, state: FSMContext):
    await start_state.start.answer(message)
