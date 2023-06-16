from aiogram.types import KeyboardButton, InlineKeyboardButton

from base.text import SuperText


class SuperButton:
    def __init__(self,
                 text: SuperText,
                 button_type: InlineKeyboardButton | KeyboardButton = InlineKeyboardButton,
                 callback_data: None | str = None,
                 url: None | str = None, **kwargs):
        """

        :param languages_text:
        :param button_type: InlineKeyboardButton or KeyboardButton
        :param callback_data: any data
        :param url: any url
        """
        self.text = text
        self.button_type = button_type
        self.callback_data = callback_data
        self.url = url
        self.kwargs = kwargs

    def get_button(self, language_code):
        text = self.text.get(language_code)
        if self.button_type == InlineKeyboardButton:
            if self.callback_data is not None:
                return InlineKeyboardButton(text=text, callback_data=self.callback_data)
            elif self.url is not None:
                return InlineKeyboardButton(text=text, callback_data=self.url)
        else:
            return KeyboardButton(text=text)
