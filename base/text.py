from base import default_language
from base.language import LanguageText


class SuperText:
    def __init__(self, languages_text: list[LanguageText]):
        self.languages_text = languages_text

    def get(self, language_code, format_text=None):
        for language_text in self.languages_text:
            if language_text.get_language() == language_code:
                if format_text is None:
                    return language_text.get_text()
                else:
                    return language_text.get_text().format(*format_text)
                break
        else:
            for language_text in self.languages_text:
                if language_text.get_language() == default_language:
                    if format_text is None:
                        return language_text.get_text()
                    else:
                        return language_text.get_text().format(*format_text)
                    break
            else:
                raise "NoLanguage"
