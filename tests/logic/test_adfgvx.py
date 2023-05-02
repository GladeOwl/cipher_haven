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
    cipher = adfgvx.ADFGVX()
    cipher.generate_table(table_code)
    encrypted_message = cipher.encrypt(message, transpose_key)
    assert encrypted_message == expected_output


@pytest.mark.parametrize(
    "table_code, encryped_message, transpose_key, expected_output",
    [
        (
            "nachtbommenwerper",
            "DGDD DAGD DGAF ADDF DADV DVFA ADVX",
            "privacy",
            "attack at 1200am",
        )
    ],
)
def test_decrypt(
    table_code: str, encryped_message: str, transpose_key: str, expected_output: str
):
    cipher = adfgvx.ADFGVX()
    cipher.generate_table(table_code)
    decrypted_message = cipher.decrypt(encryped_message, transpose_key)
    assert decrypted_message == expected_output
