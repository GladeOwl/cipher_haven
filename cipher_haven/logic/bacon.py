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
