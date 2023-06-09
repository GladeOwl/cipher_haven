""" Bacon's Cipher """

CODE_TABLE: dict = {
    "A": "aaaaa",
    "B": "aaaab",
    "C": "aaaba",
    "D": "aaabb",
    "E": "aabaa",
    "F": "aabab",
    "G": "aabba",
    "H": "aabbb",
    "I": "abaaa",
    "J": "abaab",
    "K": "ababa",
    "L": "ababb",
    "M": "abbaa",
    "N": "abbab",
    "O": "abbba",
    "P": "abbbb",
    "Q": "baaaa",
    "R": "baaab",
    "S": "baaba",
    "T": "baabb",
    "U": "babaa",
    "V": "babab",
    "W": "babba",
    "X": "babbb",
    "Y": "bbaaa",
    "Z": "bbaab",
}


class BACON:
    """Bacon's Cipher Class"""

    def __init__(self, A: str = "A", B: str = "B") -> None:
        if A == B:
            raise ValueError("A and B values cannot be the same")

        self.able = A
        self.baker = B

    def encrypt(self, message: str) -> str:
        """Encrypt the Message using the Bacon's Cipher"""
        plaintext: str = message.upper().replace(" ", "")
        return (
            " ".join([CODE_TABLE[letter].upper() for letter in plaintext])
            .replace("A", self.able)
            .replace("B", self.baker)
        )

    def decrypt(self, encrypted_message: str) -> str:
        """Decrypt the Message using the Bacon's Cipher"""
        encrypted_message: str = (
            encrypted_message.upper()
            .replace(" ", "")
            .replace("A", self.able)
            .replace("B", self.baker)
        )

        if len(encrypted_message) % 5 != 0:
            raise ValueError("Please input a valid encrypted message")

        message_list: list = [
            encrypted_message[i : i + 5] for i in range(0, len(encrypted_message), 5)
        ]

        letters: list = list(CODE_TABLE.keys())
        letter_codes: list = list(CODE_TABLE.values())

        decrypted_message: list = [
            letters[letter_codes.index(x.lower())] for x in message_list
        ]
        return "".join(decrypted_message)
