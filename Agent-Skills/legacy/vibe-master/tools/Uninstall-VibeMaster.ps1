[CmdletBinding()]
param(
    [string]$SkillInstallRoot = (Join-Path $env:USERPROFILE '.agents\skills')
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Assert-ChildPath {
    param(
        [Parameter(Mandatory = $true)][string]$Child,
        [Parameter(Mandatory = $true)][string]$Parent
    )

    $childFull = [System.IO.Path]::GetFullPath($Child).TrimEnd('\')
    $parentFull = [System.IO.Path]::GetFullPath($Parent).TrimEnd('\')
    $requiredPrefix = $parentFull + '\'

    if (-not $childFull.StartsWith($requiredPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing to remove a path outside the expected root: $childFull"
    }
}

$skillDestination = Join-Path $SkillInstallRoot 'vibe-master-flow'

Assert-ChildPath -Child $skillDestination -Parent $SkillInstallRoot

if (Test-Path -LiteralPath $skillDestination -PathType Container) {
    Remove-Item -LiteralPath $skillDestination -Recurse -Force
    Write-Host "Removed skill: $skillDestination"
} else {
    Write-Host "Skill was not installed: $skillDestination"
}

Write-Host 'Vibe Master Flow uninstalled.'
