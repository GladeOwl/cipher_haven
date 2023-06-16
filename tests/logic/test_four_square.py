""" Four-square Cipher Test Module """

import pytest
from cipher_haven.logic import four_square


@pytest.mark.parametrize(
    "message, key1, key2, expected_output",
    [("Hey There", "fantastic", "rechnung", "EC YS EC UE")],
)
def test_encrypt(message: str, key1: str, key2: str, expected_output: str):
    """Test the Four-square Cipher Class encrypt function"""

    cipher = four_square.FOURSQUARE(key1, key2)
    encrypted_message = cipher.encrypt(message)
    assert encrypted_message == expected_output


@pytest.mark.parametrize(
    "encrypted_message, key1, key2, expected_output",
    [("EC YS EC UE", "fantastic", "rechnung", "HEYTHERE")],
)
def test_decrypt(encrypted_message: str, key1: str, key2: str, expected_output: str):
    """Test the Four-square Cipher Class decrypt function"""

    cipher = four_square.FOURSQUARE(key1, key2)
    decrypted_message = cipher.decrypt(encrypted_message)
    assert decrypted_message == expected_output
