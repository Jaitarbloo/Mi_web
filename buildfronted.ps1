#IMPORTANTE.....activar todo este codigo con el comando......          .\buildfronted.ps1

$ErrorActionPreference = "Continue"
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path

try {
    Write-Host "=== Iniciando build del frontend ===" -ForegroundColor Green
    
    # Activar el entorno virtual
    Write-Host "1. Activando entorno virtual..."
    & "$scriptPath\.venv\Scripts\Activate.ps1"
    if ($LASTEXITCODE -ne 0) { throw "Error activando entorno virtual" }
    
    # Actualizar pip
    Write-Host "2. Actualizando pip..."
    python -m pip install --upgrade pip --quiet
    
    # Instalar dependencias (si requirements.txt existe)
    if (Test-Path requirements.txt) {
        Write-Host "3. Instalando dependencias..."
        pip install -r requirements.txt --quiet
    }
    
    # Inicializar Reflex
    Write-Host "4. Inicializando Reflex..."
    reflex init --skip-demo
    
    # Exportar solo frontend
    Write-Host "5. Exportando frontend..."
    reflex export --frontend-only
    
    # Descomprimir frontend.zip en carpeta public
    Write-Host "6. Descomprimiendo frontend..."
    if (Test-Path frontend.zip) {
        if (Test-Path public) {
            Remove-Item public -Recurse -Force
        }
        New-Item -ItemType Directory -Path public -Force | Out-Null
        Expand-Archive -Path frontend.zip -DestinationPath public -Force
        Remove-Item frontend.zip -Force
        Write-Host "Frontend descomprimido correctamente" -ForegroundColor Green
    } else {
        Write-Host "ADVERTENCIA: frontend.zip no fue encontrado" -ForegroundColor Yellow
    }
    
    # Subir cambios a GitHub
    Write-Host "7. Subiendo cambios a GitHub..."
    git add .
    git commit -m "Build: actualizar frontend exportado"
    git push origin main
    
    Write-Host "=== Build completado exitosamente ===" -ForegroundColor Green
}
catch {
    Write-Host "ERROR: $_" -ForegroundColor Red
    Write-Host "Línea: $($_.InvocationInfo.ScriptLineNumber)" -ForegroundColor Red
    exit 1
}
finally {
    Write-Host "Script finalizado" -ForegroundColor Cyan
}
