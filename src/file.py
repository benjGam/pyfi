from src.systorage import Systorage

class File(Systorage):
    _extension: str

    def __init__(self, path: str):
        super().__init__(path)

    def get_extension(self):
        path = self._path._path_literal
        return path[path.rfind("."):len(path)]
    
    def get_name(self, with_extension: bool = False):
        return super().get_name() + (self.get_extension() if with_extension else "")