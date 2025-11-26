$VenvDir = "venv"

Write-Host "Verificando entorno virtual..."

if (!(Test-Path $VenvDir)) {
    Write-Host "Creando entorno virtual..."
    python -m venv $VenvDir
}
else {
    Write-Host "El entorno virtual ya existe."
}

Write-Host "Instalando dependencias..."
.\venv\Scripts\pip.exe install --upgrade pip

if (Test-Path "requirements.txt") {
    .\venv\Scripts\pip.exe install -r requirements.txt
}

Write-Host "Para activar el entorno ejecuta:"
Write-Host ".\venv\Scripts\Activate.ps1"