# Taller en Grupo : Identificar y Refactorizar Violaciones a SOLID

**Objetivo.** Identificar qué principios SOLID se violan en cada escenario y refactorizar el código aplicándolos.  

## Plan sugerido
### **60 min**: 
- Lectura de escenarios y asignación de roles.
- Refactorización (al menos 3 escenarios).
- Preparar explicación y subir su solución a repositorio de grupo.
---

## Escenario 1 — SRP (Responsabilidad Única)

```python
# ANTES (SRP)
import json
from datetime import datetime

class ReportManager:
    def run_report(self):
        # cargar datos
        data = {"ventas": 1200, "fecha": str(datetime.now())}

        # formatear
        text = f"REPORTE: ventas={data['ventas']} fecha={data['fecha']}"

        # persistir
        with open("reporte.txt", "w", encoding="utf-8") as f:
            f.write(text)

        # presentar
        print(text)

if __name__ == "__main__":
    ReportManager().run_report()
```
Tarea.
- Indica por qué viola SRP (múltiples motivos de cambio).

- Refactoriza separando: DataSource, Formatter, Output (archivo/console) y un servicio que orqueste.

---


## Escenario 2 — OCP (Abierto/Cerrado)
```python
# ANTES (OCP)
class PaymentProcessor:
    def process(self, payment_type: str, amount: float):
        if payment_type == "cash":
            print(f"Efectivo: {amount}")
        elif payment_type == "card":
            print(f"Tarjeta: {amount}")
        elif payment_type == "transfer":
            print(f"Transferencia: {amount}")
        else:
            raise ValueError("Tipo no soportado")

if __name__ == "__main__":
    PaymentProcessor().process("card", 100.0)

```
Tarea
- Explica por qué viola OCP.

- Refactoriza usando polimorfismo/estrategia: interfaz PaymentMethod con implementaciones (Cash, Card, …).

---

## Escenario 3 — LSP (Sustitución de Liskov)
```python
# ANTES (LSP)
class Rectangle:
    def __init__(self):
        self._w = 0
        self._h = 0

    def set_width(self, w: int):
        self._w = w

    def set_height(self, h: int):
        self._h = h

    def area(self) -> int:
        return self._w * self._h

class Square(Rectangle):
    # forzar lados iguales rompe a clientes que esperan set_width/set_height independientes
    def set_width(self, w: int):
        self._w = w
        self._h = w

    def set_height(self, h: int):
        self._h = h
        self._w = h

def compute_area(rect: Rectangle) -> int:
    rect.set_width(5)
    rect.set_height(10)  # en Square esto cambia ambos lados
    return rect.area()

if __name__ == "__main__":
    print(compute_area(Rectangle()))  # 50
    print(compute_area(Square()))     # 100 (sorpresa)
```
Tareas.

- Describe el quiebre de LSP.

- Refactoriza evitando herencia inapropiada: usa una abstracción Shape(forma) y clases independientes (Rect, Square) o composición.

- Ajusta compute_area para depender de la abstracción adecuada.

---

## Escenario 4 — ISP (Segregación de Interfaces)
``` python
# ANTES (ISP)
from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self) -> None: ...
    @abstractmethod
    def eat(self) -> None: ...
    @abstractmethod
    def attend_meeting(self) -> None: ...

class Robot(Worker):
    def work(self) -> None:
        print("Produciendo")
    def eat(self) -> None:
        raise NotImplementedError("Un robot no come")
    def attend_meeting(self) -> None:
        print("¿Tiene sentido que un robot asista?")

if __name__ == "__main__":
    Robot().eat()  # explota/absurdo

```
Tareas.

- Explica por qué viola ISP.

- Divide en contratos pequeños (Workable, Eatable, Attendee) y aplica solo lo necesario en cada implementación.
---
## Escenario 5 — DIP (Inversión de Dependencias)
``` python
# ANTES (DIP)
class EmailSender:
    def send(self, to: str, msg: str) -> None:
        print(f"SMTP -> {to}: {msg}")

class OrderService:
    def __init__(self):
        self.email = EmailSender()  # dependencia rígida a un detalle

    def place_order(self, to: str, msg: str) -> None:
        # ... lógica de orden ...
        self.email.send(to, msg)

if __name__ == "__main__":
    OrderService().place_order("user@test.com", "Gracias por su compra")
```
Tareas.

- Señala cómo esto dificulta pruebas y cambios (p. ej., SMS, Push).

- Refactoriza definiendo una abstracción Notifier e inyecta la implementación por constructor.


