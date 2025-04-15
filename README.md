# Máquina de Snacks

Este proyecto implementa una **Máquina de Snacks** en Python, que permite gestionar un inventario de snacks y realizar compras simuladas. El proyecto utiliza conceptos de **POO (Programación Orientada a Objetos)**, como clases, encapsulamiento, herencia y manejo de archivos.

## Funcionalidades principales
1. **Gestión de Snacks**:
   - Clase `Snack`: Representa un snack con atributos como `id`, `nombre` y `precio`.
   - Clase `serviciosSnacks`: Administra el inventario de snacks, incluyendo la creación, carga, y almacenamiento de snacks en un archivo (`snacks.txt`).

2. **Simulación de Máquina de Snacks**:
   - Clase `maquinaSnacksApp`: Permite al usuario interactuar con la máquina de snacks mediante un menú. Las opciones incluyen:
     - Comprar snacks.
     - Mostrar un ticket de compra.
     - Agregar nuevos snacks al inventario.
     - Mostrar el inventario actual.

3. **Persistencia de datos**:
   - Los snacks se almacenan en un archivo (`snacks.txt`) para mantener el inventario entre ejecuciones.

## Estructura del proyecto
- **`Snack.py`**: Define la clase `Snack` con atributos privados y métodos para manipular snacks.
- **`serviciosSnacks.py`**: Administra el inventario de snacks, incluyendo la lectura/escritura en el archivo.
- **`maquinaSnacksApp.py`**: Implementa la lógica principal de la máquina de snacks y la interacción con el usuario.

## Ejecución
El programa principal se encuentra en `maquinaSnacksApp.py`. Para ejecutarlo, simplemente corre el archivo:

```bash
python [maquinaSnacksApp.py](http://_vscodecontentref_/0)
