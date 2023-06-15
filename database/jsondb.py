import json
import os
from json import JSONDecodeError
from typing import Any


class JSONDATABASE:
    def __init__(self, json_file: str, options="c"):
        """
        :param json_file: Path to json database file
        :param options: c:clear database, e:raise error, p:print error
        """
        self.filedb = json_file.replace("\\", "/")
        self.options = options
        if not os.path.isfile(self.filedb):
            if self.options == "c":
                if not os.path.exists("".join(self.filedb.split("/")[:-1])):
                    os.makedirs("".join(self.filedb.split("/")[:-1]))
            elif self.options == "e":
                raise FileNotFoundError
            elif self.options == "p":
                print(FileNotFoundError)

    @staticmethod
    def is_jsonable(x):
        try:
            json.loads(x)
            return True
        except JSONDecodeError:
            return False

    def find(self, attribute: str):
        pass

    def write(self, attributes: list[str], param: Any):
        with open(self.filedb, "w+") as filedb_stream:
            if not self.is_jsonable(filedb_stream.read()):
                if self.options == "c":
                    filedb_stream.write(json.dumps({}))
                elif self.options == "e":
                    raise JSONDecodeError
                elif self.options == "p":
                    print(JSONDecodeError)
            db = json.load(filedb_stream)


JSONDATABASE("static/database.json")
