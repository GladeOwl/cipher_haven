import pytest
from cipher_haven.logic import adfgvx


@pytest.mark.parametrize(
    "table_code, message, code_key, expected_output",
    [
        (
            "nachtbommenwerper",
            "attack at 1200am",
            "privacy",
            "DGDD DAGD DGAF ADDF DADV DVFA ADVX",
        )
    ],
)
def test_cipher_run(table_code: str, message: str, code_key: str, expected_output: str):
    cipher = adfgvx.ADFGVX()
    cipher.generate_table(table_code)
    plaintext = cipher.encrypt(message, code_key)
    assert plaintext == expected_output
