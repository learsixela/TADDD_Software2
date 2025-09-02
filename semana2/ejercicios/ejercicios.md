# Desafío: Clean Architecture & DDD (Lightweight) — Login

Diseña e implementa un **módulo de Login** aplicando **Clean Architecture** y **DDD (ligero)**:
- Dominio independiente de frameworks y de la base de datos
- Casos de uso que dependen de **puertos (interfaces)**
- Adaptadores (infraestructura) que implementan esos puertos
- Pruebas unitarias de casos de uso

---

## Propósito
Modelar un flujo de **autenticación** simple:
- Registrar usuario (con email único y contraseña segura)
- Iniciar sesión (validación de credenciales)
- Cerrar sesión (opcional)
- (Opcional) Emitir token de sesión simple

> **Nivel:** 1º año – Enfoque en separar capas y respetar contratos. No es necesario un servidor web, puede ser CLI.  

---

## Dominio y Lenguaje Ubicuo
- **Usuario**: entidad con `id`, `email`, `password_hash`, `created_at`.
- **Credenciales**: value object (`email`, `password_plano`) usado solo para validación de ingreso.
- **Repositorio de Usuarios (UserRepository)**: puerto para persistir y buscar usuarios.
- **PasswordHasher**: puerto para hashear y verificar contraseñas.
- **TokenService** (opcional): puerto para emitir/verificar tokens de sesión.

---

## Requerimientos Funcionales
1. **Registro de usuario**
   - Debe validar que el **email sea único**.
   - Debe **hashear** la contraseña antes de guardar.
   - Devuelve el usuario creado (sin exponer el hash).

2. **Login**
   - Debe buscar por email y **verificar contraseña** con el hasher.
   - Si las credenciales son válidas, devolver **éxito** y (opcional) **token**.
   - Si no son válidas, devolver error controlado.

3. **(Opcional) Logout**
   - Invalidar token o marcar sesión como cerrada (en memoria).

4. **Listar usuarios** (sólo para demo / pruebas)
   - Devolver lista sin `password_hash`.

---

## Requisitos de Arquitectura (Obligatorios)
- **Dominio (core)** sin imports de infraestructura.
- **Casos de uso** que dependen de puertos (`UserRepository`, `PasswordHasher`, `TokenService?`).
- **Adaptadores** que implementan esos puertos (`InMemoryUserRepository`, `SimplePasswordHasher`, `InMemoryTokenService?`).
- **UI mínima** (CLI o script `main.py`) que **ensambla** adaptadores + casos de uso.
- **Pruebas unitarias** de casos de uso con **dobles** (fakes/mocks) de los puertos.

> **Prohibido:** que casos de uso importen `sqlite3`, `bcrypt`, `jwt`, etc.  
> **Permitido:** usar esas libs **solo en adaptadores** (si decides implementarlos).

---
