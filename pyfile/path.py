from pathlib import Path as path
import pyfile
from pyfile.utils import *
from pyfile.enums import *
import os.path as syspath
from typing import List, Union

class Path:
    """
    A wrapper class for filesystem paths.

    This class provides both a literal string representation (`_literal`) 
    and a `pathlib.Path` object (`_internal`) of the path. It includes 
    methods to retrieve files, directories, and systorage objects, 
    optionally filtering by extensions and supporting recursive searches.
    """

    _literal: str  # The normalized string representation of the path
    _internal: path  # The pathlib.Path object corresponding to _literal

    def __init__(self, literal: str) -> None:
        """
        Initialize the Path object.

        Args:
            literal (str): The raw path string (absolute or relative).
        """
        self._literal = self.format_literal_path(literal)
        self._internal = path(self._literal)

    def exists(self) -> bool:
        """
        Check if the path exists in the filesystem.

        Returns:
            bool: True if the path exists, False otherwise.
        """
        return syspath.exists(self._literal)

    def get_parent_name(self) -> str:
        """
        Return the name of the parent directory.

        Returns:
            str: Name of the parent directory.
        """
        parent_names = self._literal.split("/")
        return parent_names[len(parent_names) - 2]

    def get_name(self) -> str:
        """
        Return the base name of the file or directory, without its extension.

        Returns:
            str: Name of the file or directory.
        """
        last_index_of_dot = self._literal.rfind(".")
        return self._literal[self._literal.rfind("/") + 1 : len(self._literal) if last_index_of_dot == -1 else last_index_of_dot]

    def get_literal(self) -> str:
        """
        Get the literal string representation of the path.

        Returns:
            str: The formatted path string.
        """
        return self._literal
    
    def get_internal(self) -> path:
        """
        Get the internal pathlib.Path object.

        Returns:
            pathlib.Path: The internal Path object.
        """
        return self._internal
    
    def get_systorage_paths(self, recursively: bool = False) -> List[str]:
        """
        Retrieve all items (files and directories) under this path.

        Args:
            recursively (bool): If True, performs a recursive search.

        Returns:
            List[str]: A list of formatted paths for all contained items.
        """
        return list(map(
            lambda path: self.format_literal_path(str(path)),
            (self._internal.rglob if recursively else self._internal.glob)("*")
        ))

    def get_files_paths(self, recursively: bool = False, extensions: List[Extensions | str] = []) -> List[str]:
        """
        Get paths of all files, optionally filtered by extensions.

        Args:
            recursively (bool): If True, search in subdirectories.
            extensions (List[str]): List of extensions to include (e.g., [".txt", ".py"]).

        Returns:
            List[str]: List of file paths matching the criteria.
        """
        extensions = convert_enum_values_to_str(extensions)
        return list(filter(
            lambda current_path: syspath.isfile(current_path) and (
                True if len(extensions) == 0 else (current_path[current_path.rfind("."):len(current_path)] in extensions)
            ),
            self.get_systorage_paths(recursively)
        ))

    def get_files(self, recursively: bool = False, extensions: List[Extensions | str] = []) -> List[pyfile.File]:
        """
        Get File objects for all files in the path, optionally filtered by extensions.

        Args:
            recursively (bool): If True, include files from subdirectories.
            extensions (List[Union[Extensions, str]]): List of extensions to filter files.

        Returns:
            List[pyfile.File]: List of File objects corresponding to the filtered files.
        """
        extensions = convert_enum_values_to_str(extensions)
        builded_files = map(lambda path: pyfile.File(path), self.get_files_paths(recursively, extensions))
        return list(builded_files if len(extensions) == 0 else filter(
            lambda builded_file: builded_file.get_extension() in extensions, builded_files
        ))
    
    def get_directories_paths(self, recursively: bool = False) -> List[str]:
        """
        Get paths of all subdirectories in this path.

        Args:
            recursively (bool): If True, include subdirectories of subdirectories.

        Returns:
            List[str]: List of directory paths.
        """
        return list(filter(lambda path: syspath.isdir(path), self.get_systorage_paths(recursively)))

    def get_directories(self, recursively: bool = False) -> List[pyfile.Directory]:
        """
        Get Directory objects for all subdirectories in this path.

        Args:
            recursively (bool): If True, include subdirectories of subdirectories.

        Returns:
            List[pyfile.Directory]: List of Directory objects for each subdirectory.
        """
        return list(map(lambda path: pyfile.Directory(path, recursively), self.get_directories_paths()))

    ### Utility methods

    def format_literal_path(self, literal: str) -> str:
        """
        Normalize a path string to a standard format.

        Replaces backslashes with forward slashes, removes double slashes,
        and removes trailing slashes.

        Args:
            literal (str): The raw path string.

        Returns:
            str: Formatted path string.
        """
        literal = literal.replace("\\", "/")
        while ("//" in literal):
            literal = literal.replace("//", "/")
        return literal if not literal.endswith("/") else literal[0:-1]