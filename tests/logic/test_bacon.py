""" Bacon's Cipher Test Module """

import pytest
from cipher_haven.logic import bacon


@pytest.mark.parametrize(
    "message, A, B, expected_ouput",
    [
        (
            "Hello There",
            "A",
            "B",
            "AABBB AABAA ABABB ABABB ABBBA BAABB AABBB AABAA BAAAB AABAA",
        )
    ],
)
def test_encrypt(message: str, A: str, B: str, expected_ouput: str):
    """Test the Bacon's Cipher Class encrypt function"""
    cipher = bacon.BACON(A, B)
    encrypted_message = cipher.encrypt(message)
    assert encrypted_message == expected_ouput


@pytest.mark.parametrize(
    "encrypted_message, A, B, expected_ouput",
    [
        (
            "AABBB AABAA ABABB ABABB ABBBA BAABB AABBB AABAA BAAAB AABAA",
            "A",
            "B",
            "HELLOTHERE",
        )
    ],
)
def test_decrypt(encrypted_message: str, A: str, B: str, expected_ouput: str):
    """Test the Bacon's Cipher Class encrypt function"""
    cipher = bacon.BACON(A, B)
    decrypted_message = cipher.decrypt(encrypted_message)
    assert decrypted_message == expected_ouput
