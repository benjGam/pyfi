from pathlib import Path as path
import os.path as syspath 

class Path:
    _path_literal: str
    _internal_path: path

    def __init__(self, path_literal: str):
        self._path_literal = self.format_literal_path(path_literal)
        self._internal_path = path(self._path_literal)

    def exists(self):
        return syspath.exists(self._path_literal)

    def get_parent_name(self):
        parent_names = self._path_literal.split("/")
        return parent_names[len(parent_names) -1]

    ### Utils methods

    def format_literal_path(self, path_literal: str) -> str:
        # Replace "\" by "/" (universal path format)
        path_literal = path_literal.replace("\\", "/")
        # Remove all "//" occurrences in path to form it well
        while ("//" in path_literal): path_literal = path_literal.replace("//", "/")
        return path_literal if not path_literal.endswith("/") else path_literal[0:-1]