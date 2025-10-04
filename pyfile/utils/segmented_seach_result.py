import pyfile


class SegmentedSearchResult:

    parent: pyfile.Directory = property(lambda self: self._parent)
    childs: list[pyfile.File] | list[pyfile.Directory] = property(
        lambda self: self._childs
    )

    def __init__(
        self,
        parent: pyfile.Directory,
        childs: list[pyfile.File] | list[pyfile.Directory],
    ):
        self._parent = parent
        self._childs = childs
