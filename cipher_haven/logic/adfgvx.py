"""ADFGVX Cipher"""

from string import ascii_uppercase
from rich.console import Console
from rich.table import Table, box
from itertools import cycle
import numpy

CODE_TABLE: dict = {"A": 0, "D": 1, "F": 2, "G": 3, "V": 4, "X": 5}


class ADFGVX:
    """ADFGVX Cipher Class"""

    def __init__(self, transpose_key: str, table_code: str) -> None:
        self.table: Table = None
        self.code_table_keys: list = list(CODE_TABLE.keys())
        self.transpose_key: str = transpose_key
        self.table_code: str = table_code

        self.__generate_table()

    def __generate_code(self, code: str) -> list:
        extra_letters: list = [x for x in ascii_uppercase if x not in code]
        code_list: list = list({item: None for item in list(code)})

        sorted_letters: list = code_list + extra_letters

        table_key: list = []
        for letter in sorted_letters:
            table_key.append(letter)
            number: int = ascii_uppercase.index(letter) + 1
            if number <= 10:
                table_key.append(number if number != 10 else 0)

        return table_key

    def __generate_table(self) -> None:
        """Generate Table for the Affine Cipher"""

        table_key: numpy.array = numpy.array(
            self.__generate_code(self.table_code.upper())
        )

        # ADFGVX table has 6 rows and columns
        self.table: numpy.ndarray = table_key.reshape(6, 6)

        print_table: Table = Table(title="ADFGVX", show_lines=True, box=box.SQUARE)

        print_table.add_column(" ")
        for i, _ in enumerate(self.table):
            print_table.add_column(self.code_table_keys[i])

        for i, row in enumerate(self.table):
            table_row = [self.code_table_keys[i]] + list(row)
            print_table.add_row(*table_row)

        console = Console()
        console.print(print_table)

    def encrypt(self, message: str) -> str:
        """Encrypt the Message using the ADFGVX Cipher"""

        plaintext: str = message.upper().replace(" ", "")
        letters: list = list(map(str, plaintext))

        code_string: str = ""
        for letter in letters:
            index = numpy.argwhere(self.table == letter)

            row = index[0][0]
            column = index[0][1]

            position = self.code_table_keys[row] + self.code_table_keys[column]
            code_string += position

        plaintext_list: list = [[x] for x in self.transpose_key]

        key_list_index: int = 0
        for letter in code_string:
            plaintext_list[key_list_index].append(letter)
            key_list_index = (
                key_list_index + 1 if key_list_index < len(plaintext_list) - 1 else 0
            )

        plaintext_list.sort()
        encrypted_message: str = " ".join("".join(x[1:]) for x in plaintext_list)
        return encrypted_message.strip()

    def decrypt(self, encrypted_message: str) -> str:
        """Decrypt the Encrypted Message using the ADFGVX Cipher"""

        sorted_key: list = sorted(self.transpose_key)
        decrypt_table: list = [[x] for x in sorted_key]

        for i, letter in enumerate(encrypted_message.split(" ")):
            decrypt_table[i] += letter

        decrypt_table.sort(key=self.__decrypt_sort)

        for code_list in decrypt_table:
            code_list.pop(0)

        code_list_index: int = 0
        decrypt_table_index: int = 0
        code_string: str = ""

        for i in range(sum(map(len, decrypt_table))):
            code_list = decrypt_table[decrypt_table_index]

            if code_list_index > len(code_list) - 1:
                continue

            code_string += code_list[code_list_index]

            if decrypt_table_index + 1 < len(decrypt_table):
                decrypt_table_index += 1
            else:
                decrypt_table_index = 0
                code_list_index += 1

        decrypted_message: str = ""
        for i in range(0, len(code_string), 2):
            row: int = CODE_TABLE[code_string[i]]
            column: int = CODE_TABLE[code_string[i + 1]]

            letter: str = self.table[row, column]
            decrypted_message += letter

        return decrypted_message.lower()

    def __decrypt_sort(self, code_list: list) -> int:
        tranpose_letter = code_list[0]
        return self.transpose_key.index(tranpose_letter)
