""" Caesar Cipher Test Module """

import pytest
from cipher_haven.logic import caesar


@pytest.mark.parametrize(
    "message, shift_right, number, expected_output",
    [
        (
            "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG",
            False,
            3,
            "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD",
        )
    ],
)
def test_encrypt(message: str, shift_right: bool, number: int, expected_output: str):
    """Test the Caesar Cipher Class encrypt function"""

    cipher = caesar.CAESAR(shift_right, number)
    encrypted_message = cipher.encrypt(message)
    assert encrypted_message == expected_output


@pytest.mark.parametrize(
    "encrypted_message, shift_right, number, expected_output",
    [
        (
            "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD",
            False,
            3,
            "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG",
        )
    ],
)
def test_decrypt(
    encrypted_message: str, shift_right: bool, number: int, expected_output: str
):
    """Test the Caesar Cipher Class encrypt function"""

    cipher = caesar.CAESAR(shift_right, number)
    encrypted_message = cipher.decrypt(encrypted_message)
    assert encrypted_message == expected_output
