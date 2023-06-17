from aiogram.types import KeyboardButton, InlineKeyboardButton

from base.text import SuperText


class SuperButton:
    def __init__(self,
                 text: SuperText,
                 button_type: str = "InlineKeyboardButton",
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

    def get(self, language_code, format_text=None, format_callback=None, format_url=None):
        text = self.text.get(language_code)
        callback_data = self.callback_data
        url = self.url
        if format_text is not None:
            text = text.format(*format_text)
        if format_callback is not None:
            callback_data = callback_data.format(*format_callback)
        if format_url is not None:
            url = url.format(*format_url)
        if self.button_type == "InlineKeyboardButton":
            if self.callback_data is not None:
                return InlineKeyboardButton(text=text, callback_data=callback_data)
            elif self.url is not None:
                return InlineKeyboardButton(text=text, url=url)
            else:
                raise "NoFunctions"
        else:
            return KeyboardButton(text=text)
