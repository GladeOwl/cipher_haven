import numpy
from string import ascii_lowercase


class ADFGVX:
    def __init__(self) -> None:
        self.table = None
        self.code_table = ["A", "D", "F", "G", "V", "X"]

    def __generate_code(self, code: str) -> list:
        # TODO: This is a disgrace! Change it.
        alphabets: list = list(map(str, ascii_lowercase))

        extra_letters: list = []
        for letter in alphabets:
            if letter not in code:
                extra_letters.append(letter)

        code_list_with_duplicates: list = list(map(str, code))
        code_list: list = []

        # TODO: Use Dict comprehenssion to order instead. Dicts are always ordered. It's neat! "{x: None for x in unordered_list}"
        [
            code_list.append(letter)
            for letter in code_list_with_duplicates
            if letter not in code_list
        ]

        sorted_letters: list = code_list + extra_letters
        table_key: list = []

        for letter in sorted_letters:
            table_key.append(letter)

            number: int = alphabets.index(letter) + 1

            if number <= 10:
                table_key.append(number if number != 10 else 0)

        return table_key

    def generate_table(self, code: str) -> None:
        table_key = numpy.array(self.__generate_code(code.lower()))

        print(table_key)
        # ADFGVX table has 6 rows and columns
        self.table: numpy.ndarray = table_key.reshape(6, 6)

        # TODO: Maybe have a more readable version of the table with the ADFGVX embeded?
        print("Table Generated")
        print(self.table)

    def encrypt(self, message: str, key: str):
        message_no_spaces = message.replace(" ", "").lower()
        letters: list = list(map(str, message_no_spaces))

        code_string: str = ""
        for letter in letters:
            index = numpy.argwhere(self.table == letter)

            # TODO: numpy creates a nested list, look into ways to simplifying it.
            row = index[0][0]
            column = index[0][1]

            position = self.code_table[column] + self.code_table[row]
            code_string += position

            # print(letter, position)

        enciphered_plaintext = [
            code_string[i : i + len(key)] for i in range(0, len(code_string), len(key))
        ]

        print(enciphered_plaintext)


cipher = ADFGVX()
cipher.generate_table("SOMETHINGFOREVERYONE")
cipher.encrypt("Honey I shrunk the kids", "NOTTHEBEES")
