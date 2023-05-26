""" Autokey Cipher Test Module """

import pytest
from cipher_haven.logic import autokey


@pytest.mark.parametrize(
    "message, key, expected_output", [("attack at dawn", "QUEENLY", "QNXEPVYTWTWP")]
)
def test_encrypt(message: str, key: str, expected_output: str):
    """Test the Autokey Cipher Class encrypt function"""
    cipher = autokey.AUTOKEY()
    encrypted_message = cipher.encrypt(message, key)
    assert encrypted_message == expected_output
