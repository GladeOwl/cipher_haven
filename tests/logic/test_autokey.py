""" Autokey Cipher Test Module """

import pytest
from cipher_haven.logic import autokey


@pytest.mark.parametrize(
    "message, key, expected_output",
    [
        ("attack at dawn", "QUEENLY", "QNXEPVYTWTWP"),
        ("meetatthefountain", "kilt", "WMPMMXXAEYHBRYOCA"),
    ],
)
def test_encrypt(message: str, key: str, expected_output: str):
    """Test the Autokey Cipher Class encrypt function"""

    cipher = autokey.AUTOKEY(key)
    encrypted_message = cipher.encrypt(message)
    assert encrypted_message == expected_output


@pytest.mark.parametrize(
    "encrypted_message, key, expected_output",
    [
        ("QNXEPVYTWTWP", "QUEENLY", "ATTACKATDAWN"),
        ("WMPMMXXAEYHBRYOCA", "kilt", "MEETATTHEFOUNTAIN"),
    ],
)
def test_decrypt(encrypted_message: str, key: str, expected_output: str):
    """Test the Autokey Cipher Class decrypt function"""

    cipher = autokey.AUTOKEY(key)
    encrypted_message = cipher.decrypt(encrypted_message)
    assert encrypted_message == expected_output
