from abc import ABC, abstractmethod
from .path import Path
import os


class Systorage(ABC):

    __path: Path
    __name: str
    __parent = None

    def __init__(self, path):
        self._update_metadata(path)

    @abstractmethod
    def _update_metadata(self, path: str):
        self.__path = Path(path)
        self.__name = self.__path.get_complex().name

    def exists(self) -> bool:
        return self.__path.exists()

    @abstractmethod
    def create(self) -> bool:
        pass

    @abstractmethod
    def delete(self) -> bool:
        pass

    def rename(self, new_name: str) -> bool:
        if "/" or "\\" in new_name:
            raise Exception("This method is not intended to be used as move method")
        old_path = self.__path.get_literal()
        new_path = f"{str(self.__path.get_complex().parent())}/{new_name}"
        os.rename(self.__path._literal, new_path)
        self._update_metadata(new_path)
        return os.path.exists(old_path) == False and os.path.exists(new_path) == True

    def move(self, new_path: str) -> bool:
        new_path = os.path.realpath(new_path)  # Format to absolute
        # If parent of new path do not exists
        if not os.path.exists(os.path.dirname()):
            raise Exception(f'"{new_path}" do not exists')
        old_path = self.__path.get_literal()
        os.rename(old_path, new_path)
        self._update_metadata(new_path)
        return os.path.exists(old_path) == False and os.path.exists(new_path) == True
