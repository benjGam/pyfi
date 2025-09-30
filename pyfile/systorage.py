from abc import ABC, abstractmethod
from .path import Path
import os


class Systorage(ABC):

    __path: Path
    __name: str
    __parent = None

    def __init(self, path):
        self.__path = Path(path)

    def exists(self) -> bool:
        return self.__path.exists()

    @abstractmethod
    def create(self) -> bool:
        pass

    @abstractmethod
    def delete(self) -> bool:
        pass

    def rename(self, new_name: str) -> bool:
        if os.path.exists(os.path.realpath(new_name)):
            raise Exception("This method is not intended to be used as move method")
        old_path = self.__path.get_literal()
        new_path = f"{str(self.__path.get_complex().parent())}/{new_name}"
        os.rename(self.__path._literal, new_path)
        return os.path.exists(old_path) == False and os.path.exists(new_path) == True
