---
name: vibe-master-flow
description: Initialize or resume the Vibe Master project lifecycle when the user says "Vibe_Master Flow 시작", "Vibe Master Flow 시작", asks to apply Vibe Master to a project folder, or explicitly invokes $vibe-master-flow. Copy the bundled Vibe-master control documents into the target workspace, read VIBE_MASTER.md, and begin the correct new-project or continuation flow. Do not use for unrelated build-system questions or read-only inspection.
---

# Vibe Master Flow

Apply and operate the bundled Vibe Master lifecycle system.

## Resolve the target

1. Use a folder explicitly supplied by the user.
2. Otherwise use the current workspace root.
3. The managed document root is `<target>/Vibe-master`; the parent `<target>` remains the product source workspace.

## Initialize

Run `scripts/Apply-VibeMaster.ps1` with the resolved target path. The script copies every bundled file from `assets/Vibe-master` and skips existing files by default.

Do not pass `-Force` unless the user explicitly asks to replace existing Vibe Master files. If `Vibe-master` already exists, preserve it and fill only missing bundled files.

After applying, verify that `<target>/Vibe-master/VIBE_MASTER.md` exists.

## Start or continue the lifecycle

Read `<target>/Vibe-master/VIBE_MASTER.md` completely and follow it as the lifecycle controller, subject to the user's current instructions.

- Treat `<target>/Vibe-master` as the document root for `progress.md`, `PROJECT_PLAN.md`, `architecture.md`, `DECISIONS.md`, test/security/platform documents, and `ReleaseLog`.
- Treat `<target>` as the root for source code, assets, runtime configuration, and stack-specific project folders.
- For a newly initialized folder with no `progress.md`, enter `Status: New` and immediately begin the New Project Intake Protocol. Ask the user to describe the project before implementation.
- For an existing installation, do not reset it. Read the `progress.md` State Header first and resume according to the Boot Protocol.
- Never overwrite project files or existing lifecycle records merely because the skill was invoked again.

## Bundled resources

- `assets/Vibe-master/` contains the complete original Vibe Build Flow document set and templates.
- `scripts/Apply-VibeMaster.ps1` performs deterministic, non-destructive installation into a workspace.
