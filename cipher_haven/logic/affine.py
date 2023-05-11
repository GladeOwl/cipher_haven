from string import ascii_uppercase


class AFFINE:
    def __init__(self, a: int = 5, b: int = 8) -> None:
        coprime_list: list = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
        if a not in coprime_list:
            raise ValueError(
                f"Given number is not a co-prime of 26, it must be in the list: {coprime_list}"
            )

        self.a: int = a
        self.b: int = b
        self.m: int = 26  # Number of alphabets in the english language

    def encrypt(self, message: str) -> str:
        plaintext: str = message.upper().replace(" ", "")

        encrypted_message: str = ""
        for letter in plaintext:
            print(letter)
            x: int = ascii_uppercase.index(letter)
            letter_key: int = (self.a * x + self.b) % self.m
            encrypted_message += ascii_uppercase[letter_key]

        return encrypted_message

    def __find_modulor_multiplicative_inverse(self):
        for x in range(1, self.m):
            if ((self.a % self.m) * (x % self.m)) % self.m == 1:
                return x
        return -1

    def decrypt(self, encryped_message: str) -> str:
        a_inverse: int = self.__find_modulor_multiplicative_inverse()
        decrypted_message: str = ""

        for letter in encryped_message:
            x: int = ascii_uppercase.index(letter)
            letter_key: int = a_inverse * (x - self.b) % self.m
            decrypted_message += ascii_uppercase[letter_key]

        return decrypted_message
