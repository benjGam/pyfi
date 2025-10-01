from .systorage import Systorage
import os


class Directory(Systorage):

    def __init__(self, path):
        super().__init__(path)
        if not os.path.isfile(path):
            raise Exception(f'"{path}" is not a folder')
