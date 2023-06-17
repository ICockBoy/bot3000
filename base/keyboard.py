from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from base.button import SuperButton
from base.text import SuperText


class SuperKeyboard:
    def __init__(self,
                 buttons: list[list[SuperButton | InlineKeyboardButton | KeyboardButton]],
                 keyboard_type: str = "InlineKeyboardMarkup",
                 placeholder: None | SuperText = None):
        self.buttons = buttons
        self.keyboard_type = keyboard_type
        self.placeholder = placeholder

    def get(self,
            language_code,
            format_buttons_text=None,
            format_buttons_callback=None,
            format_buttons_url=None) -> InlineKeyboardMarkup | ReplyKeyboardMarkup:
        if format_buttons_text is None or format_buttons_text == {}:
            format_buttons_text = {}
        if format_buttons_callback is None or format_buttons_callback == {}:
            format_buttons_callback = {}
        if format_buttons_url is None or format_buttons_url == {}:
            format_buttons_url = {}
        i = 0
        if self.keyboard_type == "InlineKeyboardMarkup":
            keyboard = InlineKeyboardBuilder()
            for keyboard_row in self.buttons:
                buttons = []
                for button in keyboard_row:
                    if type(button) == InlineKeyboardButton:
                        buttons.append(button)
                    else:
                        format_button_text = format_buttons_text[str(i)] if str(i) in format_buttons_text else None
                        format_button_callback = format_buttons_callback[str(i)] if str(
                            i) in format_buttons_callback else None
                        format_button_url = format_buttons_url[str(i)] if str(i) in format_buttons_url else None
                        buttons.append(button.get(language_code,
                                                  format_button_text,
                                                  format_button_callback,
                                                  format_button_url))
                    i += 1
                keyboard.row(*buttons)
            return keyboard.as_markup()
        else:
            kb = []
            for keyboard_row in self.buttons:
                buttons = []
                for button in keyboard_row:
                    if type(button) == KeyboardButton:
                        buttons.append(button)
                    else:
                        format_button_text = format_buttons_text[str(i)] if str(i) in format_buttons_text else None
                        format_button_callback = format_buttons_callback[str(i)] if str(
                            i) in format_buttons_callback else None
                        format_button_url = format_buttons_url[str(i)] if str(i) in format_buttons_url else None
                        buttons.append(button.get(language_code,
                                                  format_button_text,
                                                  format_button_callback,
                                                  format_button_url))
                    i += 1
                kb.append(buttons)
            return ReplyKeyboardMarkup(
                keyboard=kb,
                resize_keyboard=True,
                input_field_placeholder=self.placeholder.get(language_code)
            )
