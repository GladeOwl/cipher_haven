"""Affine Cipher"""

from string import ascii_uppercase
from cipher_haven.logic.cipher import CIPHER

NUMBER_OF_ALPHABETS: int = 26
CO_PRIME: list = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]


class AFFINE(CIPHER):
    """Affine Cipher Class"""

    def __init__(self, alpha: int = 5, beta: int = 8) -> None:
        if alpha not in CO_PRIME:
            raise ValueError(
                f"Given number is not a co-prime of 26, it must be in the list: {CO_PRIME}"
            )

        self.alpha: int = alpha
        self.beta: int = beta

    def encrypt(self, message: str) -> str:
        """Encrypt the Message using the Affine Cipher"""

        plaintext: str = message.upper().replace(" ", "")

        encrypted_message: str = ""
        for letter in plaintext:
            letter_index: int = ascii_uppercase.index(letter)
            letter_key: int = (
                self.alpha * letter_index + self.beta
            ) % NUMBER_OF_ALPHABETS
            encrypted_message += ascii_uppercase[letter_key]

        return encrypted_message

    def __find_modulor_multiplicative_inverse(self):
        for index in range(1, NUMBER_OF_ALPHABETS):
            if (
                (self.alpha % NUMBER_OF_ALPHABETS) * (index % NUMBER_OF_ALPHABETS)
            ) % NUMBER_OF_ALPHABETS == 1:
                return index
        return -1

    def decrypt(self, encrypted_message: str) -> str:
        """Decrypt the Encrypted Message using the Affine Cipher"""

        a_inverse: int = self.__find_modulor_multiplicative_inverse()
        decrypted_message: str = ""

        for letter in encrypted_message:
            letter_index: int = ascii_uppercase.index(letter)
            letter_key: int = (
                a_inverse * (letter_index - self.beta) % NUMBER_OF_ALPHABETS
            )
            decrypted_message += ascii_uppercase[letter_key]

        return decrypted_message
