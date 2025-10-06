from __future__ import annotations
from .systorage import Systorage
import os
import pyfile


class Directory(Systorage):

    __files: list[pyfile.File] = []
    __directories: list[Directory] = []

    ### Implement logic for handling correctly 'recursive_load'

    def __init__(self, path: str, auto_load: bool = True, recursive_load: bool = False):
        super().__init__(path)
        if os.path.exists(path) and not os.path.isdir(path):
            raise Exception(f'"{path}" is not a folder')
        if auto_load:
            self.load(auto_load, recursive_load)

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
                lambda file_path: pyfile.File(file_path),
                filter(lambda path: os.path.isfile(path), paths),
            )
        )

    def __load_directories(
        self, paths: list[str], auto_load: bool, recursive_load: bool
    ):
        self.__directories = list(
            map(
                lambda folder_path: Directory(folder_path, auto_load, recursive_load),
                filter(lambda path: os.path.isdir(path), paths),
            )
        )

    def load(self, auto_load: bool, recursive_load: bool):
        child_paths = self.__get_sub_paths()
        self.__load_files(child_paths)
        if recursive_load:
            self.__load_directories(child_paths, auto_load, recursive_load)
        self.__bind_as_parent()

    def create(self) -> bool:
        super().get_path_object().get_complex().mkdir(parents=True, exist_ok=True)
        return self.exists()

    def delete(self, delete_all_content: bool = False) -> bool:
        # Implement clean each file by using self.get_files.
        os.rmdir(super().get_path_object().get_literal())
        return self.exists()

    def __get_files_by_extensions(
        self, file_list: list[pyfile.File], extensions: list[str]
    ) -> list[pyfile.File]:

        return list(filter(lambda file: file.get_extension() in extensions, file_list))

    def __get_files_recursively(self) -> list[pyfile.File]:
        to_return = self.__files
        for directory in self.__directories:
            to_return.extend(directory.__get_files_recursively())
        return to_return

    def __group_by_parent(
        self, elem_list: list[pyfile.File] | list[Directory]
    ) -> list[pyfile.SegmentedSearchResult]:
        segmented_elem_list: list[pyfile.SegmentedSearchResult] = []

        for elem in elem_list:
            parent = elem.get_parent()
            existing_segment = next(
                (seg for seg in segmented_elem_list if seg.parent == parent), None
            )
            if existing_segment:
                existing_segment.childs.append(elem)
            else:
                segmented_elem_list.append(pyfile.SegmentedSearchResult(parent, [elem]))
        return segmented_elem_list

    def get_files(
        self, options: pyfile.SearchOptions
    ) -> list[pyfile.SegmentedSearchResult] | list[pyfile.File]:
        file_list = self.__files
        if options.recursion:
            file_list = self.__get_files_recursively()
        if len(options.extensions) > 0:
            file_list = self.__get_files_by_extensions(file_list, options.extensions)
        return self.__group_by_parent(file_list) if options.segmentation else file_list

    def __get_directories_recursively(self) -> list[Directory]:
        to_return = self.__directories
        for directory in self.__directories:
            to_return.extend(directory.__get_directories_recursively())
        return to_return

    def get_directories(self):
        return self.__directories

    def _update_metadata(self, path):
        pass

    def get_size(self):
        pass
