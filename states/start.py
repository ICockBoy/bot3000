from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

from base.button import SuperButton
from base.keyboard import SuperKeyboard
from base.language import LanguageText
from base.state import SuperState
from base.text import SuperText


class Start:
    start_text = SuperText([LanguageText("en", "IDI NAHUI"),
                            LanguageText("ru", "Здарова заебал")])

    start_button1 = SuperButton(SuperText([LanguageText("en", "IDI NAHUI"),
                                           LanguageText("ru", "Здарова заебал")]),
                                callback_data="sex"
                                )
    start_button2 = InlineKeyboardButton(text="text", callback_data="self.callback_data")
    start_keyboard = SuperKeyboard([[start_button1], [start_button2]])
    start = SuperState(start_text,
                       start_keyboard)
