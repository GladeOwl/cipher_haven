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

        # console = Console()
        # console.print(table)

    def encrypt(self, message: str, transpose_key: str) -> str:
        message_no_spaces: str = message.replace(" ", "").upper()
        letters: list = list(map(str, message_no_spaces))

        code_string: str = ""
        for letter in letters:
            index = numpy.argwhere(self.table == letter)

            row = index[0][0]
            column = index[0][1]

            position = self.code_table[row] + self.code_table[column]
            code_string += position

        plaintext_list: list = []
        for key_letter in transpose_key:
            plaintext_list.append([key_letter])

        key_list_index: int = 0
        for letter in code_string:
            plaintext_list[key_list_index].append(letter)
            key_list_index = (
                key_list_index + 1 if key_list_index < len(plaintext_list) - 1 else 0
            )

        plaintext_list.sort()
        plaintext: str = ""
        for code_list in plaintext_list:
            code_list.pop(0)
            plaintext += "".join(code_list) + " "

        return plaintext.strip()

    def decrypt(self, encrypted_message: str, transpose_key: str) -> str:
        self.tranpose_key = transpose_key

        sorted_key: list = sorted(list(transpose_key))

        decrypt_table: list = []
        for key_letter in sorted_key:
            decrypt_table.append([key_letter])

        encrypted_message_list = encrypted_message.split(" ")
        for x in range(len(encrypted_message_list)):
            message_string_list = list(encrypted_message_list[x])
            decrypt_table[x] += message_string_list

        decrypt_table.sort(key=self.__decrypt_sort)

        for code_list in decrypt_table:
            code_list.pop(0)

        code_list_index: int = 0
        decrypt_table_index: int = 0
        code_string: str = ""
        # TODO: This will break with uneven number of letters.
        for x in range(len(decrypt_table) * len(decrypt_table[0])):
            code_list = decrypt_table[decrypt_table_index]
            code_string += code_list[code_list_index]

            if decrypt_table_index + 1 < len(decrypt_table):
                decrypt_table_index += 1
            else:
                decrypt_table_index = 0
                code_list_index += 1

        print(code_string)

    def __decrypt_sort(self, code_list: list) -> int:
        tranpose_letter = code_list[0]
        return self.tranpose_key.index(tranpose_letter)


cipher = ADFGVX()
cipher.generate_table("nachtbommenwerper")
# plaintext = cipher.encrypt("attack at 1200am", "privacy")
plaintext = cipher.decrypt("DGDD DAGD DGAF ADDF DADV DVFA ADVX", "privacy")
