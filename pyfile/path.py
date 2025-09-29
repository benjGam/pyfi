from pathlib import Path as ComplexPath
import os


class Path:

    _literal: str
    _complex: ComplexPath

    def __init__(self, path: str):
        pass

    def format_path(self, path: str | ComplexPath) -> str:
        pass

    def exists(self) -> bool:
        pass

    def get_literal(self) -> str:
        pass

    def get_complex(self) -> ComplexPath:
        pass
