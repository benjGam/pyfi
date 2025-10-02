from __future__ import annotations
from .systorage import Systorage
from .file import File
import os


class Directory(Systorage):

    __files: list[File]
    __directories: list[Directory]

    def __init__(self, path, recursive_load: bool = False):
        super().__init__(path)
        if not os.path.isfile(path):
            raise Exception(f'"{path}" is not a folder')

    def __bind_files_parent(self):
        for file in self.__files:
            file.__parent = self

    def __load(self, recursive_load: bool):
        complex_path = self.__path.get_complex()
        child_paths = complex_path.glob("*")
        self.__files = list(filter(lambda path: os.path.isfile(path), child_paths))
        self.__bind_files_parent()
        self.__directories = list(filter(lambda path: os.path.isdir(path), child_paths))
        if recursive_load:
            for directory in self.__directories:
                directory.__load(recursive_load)

    def create(self) -> bool:
        self.__path.get_complex().mkdir(parents=True, exist_ok=True)
        return self.exists()

    def delete(self, delete_all_content: bool = False) -> bool:
        # Implement clean each file by using self.get_files.
        os.rmdir(self.__path.get_literal())
        return self.exists()
