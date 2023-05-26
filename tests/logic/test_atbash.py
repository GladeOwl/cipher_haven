""" Atbash Cipher Test Module """

import pytest
from cipher_haven.logic import atbash


@pytest.mark.parametrize("message, expected_output", [("How are we", "SLDZIVDV")])
def test_encrypt(message: str, expected_output: str):
    """Test the Atbash Cipher Class encrypt function"""
    cipher = atbash.ATBASH()
    encrypted_message = cipher.encrypt(message)
    assert encrypted_message == expected_output


@pytest.mark.parametrize(
    "encryped_message, expected_output", [("SLDZIVDV", "HOWAREWE")]
)
def test_decrypt(encryped_message: str, expected_output: str):
    """Test the Atbash Cipher Class encrypt function"""
    cipher = atbash.ATBASH()
    decrypted_message = cipher.decrypt(encryped_message)
    assert decrypted_message == expected_output
