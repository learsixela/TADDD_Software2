# ejemplos/modular_bien/services/user_service.py
from typing import Protocol

class UserRepository(Protocol):
    def save(self, name: str, email: str) -> None: ...

class EmailService(Protocol):
    def send(self, to: str, message: str) -> None: ...

class UserService:
    def __init__(self, repo: UserRepository, email: EmailService):
        self.repo = repo
        self.email = email

    def register_user(self, name: str, email: str) -> None:
        self.repo.save(name, email)
        self.email.send(email, "¡Bienvenido/a!")
        print("[APP] Usuario registrado")
