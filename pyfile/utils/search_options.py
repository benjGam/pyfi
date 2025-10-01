from ..enums.extensions import Extensions


class SearchOptions:

    def __init__(
        recursion: bool = False,
        segmentation: bool = False,
        extensions: list[str | Extensions] = [],
    ):
        pass

    def __parse_extensions(extensions: list[str | Extensions]) -> list[str]:
        return [x.value if type(x) != str else x for x in extensions]
