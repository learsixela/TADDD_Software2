# ejemplos/hexagonal_bien/application/ports.py
from abc import ABC, abstractmethod

class UserRepositoryPort(ABC):
    @abstractmethod
    def save(self, name: str, email: str) -> None: ...

class EmailServicePort(ABC):
    @abstractmethod
    def send(self, to: str, message: str) -> None: ...
