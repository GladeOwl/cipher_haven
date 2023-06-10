""" Beaufort Cipher """

from string import ascii_uppercase


class BEAUFORT:
    """Beaufort Cipher Class"""

    def __extend_key(self, message: str, key: str) -> str:
        # TODO: Looks a bit weird. Can we change it?
        return (
            (key.upper() * (len(message) - len(key)))[: len(message)]
            if len(key) < len(message)
            else key.upper()
        )

    def __process_cipher(self, message: str, key: str) -> list:
        cipher_values: list = []

        for i, _ in enumerate(message):
            text_value: int = ascii_uppercase.index(message[i])
            key_value: int = ascii_uppercase.index(key[i])
            cipher_value: int = key_value - text_value

            if cipher_value < 0:
                cipher_value += 26

            cipher_values.append(cipher_value)

        return cipher_values

    def encrypt(self, message: str, key: str) -> str:
        """Encrypt the Message using the Beaufort Cipher"""

        plaintext: str = message.upper().replace(" ", "")
        extended_key: str = self.__extend_key(plaintext, key)

        cipher_values: list = self.__process_cipher(plaintext, extended_key)
        return "".join(ascii_uppercase[x] for x in cipher_values)

    def decrypt(self, encrypted_message: str, key: str) -> str:
        """Decrypt the Message using the Beaufort Cipher"""

        encrypted_text: str = encrypted_message.upper().replace(" ", "")
        extended_key: str = self.__extend_key(encrypted_text, key)

        cipher_values: list = self.__process_cipher(encrypted_text, extended_key)
        return "".join(ascii_uppercase[x] for x in cipher_values)
