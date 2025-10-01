from ..enums.extensions import Extensions


class SearchOptions:

    recursion = property(lambda self: self._recursion)
    segmentation = property(lambda self: self._segmentation)
    extensions = property(lambda self: self._extensions)

    def __init__(
        recursion: bool = False,
        segmentation: bool = False,
        extensions: list[str | Extensions] = [],
    ):
        pass

    def __parse_extensions(extensions: list[str | Extensions]) -> list[str]:
        return [x.value if type(x) != str else x for x in extensions]
