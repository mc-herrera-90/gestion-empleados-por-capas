# GestorBD

`GestorBD` extiende la funcionalidad de la clase `Conexion` y proporciona métodos para administrar la estructura de la base de datos.

Esta clase está diseñada para ejecutar archivos SQL completos, como scripts de creación de tablas (esquemas), inserciones iniciales y otros comandos necesarios para preparar la base de datos.

---

## Funciones principales

### `crear_esquema()`
Lee un archivo `.sql` y ejecuta todo el contenido sobre la base de datos conectada, permitiendo crear o reconstruir la estructura completa.

---

## Parámetros del constructor

| Parámetro         | Tipo     | Descripción                                                        |
|:------------------|:---------|:-------------------------------------------------------------------|
| `host`            | `str`    | Dirección del servidor MySQL.                                      |
| `database`        | `str`    | Nombre de la base de datos.                                        |
| `user`            | `str`    | Usuario autorizado para conectar al servidor.                      |
| `password`        | `str`    | Contraseña correspondiente al usuario.                             |
| `archivo_esquema` | `str`    | Ruta al archivo `.sql` que contiene las instrucciones del esquema. |

---
