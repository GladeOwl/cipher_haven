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
    cipher = alphabet.ALPHABET()
    encryped_message = cipher.encrypt(message, keyword)
    assert encryped_message == expected_output
