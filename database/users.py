from database.jsondb import JSONDATABASE


class Settings:
    pulls = ''

    def __init__(self, settings: dict):
        if 'pulls' in settings:
            self.pulls = settings['pulls']

    def dump(self):
        return {
            'pulls': self.pulls
        }


class User:
    settings: Settings = None

    def __init__(self, user_id: str, database: JSONDATABASE):
        self.user_id = user_id
        self.database = database
        user = self.database.get_field(user_id)
        if 'settings' in user:
            self.settings = Settings(user['settings'])
        else:
            self.settings = Settings({})

    def save(self):
        user = {
            'settings': self.settings.dump()
        }
        self.database.save_field(self.user_id, user)


class Users:
    def __init__(self):
        self.db = JSONDATABASE("database/static/users.json")

    def user(self, user_id: str | int):
        return User(str(user_id), self.db)
