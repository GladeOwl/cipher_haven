class ABERTI:
    def __init__(self) -> None:
        self.stationary_disk: str = "ABCDEFGILMNOPQRSTVXZ1234"
        self.movable_disk: str = "gklnprtuz&xysomqihfdbace"

    def encrypt(self, message: str, index: str) -> str:
        plaintext: str = message.upper().replace(" ", "")
