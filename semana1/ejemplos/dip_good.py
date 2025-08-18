class Database:
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL...")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connecting to PostgreSQL...")

class UserService:
    def __init__(self, db: Database):
        self.db = db

    def start(self):
        self.db.connect()

# Uso
UserService(MySQLDatabase()).start()
UserService(PostgreSQLDatabase()).start()
