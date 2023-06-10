""" Beaufort Cipher """

from string import ascii_uppercase


class BEAUFORT:
    """Beaufort Cipher Class"""

    def encrypt(self, message: str, key: str) -> str:
        """Encrypt the Message using the Beaufort Cipher"""

        plaintext: str = message.upper().replace(" ", "")

        # TODO: Looks a bit weird. Can we change it?
        extended_key: str = (
            (key.upper() * (len(plaintext) - len(key)))[: len(plaintext)]
            if len(key) < len(plaintext)
            else key.upper()
        )

        cipher_values: list = []

        for i, _ in enumerate(plaintext):
            text_value: int = ascii_uppercase.index(plaintext[i])
            key_value: int = ascii_uppercase.index(extended_key[i])
            cipher_value: int = key_value - text_value

            if cipher_value < 0:
                cipher_value += 26

            cipher_values.append(cipher_value)

        return "".join(ascii_uppercase[x] for x in cipher_values)


cipher = BEAUFORT()
cipher.encrypt("Hello", "words")
