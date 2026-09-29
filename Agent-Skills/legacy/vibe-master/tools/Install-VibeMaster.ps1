[CmdletBinding()]
param(
    [string]$SkillInstallRoot = (Join-Path $env:USERPROFILE '.agents\skills')
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$packageRoot = Split-Path -Parent $PSScriptRoot
$sourceSkill = Join-Path $packageRoot 'skill\vibe-master-flow'

if (-not (Test-Path -LiteralPath (Join-Path $sourceSkill 'SKILL.md') -PathType Leaf)) {
    throw "Skill package is incomplete: $sourceSkill"
}

$skillDestination = Join-Path $SkillInstallRoot 'vibe-master-flow'

New-Item -ItemType Directory -Path $skillDestination -Force | Out-Null
Get-ChildItem -LiteralPath $sourceSkill -Force | Copy-Item -Destination $skillDestination -Recurse -Force

Write-Host 'Vibe Master Flow installed.'
Write-Host "Skill: $skillDestination"
Write-Host 'Open any project in Codex and type: Vibe_Master Flow start'
Write-Host 'If the current Codex session does not show the skill, restart Codex once.'
