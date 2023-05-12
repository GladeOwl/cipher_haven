import numpy
from copy import deepcopy
from rich.console import Console
from rich.table import Table, box
from string import ascii_lowercase, ascii_uppercase


class ALPHABET:
    def __init__(self) -> None:
        self.table = None
        self.__generate_table()

    def __generate_table(self) -> None:
        # loop_index: int = 0
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
        if self.table == None:
            return False

        table_print = Table(title="Alphabet", show_lines=True, box=box.SQUARE)
        table_print.add_column(" ")
        for i in range(len(self.table)):
            table_print.add_column(ascii_uppercase[i])

        for i in range(len(self.table)):
            table_row = [ascii_uppercase[i]] + list(self.table[i])
            table_print.add_row(*table_row)

        console = Console()
        console.print(table_print)

        return True
