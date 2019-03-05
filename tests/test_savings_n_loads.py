# -*- coding: utf-8 -*-
from os import remove

from pupy.savings_n_loads import load_jasm
from pupy.savings_n_loads import lpak
from pupy.savings_n_loads import save_jasm
from pupy.savings_n_loads import spak

JASM_DICT = {"Jason": ["Green",
                       "Berg"],
             "Jasm":  ["Grundle",
                       "Bug"]}

def test_ljson_n_sjson():
    """

    """
    save_jasm('jasm_dict.json', JASM_DICT)

    loaded_data = load_jasm('jasm_dict.json')
    print(JASM_DICT)
    print(loaded_data)
    assert loaded_data == JASM_DICT
    remove('jasm_dict.json')

def test_spak_n_lpak():
    """

    """
    spak('data.pak', JASM_DICT)
    loaded_data = lpak('data.pak')
    assert loaded_data == JASM_DICT
    remove('data.pak')


