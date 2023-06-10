""" Beaufort Cipher Test Module """

import pytest
from cipher_haven.logic import beaufort


@pytest.mark.parametrize(
    "message, key, expected_output",
    [("Where are we going", "pickle", "TBYTHEYEGGFQHVW")],
)
def test_encrypt(message: str, key: str, expected_output: str):
    """Test the Beaufort Cipher Class encrypt function"""

    cipher = beaufort.BEAUFORT()
    encrypted_message = cipher.encrypt(message, key)
    assert encrypted_message == expected_output


@pytest.mark.parametrize(
    "encryped_message, key, expected_output",
    [("TBYTHEYEGGFQHVW", "pickle", "WHEREAREWEGOING")],
)
def test_decrypt(encryped_message: str, key: str, expected_output: str):
    """Test the Beaufort Cipher Class encrypt function"""

    cipher = beaufort.BEAUFORT()
    encrypted_message = cipher.decrypt(encryped_message, key)
    assert encrypted_message == expected_output
