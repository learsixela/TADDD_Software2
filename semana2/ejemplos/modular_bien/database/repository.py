# ejemplos/modular_bien/database/repository.py
class InMemoryUserRepository:
    def __init__(self):
        self._users = []

    def save(self, name: str, email: str) -> None:
        self._users.append({"name": name, "email": email})
        print(f"[DB] Saved user {name}")
