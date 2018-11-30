# -*- coding: utf-8 -*-
from os import remove
from pupy.savings_n_loads import save_jasm, load_jasm

JASM_DICT = {"Jason": ["Green",
                       "Berg"],
             "Jasm": ["Grundle",
                      "Bug"]}


def test_jasm():
    """

    """
    save_jasm('jasm_dict.json', JASM_DICT)

    loaded_data = load_jasm('jasm_dict.json')
    print(JASM_DICT)
    print(loaded_data)
    assert loaded_data == JASM_DICT
    remove('jasm_dict.json')
