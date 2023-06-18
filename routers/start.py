from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from base import users
from states.start import Start

router = Router()


@router.message(Command("start"))
async def start_command(message: Message, state: FSMContext):
    await Start.start_message.reply(message, state, format_text=[message.from_user.first_name])
    user = users.user(message.chat.id)
    user.settings.pulls = "cum"
    user.save()


@router.callback_query(Text(Start.start_button1.callback_data))
async def start_command(callback: CallbackQuery, state: FSMContext):
    user = users.user(callback.message.chat.id)
    await Start.start_message.edit(callback.message,
                                        state,
                                        format_text=[user.settings.pulls])
