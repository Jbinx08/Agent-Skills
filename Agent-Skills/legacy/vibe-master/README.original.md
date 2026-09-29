# Vibe Master Skill Kit

Codex용 `vibe-master-flow` 전역 개인 스킬과 Windows 원클릭 설치·삭제 도구다.

## 설치 — 한 번만 실행

`Install-VibeMaster.cmd`를 더블클릭한다. 관리자 권한은 필요 없다.

스킬이 `%USERPROFILE%\.agents\skills\vibe-master-flow`에 설치되며, 이후 프로젝트마다 CMD를 다시 실행할 필요가 없다. 현재 열려 있는 Codex에서 바로 보이지 않을 때만 Codex를 한 번 다시 시작한다.

## 모든 프로젝트에서 사용

원하는 프로젝트를 Codex로 연 뒤 채팅에 다음 문구만 입력한다.

```text
Vibe_Master Flow 시작
```

Codex가 현재 프로젝트에 `Vibe-master` 폴더와 전체 템플릿을 구성하고 `VIBE_MASTER.md`를 읽은 뒤 새 프로젝트 Intake를 시작한다. 기존 `Vibe-master` 파일은 기본적으로 덮어쓰지 않는다.

`$vibe-master-flow`로 명시 호출하는 것도 가능하지만 필수는 아니다.

## 삭제 — 한 번만 실행

`Uninstall-VibeMaster.cmd`를 더블클릭한다. 전역 스킬만 제거한다.

각 프로젝트에 이미 생성된 `Vibe-master` 폴더는 프로젝트 기록이므로 자동 삭제하지 않는다.
