class MySQLDatabase:
    def connect(self):
        print("Connecting to MySQL...")

class UserService:
    def __init__(self):
        self.db = MySQLDatabase()  # Dependencia directa a una implementación
