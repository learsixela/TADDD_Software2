# Semana 3: Patrón MVC, Principios de Diseño

### ¿Qué es MVC?
- **Modelo (M):** Representa los **datos** y reglas del negocio.  
- **Vista (V):** Es la **interfaz** con el usuario (puede ser consola, web o móvil).  
- **Controlador (C):** Coordina el flujo: recibe las acciones del usuario, actualiza el modelo y elige qué vista mostrar.

![MVC](mvc.png)
---

### Cuándo utilizar el patrón de diseño MVC

- **Aplicaciones complejas:** Utilice MVC para aplicaciones con muchas funciones e interacciones de usuario, como sitios de comercio electrónico. Ayuda a organizar el código y gestionar la complejidad.
- **Cambios frecuentes en la interfaz de usuario:** Si la interfaz de usuario necesita actualizaciones periódicas, MVC permite cambios en la Vista sin afectar la lógica subyacente.
- **Reutilizabilidad de componentes:** Si desea reutilizar partes de su aplicación en otros proyectos, la estructura modular de MVC lo hace más fácil.
- **Requisitos de prueba:** MVC admite pruebas exhaustivas, lo que le permite probar cada componente por separado para un mejor control de calidad.

### Cuándo NO utilizar el patrón de diseño MVC

- **Aplicaciones simples:** Para aplicaciones pequeñas con funcionalidad limitada, MVC puede agregar complejidad innecesaria. Un enfoque más simple puede ser mejor.
- **Aplicaciones en tiempo real:** Es posible que MVC no funcione bien para aplicaciones que requieren actualizaciones inmediatas, como juegos en línea o aplicaciones de chat.
- **Interfaz de usuario y lógica estrechamente acopladas:** Si la interfaz de usuario y la lógica empresarial están estrechamente vinculadas, MVC podría complicar aún más las cosas.
- **Recursos limitados:** Para equipos pequeños o aquellos que no están familiarizados con MVC, los diseños más simples pueden conducir a un desarrollo más rápido y menos problemas.

---

### **Ejemplo de la vida real:**  
En un restaurante ¿Quienes o que cumple los sigueintes conceptos? :  
- **Modelo:**.  
- **Vista:** .  
- **Controlador:**

---

### Principios de Diseño
1. **Separación de responsabilidades:** cada parte hace solo lo que le corresponde.  
2. **Bajo acoplamiento:** que una parte dependa lo menos posible de los detalles de otra.  
3. **Alta cohesión:** que las funciones relacionadas estén en el mismo lugar.  

![Ciclo Vida](ciclo_vida.png)

### El diseño del sistema se puede dividir en dos partes complementarias

![LLD - HLD ](niveles.png)

### Diseño de alto nivel (HLD)
Describe la arquitectura general del sistema: cómo interactúan los componentes principales, qué servicios o módulos existirán y cómo fluyen los datos entre ellos.

- Le ofrece una visión general: cómo funciona el sistema, su estructura central y las decisiones principales.
- Realizado por arquitectos, partes interesadas y gerentes

#### Conocimientos técnicos previos para el HLD
- Habilidades básicas de codificación (estructuras de datos y algoritmos)
- En comparación con el diseño de bajo nivel, el diseño de alto nivel generalmente lo realizan personas con mayor experiencia y experiencia práctica en proyectos de software.
- Conocer los roles de componentes como bases de datos (SQL y NoSQL), cachés (Redis, Memcached, CDN) y API.
- Diseño de bajo nivel (programación orientada a objetos y patrones de diseño)
- Comprensión profunda de los requisitos funcionales (qué debe hacer el sistema, por ejemplo, registro de usuarios, transmisión) y los requisitos no funcionales (cómo debe funcionar el sistema: escalabilidad, latencia, disponibilidad, seguridad, etc.)
- Fundamentos de redes y seguridad como DNS, protocolos (TCP/UDP, HTTP, WebSockets), OAuth, JWT, TLS/SSL, limitación de velocidad, seguridad de API y protección básica contra DDOS
- Colas de mensajes y herramientas de transmisión como Kafka o RabbitMQ.
- Conocimiento de microservicios vs. monolitos (cuándo dividir servicios y cómo administrar dependencias), tolerancia a fallas, estrategias de respaldo, redundancia, tipos y algoritmos de balanceador de carga.
- Herramientas de observabilidad como Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana) y sistemas de alerta (por ejemplo, PagerDuty)

---

### Diseño de bajo nivel (LLD)
Cubre cómo funciona cada parte y se implementa internamente.

- Proporciona a los desarrolladores un plan claro y práctico para construir cada componente.
- Una vez que las partes interesadas han creado un diseño de alto nivel, es tarea de los desarrolladores y diseñadores senior crear un diseño de bajo nivel.
#### Prerrequisitos / Lo que debes saber primero:
- Habilidades básicas de codificación (estructuras de datos y algoritmos)
- Sólida comprensión de los conceptos de programación orientada a objetos ( encapsulación, herencia, polimorfismo y abstracción).

**Ejemplo**
- **Desglose de componentes/módulos :** lógica interna detallada para cada módulo, con responsabilidades de clase, métodos, atributos e interacciones
- **Esquema y estructura de la base de datos :** diseño de tablas, claves, índices y relaciones con mejoras en SQL/NoSQL
- **Definiciones de API e interfaz :** formatos precisos de solicitud/respuesta, códigos de error, métodos, puntos finales e interfaz interna
- **Manejo de errores y lógica de validación :** define cómo cada módulo gestiona entradas no válidas, fallas, casos extremos y registros.
- **Patrones de diseño y SOLID :** Implemente patrones de diseño y principios sólidos para garantizar un código limpio, extensible y mantenible.
- **Artefactos UML y pseudocódigo :** diagramas de clases, diagramas de secuencia, pseudocódigo o diagramas de flujo para aclarar rutas lógicas y llamadas a métodos


https://www.geeksforgeeks.org/system-design/getting-started-with-system-design/
---

## Desafio Evaluado

### Implementar un sistema de login donde:

1. Desarrollar en el sistema que estan desarrollando como grupo y de acuerdo a su stack tecnologico.
2. Aplicar lo viste en las 3 semanas.
3. Preparar presentación.



