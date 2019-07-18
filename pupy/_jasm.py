# -*- coding: utf-8 -*-
# Pretty ~ Useful ~ Python


def _json():
    for mod in ("ujson", "rapidjson", "json"):
        try:
            res = __import__(mod)
            return res
        except ImportError:
            pass
    raise ImportError(
        "Ya need one of the following:\n"
        "   ~ ujson; 'pip install ujson'\n"
        "   ~ ujson; 'pip install python-rapidjson'\n"
        "   ~ json; this should have come with python\n"
    )


json = _json()
