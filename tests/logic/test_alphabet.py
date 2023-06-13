""" Alphabet Cipher Test Module """

import pytest
from cipher_haven.logic import alphabet


@pytest.mark.parametrize(
    "message, keyword, expected_output",
    [
        (
            "meet me on Tuesday evening at seven",
            "vigilance",
            "HMKBXEBPXPMYLLYRXIIQTOLTFGZZV",
        )
    ],
)
def test_encrypt(message: str, keyword: str, expected_output: str):
    """Test the Alphabet Cipher Class encrypt function"""

    cipher = alphabet.ALPHABET(keyword)
    encrypted_message = cipher.encrypt(message)
    assert encrypted_message == expected_output


@pytest.mark.parametrize(
    "encrypted_message, keyword, expected_output",
    [
        (
            "HMKBXEBPXPMYLLYRXIIQTOLTFGZZV",
            "vigilance",
            "MEETMEONTUESDAYEVENINGATSEVEN",
        )
    ],
)
def test_decrypt(encrypted_message: str, keyword: str, expected_output: str):
    """Test the Alphabet Cipher Class decrypt function"""

    cipher = alphabet.ALPHABET(keyword)
    decrypted_message = cipher.decrypt(encrypted_message)
    assert decrypted_message == expected_output
