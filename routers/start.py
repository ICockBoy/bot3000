from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states import start_state

start = Router()


@start.message(Command("start"))
async def start_command(message: Message, state: FSMContext):
    await start_state.start_message.answer(message,
                                           state,
                                           format_text=[message.from_user.first_name],
                                           format_button_text_0=["нахуй"])
