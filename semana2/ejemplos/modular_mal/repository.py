# examples/modular_bad/repository.py
def save_user_to_db(name: str, email: str):
    print(f"[DB] INSERT INTO users(name, email) VALUES('{name}', '{email}')")
