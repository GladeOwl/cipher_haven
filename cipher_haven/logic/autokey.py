""" Autokey Cipher """

from copy import deepcopy
from string import ascii_uppercase
from rich.console import Console
from rich.table import Table, box
import numpy


class AUTOKEY:
    """Autokey Cipher Class"""

    def __init__(self) -> None:
        self.__generate_table()

    def __generate_table(self) -> None:
        ascii_table = list(ascii_uppercase)
        table_lists: list = []

        for _ in ascii_table:
            localtable: list = deepcopy(ascii_table)
            table_lists += localtable

            first_letter: str = ascii_table.pop(0)
            ascii_table.append(first_letter)

        table_array = numpy.array(table_lists)
        self.table = table_array.reshape(26, 26)

    def print_table(self) -> bool:
        """Prints the full Alphabet table"""

        if self.table is None:
            return False

        table_print = Table(title="Autokey", show_lines=True, box=box.SQUARE)

        table_print.add_column(" ")

        for i, _ in enumerate(self.table):
            table_print.add_column(ascii_uppercase[i])

        for i, _ in enumerate(self.table):
            table_row = [ascii_uppercase[i]] + list(self.table[i])
            table_print.add_row(*table_row)

        console = Console()
        console.print(table_print)

        return True

    def encrypt(self, message: str, key: str) -> str:
        """Encrypt the Message using the Autokey Cipher"""
        plaintext: str = message.upper().replace(" ", "")
        plainkey: str = key.upper() + plaintext

        encrypted_message: str = ""
        for i, letter in enumerate(plaintext):
            keyletter: str = plainkey[i]

            row: int = ascii_uppercase.index(letter)
            column: int = ascii_uppercase.index(keyletter)

            encrypted_letter: str = self.table[row, column]
            encrypted_message += encrypted_letter
        return encrypted_message
