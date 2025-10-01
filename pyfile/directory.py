from __future__ import annotations
from .systorage import Systorage
from .file import File
import os


class Directory(Systorage):

    __files: list[File]
    __directories: list[Directory]

    def __init__(self, path):
        super().__init__(path)
        if not os.path.isfile(path):
            raise Exception(f'"{path}" is not a folder')

    def create(self) -> bool:
        self.__path.get_complex().mkdir(parents=True, exist_ok=True)
        return self.exists()

    def delete(self, delete_all_content: bool = False) -> bool:
        # Implement clean each file by using self.get_files.
        os.rmdir(self.__path.get_literal())
        return self.exists()
