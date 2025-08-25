# ejemplos/hexagonal_bien/domain/entities.py
# En un caso real, aquí irían Entidades y Value Objects de DDD.
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
