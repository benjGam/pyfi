from src.systorage import Systorage
import os

class File(Systorage):
    _extension: str

    def __init__(self, path: str):
        super().__init__(path)
        if self.exists() and not os.path.isfile(path):
            raise Exception(f"\"{path}\" is not a file.")

    def get_extension(self) -> str:
        path = self.get_path()
        return path[path.rfind("."):len(path)]
    
    def get_name(self, with_extension: bool = False) -> str:
        return super().get_name() + (self.get_extension() if with_extension else "")
    
    def create(self) -> bool:
        self.get_path_object().touch(exist_ok=True)
        return self.exists()

    def append(self, text_to_append: str) -> None:
        if not self.exists():
            self.create()
        with open(self.get_path(), "a") as fs:
            fs.write(text_to_append)

    def write(self, text_to_write: str) -> None:
        if not self.exists():
            self.create()        
        with open(self.get_path(), "w") as fs:
            fs.write(text_to_write)

    def read_to_end(self, unexisting_raise: bool = True) -> str:
        file_text_content = ""
        if not self.exists():
            if unexisting_raise: raise Exception(f"\"{self.get_path()}\" file do not exist.")
        else:
            with open(self.get_path(), "r") as fs:
                fs.seek(0)
                file_text_content = fs.read()
        return file_text_content

    def delete_content(self) -> bool:
        print(self.exists())
        if self.exists() == False: return False
        self.write("")
        return True

    def delete(self, delete_content:bool = False) -> bool:
        if not self.exists(): return False
        if delete_content: self.delete_content()
        os.remove(self.get_path())
        return self.exists() == False