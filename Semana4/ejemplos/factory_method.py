# factory_method.py

class User:
    def __init__(self, email):
        self.email = email

class UserFactory:
    @staticmethod
    def create(email: str):
        print("[Factory] Validando email...")
        return User(email)

if __name__ == "__main__":
    user = UserFactory.create("lucas@heaven.com")
    print("Usuario creado:", user.email)
