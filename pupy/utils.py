from os import path

def parent_path(fdpath):
    """

    :param fdpath:
    :return:

    .. doctest:: python

        >>> from os import path
        >>> parent_path(path.abspath(__file__)) in path.abspath(__file__)
        True

    """
    return path.split(fdpath)[0]
