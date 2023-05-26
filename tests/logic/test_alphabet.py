""" Alphabet Cipher Test Module """

import pytest
from cipher_haven.logic import alphabet


@pytest.mark.parametrize(
    "message, keyword, expected_output",
    [
        (
            "meet me on Tuesday evening at seven",
            "vigilance",
            "hmkbxebpxpmyllyrxiiqtoltfgzzv",
        )
    ],
)
def test_encrypt(message: str, keyword: str, expected_output: str):
    """Test the Alphabet Cipher Class encrypt function"""

    cipher = alphabet.ALPHABET()
    encrypted_message = cipher.encrypt(message, keyword)
    assert encrypted_message == expected_output


@pytest.mark.parametrize(
    "encrypted_message, keyword, expected_output",
    [
        (
            "hmkbxebpxpmyllyrxiiqtoltfgzzv",
            "vigilance",
            "MEETMEONTUESDAYEVENINGATSEVEN",
        )
    ],
)
def test_decrypt(encrypted_message: str, keyword: str, expected_output: str):
    """Test the Alphabet Cipher Class decrypt function"""

    cipher = alphabet.ALPHABET()
    decrypted_message = cipher.decrypt(encrypted_message, keyword)
    assert decrypted_message == expected_output
