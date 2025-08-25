# ejemplos/hexagonal_bien/infrastructure/console_email.py
from ..application.ports import EmailServicePort

class ConsoleEmailService(EmailServicePort):
    def send(self, to: str, message: str) -> None:
        print(f"[EMAIL:Consola] Para: {to} | {message}")
