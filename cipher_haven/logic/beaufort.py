""" Beaufort Cipher """

from string import ascii_uppercase
from itertools import cycle
from cipher_haven.logic.cipher import CIPHER

NUMBER_OF_ALPHABETS: int = 26


class BEAUFORT(CIPHER):
    """Beaufort Cipher Class"""

    def __init__(self, key: str) -> None:
        self.key: str = key.upper()

    def __extend_key(self, message: str) -> str:
        keys: cycle = cycle(list(self.key))
        return "".join(next(keys) for _ in message)

    def __get_cipher_indices(self, message: str, key: str) -> list:
        cipher_indices: list = []

        for i, letter in enumerate(message):
            letter_index: int = ascii_uppercase.index(letter)
            key_index: int = ascii_uppercase.index(key[i])
            cipher_index: int = key_index - letter_index

            if cipher_index < 0:
                cipher_index += NUMBER_OF_ALPHABETS

            cipher_indices.append(cipher_index)

        return cipher_indices

    def encrypt(self, message: str) -> str:
        """Encrypt the Message using the Beaufort Cipher"""

        plaintext: str = message.upper().replace(" ", "")
        extended_key: str = self.__extend_key(plaintext)

        cipher_indices: list = self.__get_cipher_indices(plaintext, extended_key)
        return "".join(ascii_uppercase[i] for i in cipher_indices)

    def decrypt(self, encrypted_message: str) -> str:
        """Decrypt the Message using the Beaufort Cipher"""

        encrypted_text: str = encrypted_message.upper().replace(" ", "")
        extended_key: str = self.__extend_key(encrypted_text)

        cipher_indices: list = self.__get_cipher_indices(encrypted_text, extended_key)
        return "".join(ascii_uppercase[i] for i in cipher_indices)
