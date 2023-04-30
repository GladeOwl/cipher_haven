import numpy
from rich.console import Console
from rich.table import Table, box
from string import ascii_uppercase


class ADFGVX:
    def __init__(self) -> None:
        self.table = None
        self.code_table = ["A", "D", "F", "G", "V", "X"]

    def __generate_code(self, code: str) -> list:
        alphabets: list = list(ascii_uppercase)

        extra_letters: list = []
        for letter in alphabets:
            if letter not in code:
                extra_letters.append(letter)

        code_list_with_duplicates: list = list(code)
        code_list_without_duplicates: list = list(
            {item: None for item in code_list_with_duplicates}
        )

        sorted_letters: list = code_list_without_duplicates + extra_letters
        table_key: list = []

        for letter in sorted_letters:
            table_key.append(letter)
            number: int = alphabets.index(letter) + 1
            if number <= 10:
                table_key.append(number if number != 10 else 0)

        return table_key

    def generate_table(self, code: str) -> None:
        table_key = numpy.array(self.__generate_code(code.upper()))

        # print(table_key)
        # ADFGVX table has 6 rows and columns
        self.table: numpy.ndarray = table_key.reshape(6, 6)

        table = Table(title="ADFGVX", show_lines=True, box=box.SQUARE)

        table.add_column(" ")
        for y in range(len(self.table)):
            table.add_column(self.code_table[y])

        for y in range(len(self.table)):
            table_row = [self.code_table[y]] + list(self.table[y])
            table.add_row(*table_row)

        console = Console()
        console.print(table)

    def encrypt(self, message: str, key: str):
        message_no_spaces = message.replace(" ", "").upper()
        letters: list = list(map(str, message_no_spaces))

        code_string: str = ""
        for letter in letters:
            index = numpy.argwhere(self.table == letter)

            # TODO: numpy creates a nested list, look into ways to simplifying it.
            row = index[0][0]
            column = index[0][1]

            position = self.code_table[row] + self.code_table[column]
            code_string += position

        enciphered_plaintext = [
            code_string[i : i + len(key)] for i in range(0, len(code_string), len(key))
        ]

        return code_string
