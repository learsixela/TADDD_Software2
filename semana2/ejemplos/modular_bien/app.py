# ejemplos/modular_bien/app.py
# Modular "bien": separa responsabilidades por paquetes, "pero" sigue siendo un monolito.

from services.user_service import UserService
from database.repository import InMemoryUserRepository
from services.email_service import ConsoleEmailService

if __name__ == "__main__":
    repo = InMemoryUserRepository()
    email = ConsoleEmailService()
    service = UserService(repo, email)
    service.register_user("Israel", "ipalma@uct.cl")
