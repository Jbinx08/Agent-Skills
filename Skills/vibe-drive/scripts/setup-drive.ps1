[CmdletBinding()]
param(
    [string]$Python = 'python',
    [string]$CredentialsPath
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$config = Join-Path $env:USERPROFILE '.vibe-drive'
$venv = Join-Path $config 'venv'
$runtime = Join-Path $venv 'Scripts/python.exe'
$requirements = Join-Path $PSScriptRoot 'requirements-drive.txt'

& $Python -c 'import sys; assert sys.version_info >= (3, 10), "Python 3.10+ required"'
if ($LASTEXITCODE -ne 0) { throw 'Python 3.10 or newer is required.' }
New-Item -ItemType Directory -Path $config -Force | Out-Null
if (-not (Test-Path -LiteralPath $runtime -PathType Leaf)) {
    & $Python -m venv $venv
    if ($LASTEXITCODE -ne 0) { throw 'Could not create Python environment.' }
}
& $runtime -m pip install --disable-pip-version-check -r $requirements
if ($LASTEXITCODE -ne 0) { throw 'Could not install Google Drive dependencies.' }
if ($CredentialsPath) {
    if (-not (Test-Path -LiteralPath $CredentialsPath -PathType Leaf)) {
        throw "Credentials file not found: $CredentialsPath"
    }
    $destination = Join-Path $config 'credentials.json'
    if (Test-Path -LiteralPath $destination -PathType Leaf) {
        throw "Credentials already exist; leaving them unchanged: $destination"
    }
    Copy-Item -LiteralPath $CredentialsPath -Destination $destination
}
Write-Host "Drive runtime ready: $runtime"
Write-Host "Place your OAuth Desktop app credentials at: $(Join-Path $config 'credentials.json')"
Write-Host 'Then run the installed vibe_drive.py auth command once.'
