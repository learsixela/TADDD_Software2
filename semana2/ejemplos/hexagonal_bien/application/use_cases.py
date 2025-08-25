# ejemplos/hexagonal_bien/application/use_cases.py
from .ports import UserRepositoryPort, EmailServicePort

class RegisterUserUseCase:
    def __init__(self, repo: UserRepositoryPort, email: EmailServicePort):
        self.repo = repo
        self.email = email

    def execute(self, name: str, email: str) -> None:
        # Aquí podría ir validación de dominio, reglas, etc.
        self.repo.save(name, email)
        self.email.send(email, "¡Bienvenido/a a la app hexagonal uct!")
