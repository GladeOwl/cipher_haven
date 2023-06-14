""" Bifid Cipher Test Module """

import pytest
from cipher_haven.logic import bifid


@pytest.mark.parametrize(
    "message, table_code, block_size, expected_output",
    [("Where are we going", "Johnson", 5, "REFMNNEGN1BIGBX")],
)
def test_encrypt(message: str, table_code: str, block_size: int, expected_output: str):
    """Test the Beaufort Cipher Class encrypt function"""

    cipher = bifid.BIFID(table_code, block_size)
    encrypted_message = cipher.encrypt(message)
    assert encrypted_message == expected_output


@pytest.mark.parametrize(
    "encryped_message, table_code, block_size, expected_output",
    [
        ("REFMNNEGN1BIGBX", "Johnson", 5, "WHEREAREWEGOING"),
        ("QISF0DJPEYUWZ2IWRBJ2BW8N", "Worker", 5, "SOMETHINGISVERYWRONGHERE"),
    ],
)
def test_decrypt(
    encryped_message: str, table_code: str, block_size: int, expected_output: str
):
    """Test the Beaufort Cipher Class decrypt function"""

    cipher = bifid.BIFID(table_code, block_size)
    encrypted_message = cipher.decrypt(encryped_message)
    assert encrypted_message == expected_output
