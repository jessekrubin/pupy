from pupy.decorations import flog


@flog
def somefunk():
    return None

somefunk()
