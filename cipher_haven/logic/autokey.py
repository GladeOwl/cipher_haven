""" Autokey Cipher """

from copy import deepcopy
from string import ascii_uppercase
from rich.console import Console
from rich.table import Table, box
import numpy
from cipher_haven.logic.cipher import CIPHER


class AUTOKEY(CIPHER):
    """Autokey Cipher Class"""

    def __init__(self, key: str) -> None:
        self.table: numpy.ndarray = None
        self.key: str = key.upper()
        self.__generate_table()

    def __generate_table(self) -> None:
        ascii_table = list(ascii_uppercase)
        table_lists: list = []

        for _ in ascii_uppercase:
            table_lists += ascii_table
            first_letter: str = ascii_table.pop(0)
            ascii_table.append(first_letter)

        table_array: numpy.array = numpy.array(table_lists)
        self.table = table_array.reshape(26, 26)

    def print_table(self) -> bool:
        """Prints the full Alphabet table"""

        if self.table is None:
            return False

        table_print = Table(title="Autokey", show_lines=True, box=box.SQUARE)
        table_print.add_column(" ")

        for i, _ in enumerate(self.table):
            table_print.add_column(ascii_uppercase[i])

        for i, row in enumerate(self.table):
            table_row = [ascii_uppercase[i]] + list(row)
            table_print.add_row(*table_row)

        console = Console()
        console.print(table_print)

        return True

    def encrypt(self, message: str) -> str:
        """Encrypt the Message using the Autokey Cipher"""

        plaintext: str = message.upper().replace(" ", "")
        plainkey: str = self.key + plaintext

        encrypted_message: str = ""
        for i, letter in enumerate(plaintext):
            keyletter: str = plainkey[i]

            row: int = ascii_uppercase.index(letter)
            column: int = ascii_uppercase.index(keyletter)

            encrypted_letter: str = self.table[row, column]
            encrypted_message += encrypted_letter

        return encrypted_message

    def decrypt(self, encrypted_message: str) -> str:
        """Decrypt the Message using the Autokey Cipher"""

        decrypted_message: str = ""
        for i, letter in enumerate(encrypted_message):
            keyletter: str = self.key[i]

            row: int = ascii_uppercase.index(keyletter)
            column: int = list(self.table[row]).index(letter)

            decrypted_letter = ascii_uppercase[column]
            self.key += decrypted_letter
            decrypted_message += decrypted_letter

        return decrypted_message
