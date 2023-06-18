from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from base import default_language
from base.keyboard import SuperKeyboard
from base.text import SuperText


class SuperMessage:
    def __init__(self, text: SuperText, keyboard: SuperKeyboard):
        self.text = text
        self.keyboard = keyboard

    async def answer(self, message: Message, state: FSMContext, **kwargs):
        """
        format_text: format text *args
        format_button_callback_0: format number button callback
        format_button_text_0: format number button text
        format_button_url_0: format number button url
        :param message: message
        :param state: state
        :param kwargs: kwargs
        :return:
        """
        language = await self.get_text_from_language(message, state)
        format_text = None
        format_buttons_text = {}
        format_buttons_callback = {}
        format_buttons_url = {}
        if kwargs != {}:
            for key in kwargs.keys():
                if key == 'format_text':
                    format_text = kwargs[key]
                elif 'format_button_callback' in key:
                    format_buttons_callback[str(key.split("_")[-1])] = kwargs[key]
                elif 'format_button_text' in key:
                    format_buttons_text[str(key.split("_")[-1])] = kwargs[key]
                elif 'format_button_url' in key:
                    format_buttons_url[str(key.split("_")[-1])] = kwargs[key]
        await message.answer(text=self.text.get(language, format_text),
                             reply_markup=self.keyboard.get(language,
                                                            format_buttons_text,
                                                            format_buttons_callback,
                                                            format_buttons_url))

    async def reply(self, message: Message, state: FSMContext, **kwargs):
        """
        format_text: format text *args
        format_button_callback_0: format number button callback
        format_button_text_0: format number button text
        format_button_url_0: format number button url
        :param message: message
        :param state: state
        :param kwargs: kwargs
        :return:
        """
        language = await self.get_text_from_language(message, state)
        format_text = None
        format_buttons_text = {}
        format_buttons_callback = {}
        format_buttons_url = {}
        if kwargs != {}:
            for key in kwargs.keys():
                if key == 'format_text':
                    format_text = kwargs[key]
                elif 'format_button_callback' in key:
                    format_buttons_callback[str(key.split("_")[-1])] = kwargs[key]
                elif 'format_button_text' in key:
                    format_buttons_text[str(key.split("_")[-1])] = kwargs[key]
                elif 'format_button_url' in key:
                    format_buttons_url[str(key.split("_")[-1])] = kwargs[key]
        await message.reply(text=self.text.get(language, format_text),
                            reply_markup=self.keyboard.get(language,
                                                           format_buttons_text,
                                                           format_buttons_callback,
                                                           format_buttons_url))

    async def edit_markup(self, message: Message, state: FSMContext, **kwargs):
        """
        format_text: format text *args
        format_button_callback_0: format number button callback
        format_button_text_0: format number button text
        format_button_url_0: format number button url
        :param message: message
        :param state: state
        :param kwargs: kwargs
        :return:
        """
        language = await self.get_text_from_language(message, state)
        format_text = None
        format_buttons_text = {}
        format_buttons_callback = {}
        format_buttons_url = {}
        if kwargs != {}:
            for key in kwargs.keys():
                if key == 'format_text':
                    format_text = kwargs[key]
                elif 'format_button_callback' in key:
                    format_buttons_callback[str(key.split("_")[-1])] = kwargs[key]
                elif 'format_button_text' in key:
                    format_buttons_text[str(key.split("_")[-1])] = kwargs[key]
                elif 'format_button_url' in key:
                    format_buttons_url[str(key.split("_")[-1])] = kwargs[key]
        await message.edit_reply_markup(reply_markup=self.keyboard.get(language,
                                                                       format_buttons_text,
                                                                       format_buttons_callback,
                                                                       format_buttons_url))

    async def edit(self, message: Message, state: FSMContext, **kwargs):
        """
        format_text: format text *args
        format_button_callback_0: format number button callback
        format_button_text_0: format number button text
        format_button_url_0: format number button url
        :param message: message
        :param state: state
        :param kwargs: kwargs
        :return:
        """
        language = await self.get_text_from_language(message, state)
        format_text = None
        format_buttons_text = {}
        format_buttons_callback = {}
        format_buttons_url = {}
        if kwargs != {}:
            for key in kwargs.keys():
                if key == 'format_text':
                    format_text = kwargs[key]
                elif 'format_button_callback' in key:
                    format_buttons_callback[str(key.split("_")[-1])] = kwargs[key]
                elif 'format_button_text' in key:
                    format_buttons_text[str(key.split("_")[-1])] = kwargs[key]
                elif 'format_button_url' in key:
                    format_buttons_url[str(key.split("_")[-1])] = kwargs[key]
        try:
            await message.edit_text(text=self.text.get(language, format_text),
                                    reply_markup=self.keyboard.get(language,
                                                                   format_buttons_text,
                                                                   format_buttons_callback,
                                                                   format_buttons_url))
        except:
            pass

    @staticmethod
    async def get_text_from_language(message: Message, state: FSMContext) -> str:
        if message.from_user.language_code is not None:
            await state.update_data(language=message.from_user.language_code)
            return message.from_user.language_code
        else:
            if "language" not in (await state.get_data()):
                return default_language
            else:
                return (await state.get_data())["language"]
