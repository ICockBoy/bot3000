from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

from base.button import SuperButton
from base.keyboard import SuperKeyboard
from base.language import LanguageText
from base.message import SuperMessage
from base.text import SuperText


class Start:
    start_text = SuperText([LanguageText("en", "Hello there, {}!"),
                            LanguageText("ru", "Приветствую тебя, {}!")])

    start_button1 = SuperButton(SuperText([LanguageText("en", "IDI NAHUI {}"),
                                           LanguageText("ru", "Здарова заебал {}")]),
                                callback_data="sex")
    start_button2 = InlineKeyboardButton(text="text", callback_data="self.callback_data")
    start_keyboard = SuperKeyboard([[start_button1], [start_button2]])
    start_message = SuperMessage(start_text, start_keyboard)
