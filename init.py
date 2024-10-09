import subprocess
import os
import sys
import re

def limpiar_pantalla():
    """Limpia la pantalla según el sistema operativo"""
    os.system('cls' if os.name == 'nt' else 'clear')  # Utiliza 'cls' para Windows y 'clear' para otros SO

def crear_directorio(nombre):
    """Crea un directorio si no existe"""
    try:
        os.makedirs(nombre, exist_ok=True)  # Crea el directorio y no da error si ya existe
        print(f"Directorio {nombre} creado correctamente.")
    except Exception as e:
        print(f"Error al crear el directorio {nombre}: {e}")
        sys.exit(1)  # Salir del script si hay error crítico

def crear_entorno_virtual(ruta_config):
    """Crea un entorno virtual dentro de la carpeta config"""
    try:
        # Usa el intérprete de Python actual para crear el entorno virtual en la ruta especificada
        subprocess.check_call([sys.executable, "-m", "venv", os.path.join(ruta_config, "venv")])
        print("Entorno virtual creado correctamente en config.")
    except subprocess.CalledProcessError as e:
        print(f"Error al crear el entorno virtual: {e}")
        sys.exit(1)  # Salir si hay un error al crear el entorno virtual

def crear_archivo_requirements(ruta_config):
    """Crea un archivo requirements.txt dentro de la carpeta config si no existe"""
    ruta_requirements = os.path.join(ruta_config, "requirements.txt")
    if not os.path.exists(ruta_requirements):  # Solo crea el archivo si no existe
        try:
            with open(ruta_requirements, "w") as req_file:
                req_file.write("# Lista de dependencias para el proyecto\n")  # Archivo inicial para dependencias
            print("Archivo requirements.txt creado correctamente en config.")
        except Exception as e:
            print(f"Error al crear el archivo requirements.txt: {e}")
    else:
        print("El archivo requirements.txt ya existe en config.")  # Mensaje si el archivo ya está creado

def inicializar_git(ruta_proyecto):
    """Inicializa un repositorio Git en la ruta principal y actualiza el archivo .gitignore"""
    ruta_git = os.path.join(ruta_proyecto, ".git")
    if not os.path.exists(ruta_git):  # Si el repositorio aún no está inicializado
        try:
            subprocess.check_call(["git", "init", ruta_proyecto])  # Inicializa un nuevo repositorio Git
            print("Repositorio Git inicializado correctamente en el directorio del proyecto.")
            
            # Añadir 'config/venv/' al archivo .gitignore para ignorar la carpeta venv
            gitignore_path = os.path.join(ruta_proyecto, ".gitignore")
            with open(gitignore_path, "a") as gitignore:
                gitignore.write("config/venv/\n")
            print(".gitignore creado o actualizado en el proyecto.")
        except subprocess.CalledProcessError as e:
            print(f"Error al inicializar Git: {e}")
            sys.exit(1)

def agregar_repositorio_remoto(ruta_proyecto, url_remoto):
    """Agrega un repositorio remoto al proyecto"""
    try:
        os.chdir(ruta_proyecto)  # Cambiar al directorio del proyecto
        subprocess.check_call(["git", "remote", "add", "origin", url_remoto])  # Vincular repositorio remoto
        print(f"Repositorio remoto '{url_remoto}' agregado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al agregar el repositorio remoto: {e}")
        sys.exit(1)

def obtener_nombre_repositorio(url_remoto):
    """Extrae el nombre del repositorio desde la URL remota"""
    nombre_repo = re.findall(r'/([^/]+)\.git$', url_remoto)  # Extrae el nombre usando expresión regular
    if nombre_repo:
        return nombre_repo[0]  # Retorna el nombre del repositorio si coincide con la expresión
    else:
        print("Error: No se pudo obtener el nombre del repositorio desde la URL.")
        sys.exit(1)

def validar_url_repositorio(url_remoto):
    """Valida que la URL proporcionada tenga el formato correcto"""
    if not url_remoto.startswith("https://github.com/"):  # Verifica si la URL empieza con la estructura correcta
        print("La URL del repositorio debe comenzar con 'https://github.com/'")
        sys.exit(1)

def crear_gitkeep(ruta_workspace):
    """Crea un archivo .gitkeep dentro de la carpeta Workspace para asegurarse de que se incluya en el commit"""
    ruta_gitkeep = os.path.join(ruta_workspace, ".gitkeep")  # Define la ruta para el archivo .gitkeep
    try:
        with open(ruta_gitkeep, "w") as gitkeep_file:
            gitkeep_file.write("")  # Crea un archivo vacío .gitkeep
        print(".gitkeep creado en Workspace.")
    except Exception as e:
        print(f"Error al crear .gitkeep en Workspace: {e}")
        sys.exit(1)

def realizar_commit_final(mensaje_commit):
    """Realiza un solo commit al final del proceso"""
    try:
        subprocess.check_call(["git", "add", "."])  # Agrega todos los archivos al área de staging
        subprocess.check_call(["git", "commit", "-m", mensaje_commit])  # Realiza el commit con un mensaje
        print(f"Commit realizado: '{mensaje_commit}'")
    except subprocess.CalledProcessError as e:
        print(f"Error al realizar el commit: {e}")
        sys.exit(1)

def realizar_push():
    """Realiza un git push al repositorio remoto"""
    try:
        subprocess.check_call(["git", "push", "-u", "origin", "master"])  # Realiza el push al repositorio remoto
        print("Push realizado exitosamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al realizar el push: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Recomendación para crear el repositorio si aún no existe
    respuesta = input("¿Ya has creado un repositorio en GitHub? (Y/n): ").strip().lower()
    if respuesta == 'n':
        print("Por favor, crea un repositorio en GitHub y copia el enlace.")
        sys.exit(0)  # Salir del script hasta que el usuario cree el repositorio

    # Pedir la URL del repositorio remoto
    url_remoto = input("Introduce la URL del repositorio remoto: ")
    
    # Validar la URL del repositorio
    validar_url_repositorio(url_remoto)

    # Obtener el nombre del repositorio desde la URL
    nombre_proyecto = obtener_nombre_repositorio(url_remoto)
    
    # Crear la estructura del proyecto con las carpetas config y Workspace
    crear_directorio(nombre_proyecto)
    ruta_config = os.path.join(nombre_proyecto, "config")
    ruta_workspace = os.path.join(nombre_proyecto, "Workspace")
    
    crear_directorio(ruta_config)   # Crear carpeta config para venv y requirements
    crear_directorio(ruta_workspace)  # Crear carpeta Workspace para scripts y archivos del proyecto
    
    # Crear .gitkeep dentro de Workspace
    crear_gitkeep(ruta_workspace)

    # Crear archivo requirements.txt y entorno virtual en config
    crear_archivo_requirements(ruta_config)
    crear_entorno_virtual(ruta_config)
    
    # Inicializar Git en la carpeta del proyecto y agregar config/venv al .gitignore
    inicializar_git(nombre_proyecto)

    # Vincular repositorio remoto
    agregar_repositorio_remoto(nombre_proyecto, url_remoto)
    
    # Realizar un único commit con un mensaje claro al final
    realizar_commit_final("Estructura del proyecto creada, entorno virtual y repositorio remoto configurados")
    
    # Realizar el push al repositorio remoto
    realizar_push()
    
    # Limpiar la pantalla al finalizar el proceso
    limpiar_pantalla()

    # Mostrar mensaje final
    print("¡Push realizado con éxito!")
    print("Puedes cortar y pegar la carpeta del proyecto a otra ruta si lo deseas.")