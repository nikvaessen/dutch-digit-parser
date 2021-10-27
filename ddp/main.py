################################################################################
#
# This file implements a CLI over the dutch digit grammar parsed
# by the lark engine.
#
# Author(s): Nik Vaessen
################################################################################

import sys
import click

from typing import TextIO

from . import parse_digit_text

################################################################################
# implement the CLI


@click.command()
@click.option(
    "--in",
    "in_file",
    type=click.File("r"),
    help="path to file containing the digit, omit to read from STDIN",
    default=sys.stdin,
)
@click.option(
    "--out",
    "out_file",
    type=click.File("w"),
    help="path to write output to, omit to write to STDOUT",
    default=sys.stdout,
)
@click.option(
    "--tree",
    "print_tree",
    help="when enabled, the parse tree will be included in the output",
    default=False,
    is_flag=True,
)
@click.option(
    "--pretty",
    "print_tree",
    help="when enabled, the digit will be printed with a separator for readability "
    "every 3 digits",
    default=False,
    is_flag=True,
)
def main(in_file: TextIO, out_file: TextIO, print_tree: bool):
    text = in_file.readlines()[0].strip()
    output, tree = parse_digit_text(text)

    if print_tree:
        print(tree.pretty(), file=out_file)

    print(output, file=out_file)


if __name__ == "__main__":
    main()
