# examples/modular_bad/app.py
# Modular "malo": hay módulos, pero el servicio depende de implementaciones concretas.
from services import user_service  # depende de implementaciones concretas dentro del módulo

if __name__ == "__main__":
    user_service.register_user("Israel", "israel@example.com")
