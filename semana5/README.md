# REST API Tutorial

## ¿Qué es REST?
REST (REpresentational State Transfer) es un **estilo arquitectónico** para sistemas distribuidos basado en hipermedia. No es un protocolo ni un estándar, sino un conjunto de principios que permiten diseñar **APIs simples, escalables y sin estado**.

Una API que cumple con estos principios se denomina **API RESTful**.

---

## Principios de REST
1. **Interfaz uniforme**  
   - Identificación única de recursos (ej: `/users/1`)  
   - Manipulación de recursos mediante representaciones (JSON, XML).  
   - Mensajes autodescriptivos.  
   - Uso de hipermedios (HATEOAS).

2. **Cliente-Servidor**  
   - Separación de responsabilidades: cliente maneja UI, servidor maneja datos.  
   - Escalabilidad y evolución independiente.

3. **Sin estado (Stateless)**  
   - Cada petición debe contener toda la información necesaria.  
   - El servidor no guarda estado de sesión.

4. **Cacheable**  
   - Las respuestas deben indicar si son cacheables o no.  
   - Mejora el rendimiento y reduce carga.

5. **Sistema en capas**  
   - Arquitectura organizada en capas (ej: proxy, balanceadores).  
   - Cada capa desconoce la lógica más allá de su vecina inmediata.

6. **Código bajo demanda (opcional)**  
   - El servidor puede enviar código ejecutable al cliente (ej: scripts).

---

## Recursos
- Todo en REST es un **recurso** (documento, imagen, colección, servicio).  
- Un recurso se identifica mediante un **URI**.  
- Su estado se representa con: **datos + metadatos + enlaces hipermedia**.

### Ejemplo de recurso REST (JSON):
```json
{
  "id": 123,
  "title": "Qué es REST",
  "content": "REST es un estilo arquitectónico para construir servicios web...",
  "published_at": "2023-11-04T14:30:00Z",
  "author": {
    "id": 456,
    "name": "John Doe",
    "profile_url": "https://ejemplo.com/authors/456"
  },
  "comments": {
    "count": 5,
    "comments_url": "https://ejemplo.com/posts/123/comments"
  },
  "self": {
    "link": "https://ejemplo.com/posts/123"
  }
}
```
---
# ¿Qué es un URI?

## Definición
**URI** significa **Uniform Resource Identifier** (Identificador Uniforme de Recursos).  
Es una cadena de texto que permite **identificar un recurso** en Internet de manera única.

Un URI puede ser:
- **URL (Uniform Resource Locator):** indica **dónde está** el recurso y cómo acceder a él.  
- **URN (Uniform Resource Name):** indica **qué es** el recurso por nombre, sin decir dónde está.  

En APIs REST trabajamos casi siempre con **URLs**.

---

## Ejemplos
- **URL:** `https://example.com/users/123`
  - Identifica y localiza al **usuario con id 123**.
- **URN:** `urn:isbn:0451450523`
  - Identifica un libro por su **ISBN**, pero no dice dónde encontrarlo.

---

## Partes de un URI (ejemplo)

https://api.micropos.cl/products/15?sort=asc#detalles


| Parte         | Significado |
|---------------|-------------|
| `https`       | **Esquema/Protocolo** (cómo se accede: HTTP, HTTPS, FTP, etc.) |
| `api.mitienda.com` | **Host/Dominio** (servidor que provee el recurso) |
| `/products/15` | **Ruta** (indica el recurso específico, producto con id=15) |
| `?sort=asc`   | **Query parameters** (modifican la petición: orden ascendente) |
| `#detalles`   | **Fragmento** (parte específica del recurso, ej: sección "detalles") |

---

## Ejemplo en REST
- Recurso: `Producto`
- URL para obtener producto con id=15:

GET https://api.micropos.cl/products/15

Respuesta JSON:
```json
{
  "id": 15,
  "name": "Notebook Gamer",
  "price": 1200000,
  "currency": "CLP"
}
```

---

## Métodos sobre Recursos
Los métodos definen las operaciones sobre recursos. Usualmente se implementan con **HTTP verbs**:

- `GET` → Obtener recurso.  
- `POST` → Crear recurso.  
- `PUT` → Reemplazar recurso.  
- `PATCH` → Modificar parcialmente.  
- `DELETE` → Eliminar recurso.  

> REST no obliga a qué método usar, pero recomienda mantener una **interfaz uniforme**.

---

## Resumen
- REST simplifica la comunicación cliente-servidor.  
- Usa **recursos identificados por URIs**.  
- Promueve **stateless**, **cacheable** y **capas**.  
- Permite **hipermedios** para descubrir acciones dinámicamente.  

## Prueba viernes en parejas
1. Implementar en REST los endpoints a entregar (`GET`, `POST`, `GET by ID`).
2. Proteger el `POST` con JWT de demo (`Bearer secret123`).
3. Investigar e Implementar GraphQL con `Query models` y `Mutation createModel`.
4. Investigar como realizar con FastAPI.