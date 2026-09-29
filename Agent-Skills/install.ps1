[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [ValidateSet('All','Codex','ClaudeCode','Cursor')]
    [string]$Agent = 'All',
    [ValidateSet('All','vibe-drive','vibe-master-flow')]
    [string]$Skill = 'All',
    [string]$InstallBase = $env:USERPROFILE,
    [switch]$Force
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$repo = $PSScriptRoot
$sourceRoot = Join-Path $repo 'skills'
$names = if ($Skill -eq 'All') { @('vibe-drive','vibe-master-flow') } else { @($Skill) }
$agents = if ($Agent -eq 'All') { @('Codex','ClaudeCode','Cursor') } else { @($Agent) }
$profileRoot = [System.IO.Path]::GetFullPath($InstallBase)

foreach ($agentName in $agents) {
    $parent = switch ($agentName) {
        'Codex' {
            if ($InstallBase -eq $env:USERPROFILE -and $env:CODEX_HOME) {
                Join-Path $env:CODEX_HOME 'skills'
            } else { Join-Path $profileRoot '.codex/skills' }
        }
        'ClaudeCode' { Join-Path $profileRoot '.claude/skills' }
        'Cursor' { Join-Path $profileRoot '.cursor/skills' }
    }
    foreach ($name in $names) {
        $source = Join-Path $sourceRoot $name
        $destination = Join-Path $parent $name
        if (-not (Test-Path -LiteralPath (Join-Path $source 'SKILL.md') -PathType Leaf)) {
            throw "Incomplete source skill: $source"
        }
        if ((Test-Path -LiteralPath $destination) -and
            ((Get-Item -LiteralPath $destination -Force).Attributes -band [IO.FileAttributes]::ReparsePoint)) {
            throw "Refusing to install through a link: $destination"
        }
        $sourcePath = (Get-Item -LiteralPath $source).FullName.TrimEnd('\','/')
        foreach ($file in Get-ChildItem -LiteralPath $sourcePath -Recurse -File) {
            $relative = $file.FullName.Substring($sourcePath.Length).TrimStart('\','/')
            $output = Join-Path $destination $relative
            if (Test-Path -LiteralPath $output -PathType Leaf) {
                $same = (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash -eq
                        (Get-FileHash -LiteralPath $output -Algorithm SHA256).Hash
                if ($same) { continue }
                if (-not $Force) { throw "Existing file differs; rerun with -Force to update: $output" }
            }
            if ($PSCmdlet.ShouldProcess($output, 'Install skill file')) {
                New-Item -ItemType Directory -Path (Split-Path -Parent $output) -Force | Out-Null
                Copy-Item -LiteralPath $file.FullName -Destination $output -Force
            }
        }
        Write-Host "$agentName / $name -> $destination"
    }
}
