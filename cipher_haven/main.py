"""Main CLI Module"""

from typer import Typer, Argument, Option
from rich.console import Console
from cipher_haven import logic


app = Typer()

MESSAGE_HELP_TEXT = "The message you wish to encrypt or decrypt"
ENCRYPT_HELP_TEXT = "--decrypt to Decrypt instead"
KEYWORD_HELP_TEXT = "Single Word with No Numbers. e.g. apple"

ENCRYPT_BOOL = "--encrypt/--decrypt"


def print_output(cipher, message: str, encrypt: bool):
    """Print the Output of the Cipher Module"""

    output_message: str = (
        cipher.encrypt(message) if encrypt else cipher.decrypt(message)
    )

    console: Console = Console()
    console.print(output_message)


@app.command()
def adfgvx(
    message: str = Argument(..., help=MESSAGE_HELP_TEXT),
    table_code: str = Argument(..., help="Single Word with No Numbers. e.g. wonderful"),
    transpose_key: str = Argument(..., help=KEYWORD_HELP_TEXT),
    encrypt: bool = Option(True, ENCRYPT_BOOL, help=ENCRYPT_HELP_TEXT),
):
    """Encrypt or Decrypt message using the ADFGVX Cipher"""

    cipher = logic.adfgvx.ADFGVX(transpose_key, table_code)
    print_output(cipher, message, encrypt)


@app.command()
def affine(
    message: str = Argument(..., help=MESSAGE_HELP_TEXT),
    alpha: int = Option(
        5,
        help="Must be a co-prime of 26, e.g. 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23 or 25",
    ),
    beta: int = Option(8, help="Random Integer"),
    encrypt: bool = Option(True, ENCRYPT_BOOL, help=ENCRYPT_HELP_TEXT),
):
    """Encrypt or Decrypt message using the Affine Cipher"""

    cipher = logic.affine.AFFINE(alpha, beta)
    print_output(cipher, message, encrypt)


@app.command()
def alphabet(
    message: str = Argument(..., help=MESSAGE_HELP_TEXT),
    keyword: str = Argument(..., help=KEYWORD_HELP_TEXT),
    encrypt: bool = Option(True, ENCRYPT_BOOL, help=ENCRYPT_HELP_TEXT),
):
    """Encrypt or Decrypt message using the Alphabet Cipher"""

    cipher = logic.alphabet.ALPHABET(keyword)
    print_output(cipher, message, encrypt)


@app.command()
def atbash(
    message: str = Argument(..., help=MESSAGE_HELP_TEXT),
    encrypt: bool = Option(True, ENCRYPT_BOOL, help=ENCRYPT_HELP_TEXT),
):
    """Encrypt or Decrypt message using the Atbash Cipher"""

    cipher = logic.atbash.ATBASH()
    print_output(cipher, message, encrypt)


@app.command()
def autokey(
    message: str = Argument(..., help=MESSAGE_HELP_TEXT),
    keyword: str = Argument(..., help=KEYWORD_HELP_TEXT),
    encrypt: bool = Option(True, ENCRYPT_BOOL, help=ENCRYPT_HELP_TEXT),
):
    """Encrypt or Decrypt message using the Autokey Cipher"""

    cipher = logic.autokey.AUTOKEY(keyword)
    print_output(cipher, message, encrypt)


@app.command()
def bacon(
    message: str = Argument(..., help=MESSAGE_HELP_TEXT),
    encrypt: bool = Option(True, ENCRYPT_BOOL, help=ENCRYPT_HELP_TEXT),
):
    """Encrypt or Decrypt message using the Bacon Cipher"""

    cipher = logic.bacon.BACON()
    print_output(cipher, message, encrypt)


@app.command()
def beaufort(
    message: str = Argument(..., help=MESSAGE_HELP_TEXT),
    keyword: str = Argument(..., help=KEYWORD_HELP_TEXT),
    encrypt: bool = Option(True, ENCRYPT_BOOL, help=ENCRYPT_HELP_TEXT),
):
    """Encrypt or Decrypt message using the Beaufort Cipher"""

    cipher = logic.beaufort.BEAUFORT(keyword)
    print_output(cipher, message, encrypt)


if __name__ == "__main__":
    app()
