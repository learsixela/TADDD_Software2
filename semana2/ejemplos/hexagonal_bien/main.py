# ejemplos/hexagonal_bien/main.py
from infrastructure.in_memory_repository import InMemoryUserRepository
from infrastructure.console_email import ConsoleEmailService
from application.use_cases import RegisterUserUseCase

def main():
    repo = InMemoryUserRepository()
    email = ConsoleEmailService()
    use_case = RegisterUserUseCase(repo, email)
    use_case.execute("Israel", "ipalma@uct.cl")

if __name__ == "__main__":
    main()
