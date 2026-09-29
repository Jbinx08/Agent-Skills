# Codex adapter

`install.ps1 -Agent Codex` copies each shared skill to `~/.codex/skills/<name>/`, or `$env:CODEX_HOME/skills/<name>/` when CODEX_HOME is set. `agents/openai.yaml` provides Codex display metadata; the skill instructions and resources stay in the common folder.

