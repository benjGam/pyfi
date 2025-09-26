from pathlib import Path as path
import os.path as syspath 

class Path:
    _literal: str
    _internal: path

    def __init__(self, literal: str):
        self._literal = self.format_literal_path(literal)
        self._internal = path(self._literal)

    def exists(self):
        return syspath.exists(self._literal)

    def get_parent_name(self):
        parent_names = self._literal.split("/")
        return parent_names[len(parent_names) -2]

    def get_name(self):
        return self._literal[self._literal.rfind("/")+1 : self._literal.rfind(".")]

    def get_literal(self):
        return self._literal
    
    def get_internal(self):
        return self._internal

    ### Utils methods

    def format_literal_path(self, literal: str) -> str:
        # Replace "\" by "/" (universal path format)
        literal = literal.replace("\\", "/")
        # Remove all "//" occurrences in path to form it well
        while ("//" in literal): literal = literal.replace("//", "/")
        return literal if not literal.endswith("/") else literal[0:-1]