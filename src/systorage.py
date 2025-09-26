from src.path import Path

class Systorage:
    _path: Path
    _parent_name: str
    _self_name: str

    def __init__(self, path: str):
        self._path = Path(path)
        self._parent_name = self._path.get_parent_name()
        self._name = self._path.get_name()

    # Getters
    def get_name(self):
        return self._name
    
    def get_parent_name(self):
        return self._parent_name
    
    def get_path(self):
        return self._path.get_literal()
        
    def get_path_object(self):
        return self._path.get_internal()