from src.systorage import Systorage
from src.path import Path

class Directory(Systorage):
    
    def __init__(self, path: str):
        super().__init__(path)