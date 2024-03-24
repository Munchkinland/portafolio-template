#!/bin/bash

# Crear un entorno virtual de Python
python3 -m venv .venv

# Activar el entorno virtual
source .venv/bin/activate

# Actualizar pip
pip install --upgrade pip

# Instalar dependencias desde requirements.txt
pip install -r requirements.txt

# Asegurar que Reflex esté instalado
pip install reflex

# Limpiar el directorio public si existe
rm -rf public

# Inicializar reflex (Asumiendo que esto prepara el proyecto para la exportación)
reflex init

# Exportar el frontend solamente
reflex export --frontend-only

# Verificar si el archivo frontend.zip fue generado
if [ -f "frontend.zip" ]; then
    # Crear el directorio public si no existe
    mkdir -p public
    # Descomprimir el contenido de frontend.zip en el directorio public
    unzip frontend.zip -d public
    # Eliminar el archivo frontend.zip después de descomprimirlo
    rm -f frontend.zip
else
    echo "Error: El archivo frontend.zip no se encontró."
    exit 1 # Salir del script indicando que hubo un error
fi

# Desactivar el entorno virtual
deactivate
