"""Bifid Cipher"""

from string import ascii_uppercase
from itertools import chain
import numpy
from cipher_haven.logic.cipher import CIPHER

AMOUNT_OF_ROWS_AND_COLUMNS = 6
AMOUNT_OF_ITEMS = AMOUNT_OF_ROWS_AND_COLUMNS * AMOUNT_OF_ROWS_AND_COLUMNS


class BIFID(CIPHER):
    """Bifid Cipher Class"""

    def __init__(self, table_code: str, block_size: int = 1) -> None:
        self.table: numpy.ndarray = None
        self.block_size: int = block_size
        self.table_code: str = table_code.upper()
        self.__generate_table()

    def __generate_table(self):
        extra_letters: list = [x for x in ascii_uppercase if x not in self.table_code]
        letters: list = list({x: None for x in list(self.table_code)})

        table_items: list = numpy.array(letters + extra_letters + list("0123456789"))
        self.table = table_items.reshape(
            AMOUNT_OF_ROWS_AND_COLUMNS, AMOUNT_OF_ROWS_AND_COLUMNS
        )

    def encrypt(self, message: str) -> str:
        """Encrypt the Message using the Bifid Cipher"""

        plaintext: str = message.upper().replace(" ", "")
        text_blocks: list = [
            plaintext[i : i + self.block_size]
            for i in range(0, len(plaintext), self.block_size)
        ]

        all_positions: list = []
        for block in text_blocks:
            positions: list = []

            for letter in block:
                index = numpy.argwhere(self.table == letter)
                positions.append([index[0][0], index[0][1]])

            sorted_positions: list = list(chain(*zip(*positions)))

            all_positions += [
                (sorted_positions[i - 1], sorted_positions[i])
                for i in range(1, len(sorted_positions), 2)
            ]

        return "".join(self.table[x, y] for x, y in all_positions)

    def decrypt(self, encrypted_message: str) -> str:
        """Decrypt the Message using the Bifid Cipher"""

        encrypted_text: str = encrypted_message.upper().replace(" ", "")
        text_blocks: list = [
            encrypted_text[i : i + self.block_size]
            for i in range(0, len(encrypted_text), self.block_size)
        ]

        all_positions: list = []
        for block in text_blocks:
            positions: list = []

            for letter in block:
                index = numpy.argwhere(self.table == letter)
                positions.append([index[0][0], index[0][1]])

            sorted_positions: list = list(chain(*positions))

            half: int = int(len(sorted_positions) / 2)
            new_positions: list = [
                sorted_positions[:half],
                sorted_positions[half:],
            ]

            all_positions += list(zip(*new_positions))

        print(all_positions)
        return "".join(self.table[x, y] for x, y in all_positions)
