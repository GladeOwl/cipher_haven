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
