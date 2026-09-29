---
name: vibe-master-flow
description: Initialize or resume the Vibe Master project lifecycle when the user says "Vibe_Master Flow 시작", asks to apply Vibe Master to a project, or invokes this skill. Do not use for unrelated build questions or read-only inspection.
---

# Vibe Master Flow

Resolve the target from the user's path, or use the current project root. Keep product source in that root and the managed documents in `<target>/Vibe-master`.

Run `python scripts/apply_vibe_master.py <target>` from this skill directory (Python 3.10+). On Windows, the original `scripts/Apply-VibeMaster.ps1` remains available. Both copy bundled `assets/Vibe-master` files and skip existing files. Replace existing files only when the user explicitly asks for replacement; pass `--force` to the Python script or `-Force` to PowerShell.

Verify `<target>/Vibe-master/VIBE_MASTER.md`, then read it fully and follow its lifecycle guidance in the context of the user's current request. For an existing project, read its `progress.md` state before continuing. Preserve existing project records. For a newly initialized project without `progress.md`, begin the New Project Intake Protocol by asking the user to describe the project.

The complete original documents and templates are in `assets/Vibe-master/`.
