# ejemplos/hexagonal_bien/infrastructure/in_memory_repository.py
from ..application.ports import UserRepositoryPort

class InMemoryUserRepository(UserRepositoryPort):
    def __init__(self):
        self._users = []

    def save(self, name: str, email: str) -> None:
        self._users.append({"name": name, "email": email})
        print(f"[DB:InMemory] Guardando usuario {name}")
