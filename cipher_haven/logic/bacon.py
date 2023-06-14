""" Bacon's Cipher """

from cipher_haven.logic.cipher import CIPHER

CODE_TABLE: dict = {
    "A": "AAAAA",
    "B": "AAAAB",
    "C": "AAABA",
    "D": "AAABB",
    "E": "AABAA",
    "F": "AABAB",
    "G": "AABBA",
    "H": "AABBB",
    "I": "ABAAA",
    "J": "ABAAB",
    "K": "ABABA",
    "L": "ABABB",
    "M": "ABBAA",
    "N": "ABBAB",
    "O": "ABBBA",
    "P": "ABBBB",
    "Q": "BAAAA",
    "R": "BAAAB",
    "S": "BAABA",
    "T": "BAABB",
    "U": "BABAA",
    "V": "BABAB",
    "W": "BABBA",
    "X": "BABBB",
    "Y": "BBAAA",
    "Z": "BBAAB",
}


class BACON(CIPHER):
    """Bacon's Cipher Class"""

    def encrypt(self, message: str) -> str:
        """Encrypt the Message using the Bacon's Cipher"""

        plaintext: str = message.upper().replace(" ", "")
        encrypted_message: str = " ".join([CODE_TABLE[letter] for letter in plaintext])

        return encrypted_message

    def decrypt(self, encrypted_message: str) -> str:
        """Decrypt the Message using the Bacon's Cipher"""

        encrypted_message: str = encrypted_message.upper().replace(" ", "")

        message_list: list = [
            encrypted_message[i : i + 5] for i in range(0, len(encrypted_message), 5)
        ]

        letters: list = list(CODE_TABLE.keys())
        letter_codes: list = list(CODE_TABLE.values())

        decrypted_message: list = [
            letters[letter_codes.index(letter)] for letter in message_list
        ]

        return "".join(decrypted_message)
