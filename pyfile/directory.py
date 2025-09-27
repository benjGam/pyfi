from __future__ import annotations
import pyfile
import os

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