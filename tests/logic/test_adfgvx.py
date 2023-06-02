""" ADFGVX Cipher Test Module """

import pytest
from cipher_haven.logic import adfgvx


@pytest.mark.parametrize(
    "table_code, message, transpose_key, expected_output",
    [
        (
            "nachtbommenwerper",
            "attack at 1200am",
            "privacy",
            "DGDD DAGD DGAF ADDF DADV DVFA ADVX",
        )
    ],
)
def test_encrypt(
    table_code: str, message: str, transpose_key: str, expected_output: str
):
    """Test the ADFGVX Cipher Class encrypt function"""

    cipher = adfgvx.ADFGVX(transpose_key)
    cipher.generate_table(table_code)
    encrypted_message = cipher.encrypt(message)
    assert encrypted_message == expected_output


@pytest.mark.parametrize(
    "table_code, encryped_message, transpose_key, expected_output",
    [
        (
            "nachtbommenwerper",
            "DGDD DAGD DGAF ADDF DADV DVFA ADVX",
            "privacy",
            "attackat1200am",
        )
    ],
)
def test_decrypt(
    table_code: str, encryped_message: str, transpose_key: str, expected_output: str
):
    """Test the ADFGVX Cipher Class decrypt function"""

    cipher = adfgvx.ADFGVX(transpose_key)
    cipher.generate_table(table_code)
    decrypted_message = cipher.decrypt(encryped_message)
    assert decrypted_message == expected_output
