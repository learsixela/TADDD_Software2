# ejemplo/modular_bien/services/email_service.py
class ConsoleEmailService:
    def send(self, to: str, message: str) -> None:
        print(f"[EMAIL] Para: {to} | {message}")
