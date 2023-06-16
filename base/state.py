from aiogram.fsm.state import State
from aiogram.types import Message

from base.keyboard import SuperKeyboard
from base.text import SuperText


class SuperState:
    def __init__(self, text: SuperText, keyboard: SuperKeyboard):
        self.text = text
        self.keyboard = keyboard
        self.state = State()

    def __call__(self):
        return self.state

    async def answer(self, message: Message):
        language_code = message.from_user.language_code
        await message.answer(self.text.get(language_code), reply_markup=self.keyboard.get(language_code))



