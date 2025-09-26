from src.systorage import Systorage

class File(Systorage):
    _extension: str

    def __init__(self, path: str):
        super().__init__(path)

    def get_extension(self):
        path = self.get_path()
        return path[path.rfind("."):len(path)]
    
    def get_name(self, with_extension: bool = False):
        return super().get_name() + (self.get_extension() if with_extension else "")
    
    def create(self):
        self.get_path_object().touch(exist_ok=True)

    def append(self, text_to_append):
        if not self.get_path_object().exists():
            self.create()
        with open(self.get_path(), "a") as fs:
            fs.write(text_to_append)

    def write(self, text_to_write):
        if not self.get_path_object().exists():
            self.create()        
        with open(self.get_path(), "w") as fs:
            fs.write(text_to_write)

    def delete_content(self):
        if not self.get_path_object().exists(): raise
        self.write("")