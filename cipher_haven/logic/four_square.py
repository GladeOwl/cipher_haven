"""Four-square Cipher"""

from string import ascii_uppercase
import numpy
from cipher_haven.logic.cipher import CIPHER

ALPHABETS_WITHOUT_Q: str = ascii_uppercase.replace("Q", "")


class FOURSQUARE(CIPHER):
    """Four-square Cipher Class"""

    def __init__(self, key1: str, key2: str) -> None:
        self.key1: str = key1.upper()
        self.key2: str = key2.upper()

        if "Q" in self.key1 or "Q" in self.key2:
            raise ValueError(
                "Keys cannot have the letter Q in them. The Cipher doesn't support it."
            )

        # The First and Fourth tables are just copies of the plaintable
        self.plaintable: numpy.ndarray = None
        self.second_table: numpy.ndarray = None
        self.third_table: numpy.ndarray = None

        self.__generate_tables()

    def __generate_code(self, key: str) -> numpy.array:
        key_letters: list = list({item: None for item in list(key)})
        extra_letters: list = [x for x in ALPHABETS_WITHOUT_Q if x not in key]
        return numpy.array(list(key_letters + extra_letters))

    def __generate_tables(self):
        q_less_alphabets: numpy.array = numpy.array(list(ALPHABETS_WITHOUT_Q))

        self.plaintable = q_less_alphabets.reshape(5, 5)
        self.second_table = self.__generate_code(self.key1).reshape(5, 5)
        self.third_table = self.__generate_code(self.key2).reshape(5, 5)

    def encrypt(self, message: str) -> str:
        """Encrypt the Message using the Four-square Cipher"""

        plaintext: str = message.upper().replace(" ", "")
        plaintext = plaintext if len(plaintext) % 2 == 0 else plaintext + "X"

        pairs: list = [
            (plaintext[i - 1], plaintext[i]) for i in range(1, len(plaintext), 2)
        ]

        cipher_pairs: list = []
        for i, j in pairs:
            i_index = numpy.argwhere(self.plaintable == i)[0]
            j_index = numpy.argwhere(self.plaintable == j)[0]

            first_letter: str = self.second_table[i_index[0], j_index[1]]
            second_letter: str = self.third_table[j_index[0], i_index[1]]
            cipher_pairs.append(first_letter + second_letter)

        return " ".join(cipher_pairs)

    def decrypt(self, encrypted_message: str) -> str:
        """Decrypt the Message using the Four-square Cipher"""

        encrypted_text: str = encrypted_message.upper().replace(" ", "")
        if len(encrypted_text) % 2 != 0:
            raise ValueError("Key seems have uneven number of letters. Seems odd.")

        pairs: list = [
            (encrypted_text[i - 1], encrypted_text[i])
            for i in range(1, len(encrypted_text), 2)
        ]

        decrypted_message: str = ""
        for i, j in pairs:
            i_index = numpy.argwhere(self.second_table == i)[0]
            j_index = numpy.argwhere(self.third_table == j)[0]

            first_letter: str = self.plaintable[i_index[0], j_index[1]]
            second_letter: str = self.plaintable[j_index[0], i_index[1]]
            decrypted_message += first_letter + second_letter

        return decrypted_message
