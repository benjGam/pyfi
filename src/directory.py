from src.systorage import Systorage
from src.file import File
from src.path import Path
from __future__ import annotations
import os

class Directory(Systorage):
    
    _files: list[File] = []
    _directories: list[Directory] = []

    def __init__(self, path: str, auto_load: bool = False):
        super().__init__(path)
        if self.exists() and not os.path.isdir(path):
            raise Exception(f"\"{path}\" is not a folder.")
        if auto_load: self.load(True)

    def load(self, recursive_load: bool = False) -> None:
        self._files = Path(self.get_path()).get_files()
        self._directories = Path(self.get_path()).get_directories(recursive_load)