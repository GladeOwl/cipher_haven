"""Base Cipher Module"""
from abc import ABC, abstractmethod


class CIPHER(ABC):
    """Base Cipher Class"""

    @abstractmethod
    def encrypt(self, message: str) -> str:
        """Base Encrypt Function"""

    @abstractmethod
    def decrypt(self, encrypted_message: str) -> str:
        """Base Decrypt Function"""
