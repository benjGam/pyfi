from .systorage import Systorage
import os


class File(Systorage):

    def __init__(self, path: str):
        super().__init__(path)
        if not os.path.isfile(path):
            raise Exception(f'"{path}" is not a file')
        # Logic to bind to parent

    def create(self):
        self.__path.get_complex().touch(exist_ok=True)
        return self.exists()

    def append(self, content: str):
        with open(self.__path.get_literal(), "a") as f:
            f.write(content)
