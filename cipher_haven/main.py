"""Main CLI Module"""

from typer import Typer, Argument, Option
from rich.console import Console
import cipher_haven.logic as logic

CONSOLE: Console = Console()

app = Typer()


@app.command()
def adfgvx(
    message: str = Argument(..., help="The message you wish to encrypt or decrypt"),
    table_code: str = Argument(..., help="Single Word with No Numbers. e.g. wonderful"),
    transpose_key: str = Argument(..., help="Single Word with No Numbers. e.g. apple"),
    encrypt: bool = Option(True, help="--no-encrypt to Decrypt instead"),
):
    """Encrypt or Decrypt message using the ADFGVX Cipher"""

    cipher = logic.adfgvx.ADFGVX(transpose_key, table_code)
    output_message: str = (
        cipher.encrypt(message) if encrypt else cipher.decrypt(message)
    )
    CONSOLE.print(output_message)
    return output_message



if __name__ == "__main__":
    app()
