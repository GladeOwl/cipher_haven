""" Atbash Cipher """

from string import ascii_uppercase

ALPHABETS: list = list(ascii_uppercase)
ALPHABETS_REVERSED: list = list(reversed(ALPHABETS))


class ATBASH:
    """Atbash Cipher Class"""

    def encrypt(self, message: str) -> str:
        """Encrypt the Message using the Atbash Cipher"""

        plaintext: str = message.upper().replace(" ", "")
        return "".join(
            [ALPHABETS_REVERSED[ALPHABETS.index(letter)] for letter in plaintext]
        )

    def decrypt(self, encrypted_message: str) -> str:
        """Decrypt the Encrypted Message using the Atbash Cipher"""

        encrypted_text: str = encrypted_message.upper().replace(" ", "")
        return "".join(
            [ALPHABETS[ALPHABETS_REVERSED.index(letter)] for letter in encrypted_text]
        )
