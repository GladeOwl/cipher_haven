import pytest
from cipher_haven.logic import affine


@pytest.mark.parametrize(
    "a, b, message, expected_output", [(5, 8, "AFFINE CIPHER", "IHHWVCSWFRCP")]
)
def test_encrypt(a: int, b: int, message: str, expected_output: str):
    cipher = affine.AFFINE(a, b)
    encryped_message = cipher.encrypt(message)
    assert encryped_message == expected_output


@pytest.mark.parametrize(
    "a, b, message, expected_output", [(5, 8, "IHHWVCSWFRCP", "AFFINECIPHER")]
)
def test_decrypt(a: int, b: int, message: str, expected_output: str):
    cipher = affine.AFFINE(a, b)
    decrypted_message = cipher.decrypt(message)
    assert decrypted_message == expected_output
