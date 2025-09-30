from abc import ABC, abstractmethod
from .path import Path


class Systorage(ABC):

    __path: Path
    __name: str
    __parent = None

    def __init(self, path):
        self.__path = Path(path)

    def exists(self) -> bool:
        return self.__path.exists()
