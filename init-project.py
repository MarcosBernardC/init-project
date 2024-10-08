import subprocess  # Para ejecutar comandos en la terminal desde Python
import os  # Para interactuar con el sistema de archivos
import sys  # Para manejar el sistema y salir del script en caso de error

def crear_directorio_proyecto(nombre_proyecto):
    """Crea un directorio para el proyecto si no existe"""
    try:
        os.makedirs(nombre_proyecto, exist_ok=True)  # Crea el directorio si no existe
        print(f"Directorio {nombre_proyecto} creado correctamente.")
    except Exception as e:
        print(f"Error al crear el directorio {nombre_proyecto}: {e}")  # Maneja errores
        sys.exit(1)  # Sale del script si ocurre un error

def crear_entorno_virtual():
    """Crea un entorno virtual dentro de config-init"""
    try:
        # Crea el entorno virtual dentro de la carpeta 'config-init'
        subprocess.check_call([sys.executable, "-m", "venv", "config-init/venv"])
        print("Entorno virtual creado correctamente en config-init.")
    except subprocess.CalledProcessError as e:
        print(f"Error al crear el entorno virtual: {e}")
        sys.exit(1)  # Sale del script si ocurre un error

def crear_archivo_requirements():
    """Crea un archivo requirements.txt en config-init si no existe"""
    # Verifica si el archivo requirements.txt no existe dentro de config-init
    if not os.path.exists("config-init/requirements.txt"):
        try:
            # Crea el archivo requirements.txt con un comentario inicial
            with open("config-init/requirements.txt", "w") as req_file:
                req_file.write("# Lista de dependencias para el proyecto\n")
            print("Archivo requirements.txt creado correctamente en config-init.")
        except Exception as e:
            print(f"Error al crear el archivo requirements.txt: {e}")
    else:
        print("El archivo requirements.txt ya existe en config-init.")

def inicializar_git():
    """Inicializa un repositorio Git en la ruta principal y crea o actualiza el archivo .gitignore"""
    # Verifica si el repositorio Git ya existe
    if not os.path.exists(".git"):
        try:
            # Inicializa un nuevo repositorio Git en la carpeta principal
            subprocess.check_call(["git", "init"])
            print("Repositorio Git inicializado correctamente en la ruta principal.")

            # Crea o actualiza el archivo .gitignore para ignorar config-init/venv/
            with open(".gitignore", "a") as gitignore:
                gitignore.write("/config-init/venv/\n")  # Ignora el entorno virtual en Git
            print(".gitignore creado o actualizado con éxito en la ruta principal.")
        except subprocess.CalledProcessError as e:
            print(f"Error al inicializar Git: {e}")
            sys.exit(1)  # Sale del script si ocurre un error
    else:
        print("El repositorio Git ya está inicializado.")  # Mensaje si Git ya está inicializado

if __name__ == "__main__":
    # Define el nombre del proyecto; puedes cambiar el nombre aquí si lo deseas
    nombre_proyecto = "Proyecto"

    # Crear directorio para el proyecto si no existe
    crear_directorio_proyecto(nombre_proyecto)

    # Crear la carpeta config-init si no existe
    if not os.path.exists('config-init'):
        os.makedirs('config-init', exist_ok=True)

    # Crear archivo requirements.txt y entorno virtual en config-init
    crear_archivo_requirements()
    crear_entorno_virtual()

    # Inicializar Git en la ruta principal y agregar config-init/venv al .gitignore
    inicializar_git()