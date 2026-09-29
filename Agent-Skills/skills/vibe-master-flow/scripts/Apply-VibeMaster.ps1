[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [string]$TargetPath = (Get-Location).Path,

    [switch]$Force
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$skillRoot = Split-Path -Parent $PSScriptRoot
$sourceRoot = Join-Path $skillRoot 'assets\Vibe-master'

if (-not (Test-Path -LiteralPath $sourceRoot -PathType Container)) {
    throw "Bundled Vibe-master assets were not found: $sourceRoot"
}

if (-not (Test-Path -LiteralPath $TargetPath)) {
    New-Item -ItemType Directory -Path $TargetPath -Force | Out-Null
}

$targetItem = Get-Item -LiteralPath $TargetPath
if (-not $targetItem.PSIsContainer) {
    throw "TargetPath must be a directory: $TargetPath"
}

$targetRoot = $targetItem.FullName
$destinationRoot = Join-Path $targetRoot 'Vibe-master'
$sourceFull = (Get-Item -LiteralPath $sourceRoot).FullName.TrimEnd('\')
$destinationFull = [System.IO.Path]::GetFullPath($destinationRoot).TrimEnd('\')

if ($sourceFull.Equals($destinationFull, [System.StringComparison]::OrdinalIgnoreCase)) {
    throw 'The destination cannot be the bundled asset directory itself.'
}

New-Item -ItemType Directory -Path $destinationFull -Force | Out-Null

$copied = 0
$skipped = 0
$sourceFiles = Get-ChildItem -LiteralPath $sourceFull -Recurse -File

foreach ($sourceFile in $sourceFiles) {
    $relativePath = $sourceFile.FullName.Substring($sourceFull.Length).TrimStart('\')
    $destinationFile = Join-Path $destinationFull $relativePath
    $destinationDirectory = Split-Path -Parent $destinationFile

    if (-not (Test-Path -LiteralPath $destinationDirectory -PathType Container)) {
        New-Item -ItemType Directory -Path $destinationDirectory -Force | Out-Null
    }

    if ((Test-Path -LiteralPath $destinationFile -PathType Leaf) -and -not $Force) {
        $skipped++
        continue
    }

    Copy-Item -LiteralPath $sourceFile.FullName -Destination $destinationFile -Force
    $copied++
}

if (-not (Test-Path -LiteralPath (Join-Path $destinationFull 'VIBE_MASTER.md') -PathType Leaf)) {
    throw 'VIBE_MASTER.md was not installed.'
}

Write-Host "Vibe Master applied successfully."
Write-Host "Destination: $destinationFull"
Write-Host "Copied: $copied"
Write-Host "Skipped existing: $skipped"

[pscustomobject]@{
    Destination = $destinationFull
    Copied = $copied
    Skipped = $skipped
}
