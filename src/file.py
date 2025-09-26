from src.systorage import Systorage

class File(Systorage):
    
    def __init__(self, path: str):
        super().__init__(path)