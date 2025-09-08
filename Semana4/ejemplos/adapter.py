# adapter.py

class EmailServicePort:
    def send(self, to: str, message: str):
        raise NotImplementedError

# Adaptador concreto
class SmtpAdapter(EmailServicePort):
    def send(self, to: str, message: str):
        print(f"[SMTP] Enviando email a {to}: {message}")

# Otro adaptador
class ConsoleAdapter(EmailServicePort):
    def send(self, to: str, message: str):
        print(f"[Console] Email -> {to}: {message}")

if __name__ == "__main__":
    smtp = SmtpAdapter()
    smtp.send("juan@heaven.com", "Bienvenida!")

    console = ConsoleAdapter()
    console.send("juan@heaven.com", "Hola desde consola!")
