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
    print(encrypted_message, "|", expected_ouput)
    assert encrypted_message == expected_ouput
