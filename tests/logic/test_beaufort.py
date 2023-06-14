""" Beaufort Cipher Test Module """

import pytest
from cipher_haven.logic import beaufort


@pytest.mark.parametrize(
    "message, key, expected_output",
    [("Where are we going", "pickle", "TBYTHEYEGGFQHVW")],
)
def test_encrypt(message: str, key: str, expected_output: str):
    """Test the Beaufort Cipher Class encrypt function"""

    cipher = beaufort.BEAUFORT(key)
    encrypted_message = cipher.encrypt(message)
    assert encrypted_message == expected_output


@pytest.mark.parametrize(
    "encryped_message, key, expected_output",
    [("TBYTHEYEGGFQHVW", "pickle", "WHEREAREWEGOING")],
)
def test_decrypt(encryped_message: str, key: str, expected_output: str):
    """Test the Beaufort Cipher Class encrypt function"""

    cipher = beaufort.BEAUFORT(key)
    encrypted_message = cipher.decrypt(encryped_message)
    assert encrypted_message == expected_output
