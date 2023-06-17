from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from base.button import SuperButton
from base.text import SuperText


class SuperKeyboard:
    def __init__(self,
                 buttons: list[list[SuperButton | InlineKeyboardMarkup]],
                 keyboard_type: str = "InlineKeyboardMarkup",
                 placeholder: None | SuperText = None):
        self.buttons = buttons
        self.keyboard_type = keyboard_type
        self.placeholder = placeholder

    def get(self, language_code) -> InlineKeyboardMarkup | ReplyKeyboardMarkup:
        if self.keyboard_type == "InlineKeyboardMarkup":
            keyboard = InlineKeyboardBuilder()
            for keyboard_row in self.buttons:
                buttons = []
                for button in keyboard_row:
                    if type(button) == InlineKeyboardButton:
                        buttons.append(button)
                    else:
                        buttons.append(button.get_button(language_code))
                keyboard.row(*buttons)
            return keyboard.as_markup()
        else:
            kb = []
            for keyboard_row in self.buttons:
                buttons = []
                for button in keyboard_row:
                    buttons.append(button.get_button(language_code))
                kb.append(buttons)
            return ReplyKeyboardMarkup(
                keyboard=kb,
                resize_keyboard=True,
                input_field_placeholder=self.placeholder.get(language_code)
            )
