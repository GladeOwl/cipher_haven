"""Alphabet Cipher"""

from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase
from rich.console import Console
from rich.table import Table, box
import numpy


class ALPHABET:
    """Alphabet Cipher Class"""

    def __init__(self) -> None:
        self.table: numpy.ndarray = None
        self.keyword_list: list = []
        self.__generate_table()

    def __generate_table(self) -> None:
        ascii_table = list(ascii_lowercase)
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

        table_print = Table(title="Alphabet", show_lines=True, box=box.SQUARE)
        table_print.add_column(" ")

        for i, _ in enumerate(self.table):
            table_print.add_column(ascii_uppercase[i])

        for i, _ in enumerate(self.table):
            table_row = [ascii_uppercase[i]] + list(self.table[i])
            table_print.add_row(*table_row)

        console = Console()
        console.print(table_print)

        return True

    def __prepare_keyword(self, message_string: str, keyword: str) -> None:
        keyword_index: int = 0

        for _ in range(len(message_string)):
            self.keyword_list.append(keyword[keyword_index].upper())
            keyword_index = keyword_index + 1 if keyword_index < len(keyword) - 1 else 0

    def encrypt(self, message: str, keyword: str) -> str:
        """Encrypt the Message using the Alphabet Cipher"""

        plaintext: str = message.upper().replace(" ", "")
        self.__prepare_keyword(plaintext, keyword)

        encrypted_message: str = ""

        for i, message_letter in enumerate(plaintext):
            row: int = ascii_uppercase.index(self.keyword_list[i])
            column: int = ascii_uppercase.index(message_letter)

            letter: str = self.table[row, column]
            encrypted_message += letter

        return encrypted_message

    def decrypt(self, encrypted_message: str, keyword: str) -> str:
        """Decrypt the Encrypted Message using the Alphabet Cipher"""

        encrypted_text = encrypted_message.upper().replace(" ", "")
        self.__prepare_keyword(encrypted_text, keyword)

        decrypted_message: str = ""
        for i, letter in enumerate(encrypted_text):
            keyletter: str = self.keyword_list[i]

            row: int = ascii_uppercase.index(keyletter)
            column: int = list(self.table[row]).index(letter.lower())

            decrypted_message += ascii_uppercase[column]

        return decrypted_message
