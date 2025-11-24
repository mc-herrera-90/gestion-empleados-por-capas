## Instrucciones sobre el proyecto

## Configurar el entorno virtual


1. Crear un entorno virtual:

```bash
# Windows
python -m venv venv
# macOS o Linux
python3 -m venv venv
```

2. Activar el entorno virtual:

```bash
# En windows
.\venv\Scripts\activate
# macos o Linux
source venv/bin/activate
```

3. Instalar dependencias

```bash
pip install -r requirements.txt
```


## Generar la documentación

Generar la documentación en una carpeta llamada documentación:

```bash
pdoc module -o documentacion
```

## Estructuras por capas

En una arquitectura por capas, el sistema suele organizarse de la siguiente manera:

```
Presentación → Aplicación → Dominio → Persistencia
```

| Capa                                  | Rol                                         |
| ------------------------------------- | ------------------------------------------- |
| **Presentación**                      | Muestra menús y recibe entradas del usuario |
| **Aplicación** (*ReglasDepartamento*) | Decide qué hacer con los datos              |
| **Dominio**                           | Define los objetos y estructuras de negocio |
| **Persistencia** (*DepartamentoDAO*)  | Guarda y recupera datos desde MySQL         |


### Capa de Aplicación

La **capa de Aplicación** es la encargada de coordinar la lógica del programa.
Es decir, **decide qué hacer**, pero no hace el trabajo duro por sí misma.

**La capa de Aplicación actúa como el “cerebro del flujo del programa”**:

* Recibe peticiones desde la interfaz/presentación (menús, vistas, API, etc.)
* Decide qué clases del dominio deben utilizarse
* Llama a los DAOs para guardar/leer datos
* Aplica validaciones básicas
* Evita que la presentación se conecte directo a la BD
* Evita que la persistencia se mezcle con la UI

> [!NOTE]  
> Es una capa **intermedia** que mantiene a tu proyecto ordenado, limpio y desacoplado.

Ejemplo de uso:

```python
class ReglasDepartamento:

	def __init__(self, dao: DepartamentoDAO):
        self.dao = dao

    def crear_objeto(self, nombre: str, descripcion: str = None) -> bool:
        d = Departamento(nombre=nombre, descripcion=descripcion)
        return self.dao.agregar(d)

    def mostrar_todos(self) -> List[Departamento]:
        return self.dao.mostrar()

    def buscar(self, valor) -> Optional[Departamento]:
        return self.dao.buscar(valor)

    def modificar(self, depto: Departamento) -> bool:
        return self.dao.modificar(depto)

    def eliminar(self, depto: Departamento) -> bool:
        return self.dao.eliminar(depto)
```

De este modo cada capa realiza la acción que le corresponde.

1. La presentación SOLO llama a métodos como:

```python
reglas.crear_objeto()
```

2. La capa de aplicación:
	* Crea un objeto `Departamento`
	* Llama al DAO para guardarlo
	* Devuelve True/False


3. La UI nunca toca la BD:
	* Se impide que la interfaz toque la BD directamente
	* Sin esta capa, tu menú tendría que hacer algo así:

```python
# ERROR: la UI no debería llamar directamente al DAO
dao = DepartamentoDAO()
dao.agregar(Departamento(...))
```

Eso mezcla presentación + persistencia.
La arquitectura quedaría mala y difícil de mantener.


4. Escalabilidad y mantenimiento:
	* Permite cambiar la BD sin tocar la interfaz. Si mañana cambias:
		* MySQL → PostgreSQL
		* PyMySQL → SQLAlchemy
		* Archivo plano → Firebase
