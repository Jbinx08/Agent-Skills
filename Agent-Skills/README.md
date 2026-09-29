# Agent-Skills

두 원본을 공통 Agent Skills 폴더로 정리한 배포용 구조다. 이 폴더를 GitHub `Agent-Skills` 저장소의 루트에 올린다.

```text
Agent-Skills/
├─ skills/
│  ├─ vibe-drive/
│  │  ├─ SKILL.md
│  │  ├─ scripts/vibe_drive.py
│  │  └─ references/GoogleDrive_Skill.original.md
│  └─ vibe-master-flow/
│     ├─ SKILL.md
│     ├─ agents/openai.yaml
│     ├─ scripts/Apply-VibeMaster.ps1
│     ├─ scripts/apply_vibe_master.py
│     └─ assets/Vibe-master/...
├─ adapters/{codex,claude-code,cursor}/README.md
├─ install.ps1
├─ setup-drive.ps1
├─ requirements-drive.txt
├─ legacy/                  # 기존 설치 방식과 원본 안내문 보관
└─ .gitignore
```

## 원본 파일 배치

| 원본 | 새 위치 | 처리 |
| --- | --- | --- |
| `GoogleDriveSkill/vibe-drive/` | `skills/vibe-drive/` | 실행 코드 그대로 복사, SKILL.md만 공용 설치 설명으로 수정 |
| `GoogleDriveSkill/GoogleDrive_Skill.md` | `skills/vibe-drive/references/GoogleDrive_Skill.original.md` | 원문 보존 |
| `GoogleDriveSkill/requirements.txt` | `requirements-drive.txt` | 원문 보존 |
| `GoogleDriveSkill/install.py`, `install.cmd`, `install.command`, `authorize_drive.py`, `.gitignore` | `legacy/google-drive/` | 원문 보존, 새 설치에는 사용하지 않음 |
| `VibeMasterSkillKit/.../skill/vibe-master-flow/` | `skills/vibe-master-flow/` | 문서·템플릿·PowerShell 코드·Codex 메타데이터 보존, SKILL.md 수정 |
| `VibeMasterSkillKit/.../README.md`, 설치·삭제 도구 | `legacy/vibe-master/` | 원문 보존, 새 설치에는 사용하지 않음 |
| 두 원본의 `SKILL.md` | 각 `legacy/`의 `SKILL.original.md` | 변경 전 문구 보존 |
| `GoogleDriveSkill/credentials.json`, `token.json` | **저장소에 포함하지 않음** | 사용자 PC의 `~/.vibe-drive/`에만 보관 |

`legacy/` 파일은 이전 배포 형태를 기록하기 위한 것이며, 현재 폴더 배치에서 그대로 실행하는 설치기는 아니다. 이후 유지보수는 `skills/`와 루트 설치기를 기준으로 한다.

## Windows 설치

PowerShell에서 저장소 루트로 이동한 뒤 실행한다.

```powershell
.\install.ps1
```

기본값은 두 스킬을 Codex, Claude Code, Cursor의 사용자 스킬 폴더에 각각 복사한다. 하나만 설치하려면 `-Agent Codex -Skill vibe-master-flow`처럼 지정한다. 기존 파일 내용이 다르면 중단한다. 새 버전으로 갱신할 때만 `-Force`를 사용한다. `-WhatIf`로 복사 예정 경로를 볼 수 있다. 설치 경로는 각 `adapters/` 안내에 정리했다. `CODEX_HOME`을 쓰는 경우 Codex는 해당 위치의 `skills/`를 사용한다.

Google Drive 기능은 설치 후 Python 3.10 이상과 별도 설정이 필요하다.

```powershell
.\setup-drive.ps1 -CredentialsPath 'C:\path\to\credentials.json'
& "$env:USERPROFILE\.vibe-drive\venv\Scripts\python.exe" "$env:USERPROFILE\.codex\skills\vibe-drive\scripts\vibe_drive.py" auth
```

위 두 번째 줄은 Codex 기본 경로의 예다. 다른 도구로 설치했다면 그 도구의 스킬 경로를 쓴다. `setup-drive.ps1`은 기존 `~/.vibe-drive/credentials.json`을 덮어쓰지 않고 `token.json`을 복사하지 않는다. 인증은 `auth` 실행 시 생성한다. Google Drive에 접근할 때는 이 코드가 Drive 전체 접근 범위를 요청한다. 원본 동작을 보존한 것이다.

macOS/Linux에서는 각 도구의 `~/.<tool>/skills/`에 `skills/` 아래의 두 폴더를 복사하고, `python3 -m venv ~/.vibe-drive/venv`와 `~/.vibe-drive/venv/bin/python -m pip install -r requirements-drive.txt`로 Drive 환경을 준비한다. OAuth 파일은 `~/.vibe-drive/`에 둔다.

## 확인

설치 후 도구를 새로 열어 스킬 목록을 확인한다. Vibe Master는 프로젝트에서 `Vibe_Master Flow 시작`, Drive는 명시적인 프로젝트 저장·복원 요청으로 사용한다. `Vibe-master` 문서와 Drive ZIP은 각 스킬이 실제 요청을 받을 때 생성된다.
