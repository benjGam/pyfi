from __future__ import annotations
import pyfile
import os
from .utils import *

class Directory(pyfile.Systorage):
    
    _files: list[pyfile.File] = []
    _directories: list[Directory] = []

    def __init__(self, path: str, auto_load: bool = False):
        super().__init__(path)
        if self.exists() and not os.path.isdir(path):
            raise Exception(f"\"{path}\" is not a folder.")
        if auto_load: self.load(True)

    def load(self, recursive_load: bool = False) -> None:        
        self._files = pyfile.Path(self.get_path()).get_files()
        self._directories = pyfile.Path(self.get_path()).get_directories(recursive_load)

    def get_files_paths(self, recursively: bool = False):
        to_return = [{self.get_path(): list(map(lambda x: x.get_path(), self._files))}]
        if recursively:
            for dir in self._directories:
                to_return.append(dir.get_files(recursively))
        return flatten(to_return)
    
    def get_files(self, recursively: bool = False):
        to_return = [self._files]
        if recursively:
            for dir in self._directories:
                to_return.append(dir.get_files(recursively))
        return flatten(to_return)