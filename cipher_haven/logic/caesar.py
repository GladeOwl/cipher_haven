"""Caesar Cipher"""

from string import ascii_uppercase
from cipher_haven.logic.cipher import CIPHER


class CAESAR(CIPHER):
    """Caesar Cipher Class"""

    def __init__(self, shift_right: bool, number: int) -> None:
        self.shift_right: bool = shift_right
        self.number: int = number

    def __shift_alphabets(self):
        if self.shift_right:
            return ascii_uppercase[self.number :] + ascii_uppercase[: self.number]
        return (
            ascii_uppercase[len(ascii_uppercase) - self.number :]
            + ascii_uppercase[: len(ascii_uppercase) - self.number]
        )

    def __get_new_message(self, message: str, shifted_alphabets: str):
        output_message: str = ""
        for letter in message:
            if letter == " ":
                output_message += " "
                continue

            index: int = ascii_uppercase.index(letter)
            output_message += shifted_alphabets[index]
        return output_message

    def encrypt(self, message: str) -> str:
        """Generate Table for the Caesar Cipher"""

        plaintext: str = message.upper()
        shifted_alphabets: str = self.__shift_alphabets()

        return self.__get_new_message(plaintext, shifted_alphabets)

    def decrypt(self, encrypted_message: str) -> str:
        """Generate Table for the Caesar Cipher"""

        self.shift_right = not self.shift_right

        encrypted_text: str = encrypted_message.upper()
        shifted_alphabets: str = self.__shift_alphabets()

        return self.__get_new_message(encrypted_text, shifted_alphabets)
