# examples/modular_bad/services.py
# Servicio fuertemente acoplado a infraestructura concreta => difícil de testear/cambiar
from repository import save_user_to_db
from emailer import send_email

def register_user(name: str, email: str):
    save_user_to_db(name, email)  # dependencia concreta
    send_email(email, "¡Bienvenido/a!")
