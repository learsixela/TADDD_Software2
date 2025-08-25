# ejemplos/hexagonal_mal/app.py
# Anti-ejemplo: la lógica de aplicación conoce detalles de infraestructura.
class MySQLRepository:
    def save(self, name: str, email: str):
        print(f"[MySQL] Insertando usuario {name}")

class SmtpEmail:
    def send(self, to: str, message: str):
        print(f"[SMTP] Enviando a {to}: {message}")

# Caso de uso (acoplado a MySQL y SMTP)
def register_user(name: str, email: str):
    repo = MySQLRepository()     # dependencia concreta
    emailer = SmtpEmail()        # dependencia concreta
    repo.save(name, email)
    emailer.send(email, "¡Bienvenido/a!")

if __name__ == "__main__":
    register_user("Israel", "ipalma@uct.cl")
