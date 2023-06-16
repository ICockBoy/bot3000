from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from base.button import SuperButton


class SuperKeyboard:
    def __init__(self,
                 buttons: list[list[SuperButton]],
                 keyboard_type: InlineKeyboardBuilder | ReplyKeyboardBuilder = InlineKeyboardMarkup):
        self.buttons = buttons
        self.keyboard_type = keyboard_type

    def get(self, language_code) -> InlineKeyboardBuilder | ReplyKeyboardMarkup:
        if self.keyboard_type == InlineKeyboardMarkup:
            keyboard = InlineKeyboardBuilder()
            for keyboard_row in self.buttons:
                buttons = []
                for button in keyboard_row:
                    buttons.append(button.get_button(language_code))
                keyboard.row(keyboard_row)
            return keyboard.as_markup()
        else:
            keyboard = ReplyKeyboardBuilder()
            for keyboard_row in self.buttons:
                buttons = []
                for button in keyboard_row:
                    buttons.append(button.get_button(language_code))
                keyboard.row(keyboard_row)
            return keyboard.as_markup()
