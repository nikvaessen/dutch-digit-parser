################################################################################
#
# This file provides an API to the grammar parsed by Lark.
#
# Author(s): Nik Vaessen
################################################################################

from typing import Tuple
from itertools import chain

from lark import Lark, Transformer
from lark.tree import Tree

################################################################################
# the transformer determines the actual digit based on the text


eenheid_to_digit = {
    "een": 1,
    "twee": 2,
    "drie": 3,
    "vier": 4,
    "vijf": 5,
    "zes": 6,
    "zeven": 7,
    "acht": 8,
    "negen": 9,
}

tweeheid_to_digit = {
    "elf": 11,
    "twaalf": 12,
    "dertien": 13,
    "veertien": 14,
    "vijftien": 15,
    "zestien": 16,
    "zeventien": 17,
    "achttien": 18,
    "negentien": 19,
}

tienheid_to_digit = {
    "twintig": 20,
    "dertig": 30,
    "veertig": 40,
    "vijftig": 50,
    "zestig": 60,
    "zeventig": 70,
    "achttig": 80,
    "negentig": 90,
}

meerheid_to_digit = {
    "honderd": 100,
    "duizend": 1_000,
    "miljoen": 1_000_000,
    "miljard": 1_000_000_000,
}


class DigitTransformer(Transformer):
    def __init__(self):
        # define all terminals
        for k, v in chain(
            eenheid_to_digit.items(),
            tweeheid_to_digit.items(),
            tienheid_to_digit.items(),
            meerheid_to_digit.items(),
        ):
            # use default value to capture value
            setattr(self, str(k), lambda _, r=v: r)

    def eental(self, value):
        print("eental", value, "returned", sum(value))
        return sum(value)

    def tiental(self, value):
        print("tiental", value)
        return sum(value)

    def samenvoeging(self, value):
        eenheid, tienheid = value
        print("samenvoeging", value, "returned", eenheid + tienheid)

        return eenheid + tienheid

    def vuldeging(self, value):
        a, b = value
        print("vuldeging", value, "returned", a * b)
        return a * b

    def meertal(self, value):
        print("meertal:", value, 'returned', sum(value))
        return sum(value)

    def getal(self, digit):
        return str(digit)


################################################################################
# implement the parser and provide a method to access the parsed grammar

parser = Lark.open(
    "grammars/proto_dutch_digit_grammar.lark",
    rel_to=__file__,
    start="getal",
)
transformer = DigitTransformer()


def parse_digit_text(digit: str) -> Tuple[str, Tree]:
    tree = parser.parse(digit)
    print(tree.pretty())
    output = transformer.transform(tree)

    return output, tree
