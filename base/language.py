class LanguageText:
    def __init__(self, language_code: str, text: str):
        self.language_code = language_code
        self.text = text

    def get_language(self) -> str:
        return self.language_code

    def get_text(self) -> str:
        return self.text
