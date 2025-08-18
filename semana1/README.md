# Semana 1: Principios SOLID y ACID

Este módulo presenta los **principios SOLID** y el concepto **ACID** en bases de datos (ejemplos en Python).

---

## Principios SOLID
SOLID es un acrónimo inventado por Robert C.Martin (también conocido como el Tío Bob) para establecer los cinco principios básicos de la programación orientada a objetos.

Estos principios establecen prácticas que se prestan al desarrollo de software con consideraciones para su fácil mantenimiento y expansión a medida que el proyecto se amplía. Adoptar estas prácticas nos puede ayudar a evitar los «code smells», refactorizar el código y aprender sobre el desarrollo ágil y adaptativo de software.


### Single Responsibility Principle (SRP)
**Definición:**  
Una clase debe tener una única responsabilidad o razón de cambio.

- [👎 Anti-ejemplo](ejemplos/srp_bad.py)  
- [👍 Ejemplo refactorizado](ejemplos/srp_good.py)

---

### Open/Closed Principle (OCP)
**Definición:**  
El código debe estar **abierto a extensión** pero **cerrado a modificación**.

- [👎 Anti-ejemplo](ejemplos/ocp_bad.py)  
- [👍 Ejemplo refactorizado](ejemplos/ocp_good.py)

---

### Liskov Substitution Principle (LSP)
**Definición:**  
Las subclases deben poder reemplazar a sus clases base sin alterar el comportamiento esperado.

- [👎 Anti-ejemplo](ejemplos/lsp_bad.py)  
- [👍 Ejemplo refactorizado](ejemplos/lsp_good.py)

---

### Interface Segregation Principle (ISP)
**Definición:**  
No se debe forzar a una clase a implementar métodos que no necesita.

- [👎 Anti-ejemplo](ejemplos/isp_bad.py)  
- [👍 Ejemplo refactorizado](ejemplos/isp_good.py)

---

### Dependency Inversion Principle (DIP)
**Definición:**  
Las dependencias deben apuntar a **abstracciones**, no a implementaciones concretas.

- [👎 Anti-ejemplo](ejemplos/dip_bad.py)  
- [👍 Ejemplo refactorizado](ejemplos/dip_good.py)

---

### Preguntas

- **¿Por qué SOLID es importante en la programación orientada a objetos?**
- **¿Cómo aplico el Principio de Responsabilidad Única?**
- **¿Cuál es la diferencia entre el Principio Abierto-Cerrado (OCP) y el Principio de Inversión de Dependencia (DIP)?**
- **¿Los principios SOLID son sólo para programación orientada a objetos?**

---



## Propiedades ACID en Bases de Datos

**Definición:**  
Conjunto de propiedades que garantizan transacciones confiables.

- **Atomicidad:** Todas las operaciones de la transacción ocurren o ninguna.  
- **Consistencia:** La BD pasa de un estado válido a otro.  
- **Aislamiento:** Las transacciones concurrentes no interfieren entre sí.  
- **Durabilidad:** Una vez confirmada, la transacción persiste incluso ante fallos.

- [👍 Ejemplo de transacción ACID en Python/SQL](ejemplos/acid_transaction.py)

---


## ⚠️ Ejercicio práctico ⚠️

1. Revisar los **anti-ejemplos** de cada principio.  
2. Identificar qué principios se rompen/violan en su proyecto.  
3. Refactorizar el código aplicando SOLID.
4. Implementar una transacción simple respetando ACID.  
5. Subir los cambios al repositorio con un `README` explicativo.

