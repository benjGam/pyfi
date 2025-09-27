from src.systorage import Systorage
from src.file import File
from src.path import Path
from __future__ import annotations
import os

class Directory(Systorage):
    
    _files: list[File] = []
    _directories: list[Directory] = []

    def __init__(self, path: str, load: bool = False):
        super().__init__(path)
        if self.exists() and not os.path.isdir(path):
            raise Exception(f"\"{path}\" is not a folder.")
        if load: self.load()

    def load(self) -> None:
        self._files = Path(self.get_path()).get_files()
        self._directories = Path(self.get_path()).get_directories()