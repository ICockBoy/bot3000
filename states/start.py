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
                                KeyboardButton)
    start_keyboard = SuperKeyboard([[start_button1]], ReplyKeyboardMarkup)
    start = SuperState(start_text,
                       start_keyboard)
