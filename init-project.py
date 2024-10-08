import subprocess
import os
import sys

def crear_directorio_proyecto(nombre_proyecto):
    """Crea un directorio para el proyecto"""
    try:
        os.makedirs(nombre_proyecto, exist_ok=True)
        print(f"Directorio {nombre_proyecto} creado correctamente.")
    except Exception as e:
        print(f"Error al crear el directorio {nombre_proyecto}: {e}")
        sys.exit(1)

def crear_entorno_virtual():
    """Crea un entorno virtual dentro de config-init"""
    try:
        subprocess.check_call([sys.executable, "-m", "venv", "config-init/venv"])
        print("Entorno virtual creado correctamente en config-init.")
    except subprocess.CalledProcessError as e:
        print(f"Error al crear el entorno virtual: {e}")
        sys.exit(1)

def crear_archivo_requirements():
    """Crea un archivo requirements.txt en config-init si no existe"""
    if not os.path.exists("config-init/requirements.txt"):
        try:
            with open("config-init/requirements.txt", "w") as req_file:
                req_file.write("# Lista de dependencias para el proyecto\n")
            print("Archivo requirements.txt creado correctamente en config-init.")
        except Exception as e:
            print(f"Error al crear el archivo requirements.txt: {e}")
    else:
        print("El archivo requirements.txt ya existe en config-init.")

def inicializar_git():
    """Inicializa un repositorio Git en la ruta principal y crea o actualiza el archivo .gitignore"""
    if not os.path.exists(".git"):
        try:
            subprocess.check_call(["git", "init"])
            print("Repositorio Git inicializado correctamente en la ruta principal.")

            # Agregar /config-init/venv/ a .gitignore sin sobrescribir
            with open(".gitignore", "a") as gitignore:
                gitignore.write("/config-init/venv/\n")
            print(".gitignore creado o actualizado con éxito en la ruta principal.")
        except subprocess.CalledProcessError as e:
            print(f"Error al inicializar Git: {e}")
            sys.exit(1)
    else:
        print("El repositorio Git ya está inicializado.")

if __name__ == "__main__":
    nombre_proyecto = "Proyecto"  # Cambia este nombre si lo deseas

    # Crear directorio para el proyecto
    crear_directorio_proyecto(nombre_proyecto)

    # Crear la carpeta config-init
    if not os.path.exists('config-init'):
        os.makedirs('config-init', exist_ok=True)

    # Crear archivo requirements.txt y entorno virtual en config-init
    crear_archivo_requirements()
    crear_entorno_virtual()

    # Inicializar Git en la ruta principal y agregar al .gitignore
    inicializar_git()
