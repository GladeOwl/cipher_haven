""" Atbash Cipher """

from string import ascii_uppercase


class ATBASH:
    """Atbash Cipher Class"""

    def __init__(self) -> None:
        self.alphabets: list = list(ascii_uppercase)
        self.alphabets_reversed: list = list(reversed(self.alphabets))

    def encrypt(self, message: str) -> str:
        """Encrypt the Message using the Atbash Cipher"""
        return "".join(
            [
                self.alphabets_reversed[self.alphabets.index(letter)]
                for letter in message.upper().replace(" ", "")
            ]
        )

    def decrypt(self, encrypted_message: str) -> str:
        """Decrypt the Encrypted Message using the Atbash Cipher"""
        return "".join(
            [
                self.alphabets[self.alphabets_reversed.index(letter)]
                for letter in encrypted_message.upper().replace(" ", "")
            ]
        )
