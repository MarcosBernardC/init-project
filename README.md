
# AutoVENV: Script de Inicialización de Proyectos con Entorno Virtual

Este proyecto **AutoVENV** automatiza la configuración inicial de un nuevo proyecto en Python, incluyendo la creación de un entorno virtual, la inicialización de Git, y la generación de archivos esenciales como **`requirements.txt`** y **`.gitignore`**.

## Estructura del Proyecto

El script crea la siguiente estructura:

```
/TuDirectorioPrincipal
  ├── .git                      # Repositorio Git inicializado en la raíz
  ├── .gitignore                 # Archivo que ignora /config-init/venv
  ├── /Proyecto                  # Carpeta del proyecto con el código fuente
  ├── /config-init               # Carpeta de configuración para el entorno virtual
  │   ├── venv/                  # Entorno virtual
  │   └── requirements.txt       # Archivo para la lista de dependencias
```

## Archivos Generados

- **`requirements.txt`**: Un archivo que lista las dependencias del proyecto. Se encuentra en **`/config-init`**.
- **`venv/`**: El entorno virtual, creado dentro de **`/config-init`**.
- **`.gitignore`**: Configurado para ignorar **`/config-init/venv/`**, evitando subir el entorno virtual al repositorio.

## Uso del Script

1. **Clona o descarga el repositorio**.

   ```bash
   git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   ```

2. **Navega al directorio del proyecto y ejecuta el script**.

   ```bash
   cd TuDirectorioPrincipal
   python config-init/config-init.py
   ```

3. **Qué hace el script**:

   - Crea la carpeta **`/Proyecto`** donde puedes almacenar el código fuente.
   - Inicializa Git en la raíz del proyecto.
   - Crea un archivo **`requirements.txt`** dentro de **`/config-init`**.
   - Crea el entorno virtual dentro de **`/config-init/venv`**.
   - Actualiza **`.gitignore`** para ignorar **`/config-init/venv`**.

## Personalización

Puedes personalizar el nombre del proyecto modificando la siguiente línea en el archivo **`config-init.py`**:

```python
nombre_proyecto = "Proyecto"
```

Este nombre será utilizado para crear la carpeta del proyecto.

## Requerimientos

Asegúrate de tener **Python 3.x** instalado en tu sistema para ejecutar el script.

## Contribuciones

¡Siéntete libre de hacer un fork de este repositorio y contribuir! Si tienes alguna mejora o sugerencia, no dudes en enviar un pull request o abrir un issue.

---

**Autor:** [Tu Nombre]  
**Licencia:** MIT
