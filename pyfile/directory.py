from __future__ import annotations
from .systorage import Systorage
from .file import File
import os


class Directory(Systorage):

    __files: list[File]
    __directories: list[Directory]

    ### Implement logic for handling correctly 'recursive_load'

    def __init__(self, path: str, recursive_load: bool = False):
        super().__init__(path)
        if os.path.exists(path) and not os.path.isdir(path):
            raise Exception(f'"{path}" is not a folder')
        self.__load(recursive_load)

    def __get_sub_paths(self) -> list[str]:
        return list(
            map(
                lambda path: str(path),
                super().get_path_object().get_complex().glob("*"),
            )
        )

    def __bind_as_parent(self):
        for file in self.__files:
            file._parent = self
        for directory in self.__directories:
            directory._parent = self

    def __load_files(self, paths: list[str]):
        self.__files = list(
            map(
                lambda file_path: File(file_path),
                filter(lambda path: os.path.isfile(path), paths),
            )
        )

    def __load_directories(self, paths: list[str], recursive_load: bool):
        self.__directories = list(
            map(
                lambda folder_path: Directory(folder_path, recursive_load),
                filter(lambda path: os.path.isdir(path), paths),
            )
        )

    def __load(self, recursive_load: bool):
        child_paths = self.__get_sub_paths()
        self.__load_files(child_paths)
        self.__load_directories(child_paths, recursive_load)
        self.__bind_as_parent()

    def create(self) -> bool:
        super().get_path_object().get_complex().mkdir(parents=True, exist_ok=True)
        return self.exists()

    def delete(self, delete_all_content: bool = False) -> bool:
        # Implement clean each file by using self.get_files.
        os.rmdir(super().get_path_object().get_literal())
        return self.exists()

    def get_files(self):
        return self.__files

    def get_directories(self):
        return self.__directories

    def _update_metadata(self, path):
        pass

    def get_size(self):
        pass
