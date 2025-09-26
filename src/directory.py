from src.systorage import Systorage
from src.file import File
from __future__ import annotations
import os

class Directory(Systorage):
    
    _files: list[File] = []
    _directories: list[Directory] = []

    def __init__(self, path: str):
        super().__init__(path)
        if self.exists() and not os.path.isdir(path):
            raise Exception(f"\"{path}\" is not a folder.")