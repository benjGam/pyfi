from .systorage import Systorage
import os


class File(Systorage):

    def __init__(self, path: str):
        super().__init__(path)
        if not os.path.isfile(path):
            raise Exception(f'"{path}" is not a file')
        # Logic to bind to parent

    def create(self) -> bool:
        self.__path.get_complex().touch(exist_ok=True)
        return self.exists()

    def append(self, content: str):
        with open(self.__path.get_literal(), "a") as f:
            f.write(content)

    def write(self, content: str):
        with open(self.__path.get_literal(), "w") as f:
            f.write(content)

    def read_to_end(self) -> str:
        file_content: str
        with open(self.__path.get_literal(), "r") as f:
            f.seek(0)
            file_content = f.read()
        return file_content

    def delete_content(self):
        self.write("")
        return os.path.getsize(self.__path.get_literal()) == 0
