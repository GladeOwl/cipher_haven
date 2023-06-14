""" Bacon's Cipher Test Module """

import pytest
from cipher_haven.logic import bacon


@pytest.mark.parametrize(
    "message, expected_ouput",
    [
        (
            "Hello There",
            "AABBB AABAA ABABB ABABB ABBBA BAABB AABBB AABAA BAAAB AABAA",
        )
    ],
)
def test_encrypt(message: str, expected_ouput: str):
    """Test the Bacon's Cipher Class encrypt function"""
    cipher = bacon.BACON()
    encrypted_message = cipher.encrypt(message)
    assert encrypted_message == expected_ouput


@pytest.mark.parametrize(
    "encrypted_message, expected_ouput",
    [
        (
            "AABBB AABAA ABABB ABABB ABBBA BAABB AABBB AABAA BAAAB AABAA",
            "HELLOTHERE",
        )
    ],
)
def test_decrypt(encrypted_message: str, expected_ouput: str):
    """Test the Bacon's Cipher Class encrypt function"""
    cipher = bacon.BACON()
    decrypted_message = cipher.decrypt(encrypted_message)
    assert decrypted_message == expected_ouput
