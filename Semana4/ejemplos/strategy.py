# strategy.py

from abc import ABC, abstractmethod

class PasswordStrategy(ABC):
    @abstractmethod
    def validate(self, password: str) -> bool:
        pass

class SimplePasswordStrategy(PasswordStrategy):
    def validate(self, password: str) -> bool:
        return len(password) >= 4

class StrongPasswordStrategy(PasswordStrategy):
    def validate(self, password: str) -> bool:
        return (
            len(password) >= 8
            and any(c.isupper() for c in password)
            and any(c.islower() for c in password)
            and any(c.isdigit() for c in password)
        )

class Authenticator:
    def __init__(self, strategy: PasswordStrategy):
        self.strategy = strategy

    def login(self, email: str, password: str) -> bool:
        if self.strategy.validate(password):
            print(f"[Auth] Usuario {email} autenticado correctamente")
            return True
        print(f"[Auth] Password inválido para {email}")
        return False

if __name__ == "__main__":
    simple_auth = Authenticator(SimplePasswordStrategy())
    simple_auth.login("pedro@heaven.com", "1234")

    strong_auth = Authenticator(StrongPasswordStrategy())
    strong_auth.login("pedro@heaven.com", "Fuerte123")
