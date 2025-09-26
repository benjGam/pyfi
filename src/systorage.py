from src.path import Path

class Systorage:
    _path: Path
    _parent_name: str
    _self_name: str

    def __init__(self, path: str):
        self._path = Path(path)
        self._parent_name = self._path.get_parent_name()
        self._name = self._path.get_name()