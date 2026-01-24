#IMPORTANTE.....activar todo este codigo con el comando......          .\buildfronted.ps1



# Activar el entorno virtual
.venv\Scripts\Activate.ps1

# Actualizar pip
pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt

# Eliminar carpeta "public" si existe
if (Test-Path public) {
    Remove-Item public -Recurse -Force
}

# Inicializar Reflex
reflex init

# Exportar solo frontend
reflex export --frontend-only

# Descomprimir frontend.zip en carpeta public
Expand-Archive -Path frontend.zip -DestinationPath public -Force

# Desactivar el entorno virtual
deactivate
