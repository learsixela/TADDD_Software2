# Monolito: todo en un archivo, sin separación de responsabilidades.
# Ejecuta: python app.py

def register_user(name: str, email: str):
    # Lógica de dominio mezclada con infraestructura (anti patrón en arquitecturas avanzadas)
    print(f"[DB] Guardando usuario {name} en DB...")
    # Simulación de inserción (sin persistencia real)
    print(f"[EMAIL] Enviando email de bienvenida a {email}...")
    return {"name": name, "email": email, "status": "created"}

if __name__ == "__main__":
    user = register_user("Israel", "ipalma@uct.cl")
    print("Result:", user)
