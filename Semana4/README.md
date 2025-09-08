# Semana 4: Patrones de Diseño (GoF) aplicados a Arquitecturas Modernas


## Introducción a los Patrones de Diseño GoF
- Definidos en el libro **Design Patterns (1994)** por el "Gang of Four" (GoF).  
- Son **soluciones probadas** a problemas comunes en el diseño de software.  
- No son código fijo, sino **plantillas conceptuales**.  

Categorías:
1. **Creacionales** → cómo crear objetos.  
2. **Estructurales** → cómo organizar clases y objetos.  
3. **De comportamiento** → cómo interactúan los objetos.  

---

## Patrones Relevantes y Ejemplos en Python

### 1.- Creacionales
**Factory Method**  
- Problema: crear objetos sin acoplarse a la clase concreta.  
- Uso moderno: en **DDD**, crear entidades o servicios sin exponer detalles.  

- [Ver código](ejemplos/factory_method.py)

---

### 2.- Estructurales
**Adapter**  
- Problema: conectar clases incompatibles.  
- Uso moderno: en **Arquitectura Hexagonal**, los adaptadores conectan puertos con infraestructuras.  

- [Ver código](ejemplos/adapter.py)

---

### 3.- De Comportamiento
**Observer**  
- Problema: notificar cambios a varios objetos automáticamente.  
- Uso moderno: en **event-driven architectures**, microservicios y colas de mensajería.  

- [Ver código](ejemplos/observer.py)

---

**Strategy**  
- Problema: cambiar algoritmos sin modificar el código cliente.  
- Uso moderno: casos de uso con múltiples implementaciones (ej: validación de contraseñas, cálculo de descuentos).  

- [Ver código](ejemplos/strategy.py)

---

**Decorator**  
- Problema: añadir responsabilidades a un objeto de forma dinámica.  
- Uso moderno: middleware en frameworks web (Django, FastAPI, Express).  

- [Ver código](ejemplos/decorator.py)

---

## Patrones y Arquitecturas Modernas

| Patrón GoF      | Aplicación en arquitecturas modernas |
|-----------------|--------------------------------------|
| **Factory Method** | Creación de entidades y servicios en DDD |
| **Singleton**      | Configuración única (ej: repositorio global, DB connection pool) |
| **Adapter**        | Arquitectura Hexagonal (puertos/adaptadores) |
| **Strategy**       | Selección de algoritmos en casos de uso (ej: cálculo de descuentos) |
| **Observer**       | Event-driven, mensajería con Kafka/RabbitMQ |
| **Decorator**      | Middleware en frameworks web (Django, FastAPI, Express) |

---

## Ejercicio Práctico Viernes
1. Implementar un **sistema de login** donde:  
   - La validación de password use el patrón **Strategy** (ej: simple vs fuerte).  
   - El envío de notificaciones use el patrón **Adapter** (ej: `ConsoleEmail`, `SmtpEmail`).  
   - El sistema de auditoría use el patrón **Observer** (log cada vez que alguien se loguea).  

