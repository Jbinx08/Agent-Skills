# PROJECT_STRUCTURE.md
# Project File & Folder Structure

이 문서는 프로젝트에서 어떤 파일과 폴더를 만들고, 각각 어떤 역할을 맡기는지 정의한다.

AI는 프로젝트를 시작할 때 이 구조를 참고하되 실제 기술 스택에 맞게 필요한 폴더는 추가할 수 있다.

---

# Recommended Root Structure

```text
ProjectRoot/
├─ README.md
├─ AGENTS.md
├─ BUILD_FLOW.md
├─ RELEASE_BUILD_FLOW.md
├─ PROJECT_STRUCTURE.md
├─ architecture.md
├─ design.md
├─ progress.md
├─ DECISIONS.md
├─ TEST_MATRIX.md
├─ SECURITY_CHECKLIST.md
│
├─ ReleaseLog/
│  ├─ ReleaseWork/
│  │  ├─ Rel_Buildflow-ver.1.1.0.md
│  │  └─ Rel_Buildflow-ver.2.0.0.md
│  │
│  └─ ReleaseResult/
│     ├─ Rel_Result-ver.1.1.0.log
│     └─ Rel_Result-ver.2.0.0.log
│
├─ src/
├─ public/
├─ tests/
└─ ... 기술 스택별 폴더
```

---

# Core Files

## README.md

목적:

> 이 서비스가 무엇인지 설명한다.

포함 권장:

- 서비스 이름
- 목적
- 주요 기능
- 기술 스택
- 로컬 실행 방법
- 환경 변수 이름
- 배포 방식
- 개발 상태

Secret 실제 값은 적지 않는다.

---

## AGENTS.md

목적:

> AI Agent가 이 프로젝트에서 어떻게 행동해야 하는지 정의한다.

포함 권장:

- 먼저 읽어야 할 문서
- 수정 전 확인 규칙
- 구현 우선순위
- 테스트 규칙
- 파일 생성/삭제 규칙
- 문서 업데이트 규칙
- Phase 규칙
- 금지 사항

예:

- 기존 기능을 이유 없이 삭제하지 않는다.
- 작업 후 반드시 관련 테스트를 실행한다.
- 구조 변경 시 architecture.md를 갱신한다.
- 릴리스 관련 작업은 RELEASE_BUILD_FLOW.md를 따른다.

---

## architecture.md

목적:

> 현재 Production/개발 상태의 실제 시스템 구조를 설명한다.

계획이 아니라 **현재 사실**을 적는다.

포함 권장:

- Frontend
- Backend
- Authentication
- Database
- Storage
- API
- External Services
- Environment
- Deployment
- Data Flow

---

## design.md

목적:

> 현재 확정된 디자인 시스템을 정의한다.

디자인 변경이 없으면 자주 수정할 필요 없다.

---

## progress.md

목적:

> 새 세션이 현재 상태를 빠르게 파악하게 한다.

최신 상태만 유지한다.

권장 구조:

```md
# Current Status

Current Version:
Current Phase:
Current Task:

## Completed

## In Progress

## Known Issues

## Next
```

과거 작업 내역을 무한히 쌓지 않는다.

---

## DECISIONS.md

목적:

> 중요한 기술적/구조적 결정을 “왜 그렇게 했는지” 보존한다.

`architecture.md`는 현재 구조만 보여주므로, 시간이 지나면 이유가 사라질 수 있다.

예:

- Firebase Auth를 선택한 이유
- R2로 Storage를 이전한 이유
- 특정 DB 구조를 선택한 이유
- 특정 기능을 이번 Release에서 제외한 이유

이 파일은 Reset하지 않는다.

---

## TEST_MATRIX.md

목적:

> 핵심 기능이 업데이트 때문에 깨지지 않았는지 반복해서 확인할 기준을 유지한다.

Release Phase 4에서 사용한다.

---

## SECURITY_CHECKLIST.md

목적:

> 배포 전에 반복적으로 확인해야 할 보안 기준을 고정한다.

---

# ReleaseLog

## ReleaseWork

경로:

`ReleaseLog/ReleaseWork/`

파일명:

`Rel_Buildflow-ver.X.Y.Z.md`

역할:

> 앞으로 배포할 버전을 어떻게 만들 것인지 기록.

계획 문서이므로 Production 결과와 다를 수 있다.

---

## ReleaseResult

경로:

`ReleaseLog/ReleaseResult/`

파일명:

`Rel_Result-ver.X.Y.Z.log`

역할:

> 실제로 Production에 배포된 결과 기록.

계획이 아닌 사실만 적는다.

---

# File Naming Rules

Build System 문서:

- `BUILD_FLOW.md`
- `RELEASE_BUILD_FLOW.md`
- `PROJECT_STRUCTURE.md`
- `DECISIONS.md`
- `TEST_MATRIX.md`
- `SECURITY_CHECKLIST.md`

프로젝트 상태 문서:

- `README.md`
- `AGENTS.md`
- `architecture.md`
- `design.md`
- `progress.md`

Release 계획:

- `Rel_Buildflow-ver.1.1.0.md`

Release 결과:

- `Rel_Result-ver.1.1.0.log`

버전은 반드시 파일명과 파일 내부 값이 일치해야 한다.

---

# Creation Timing

## 프로젝트 시작 즉시

생성:

- README.md
- AGENTS.md
- BUILD_FLOW.md
- RELEASE_BUILD_FLOW.md
- PROJECT_STRUCTURE.md
- architecture.md
- progress.md
- DECISIONS.md
- TEST_MATRIX.md
- SECURITY_CHECKLIST.md
- ReleaseLog/ReleaseWork/
- ReleaseLog/ReleaseResult/

## 디자인 확정 시

생성 또는 확정:

- design.md

## Feature/Major Release 계획 시

생성:

- `ReleaseLog/ReleaseWork/Rel_Buildflow-ver.X.Y.Z.md`

## Production 배포 성공 시

생성:

- `ReleaseLog/ReleaseResult/Rel_Result-ver.X.Y.Z.log`

---

# Do Not Duplicate Responsibilities

- 과거 Release 기록을 `progress.md`에 쌓지 않는다.
- 현재 시스템 설명을 `ReleaseResult`에만 의존하지 않는다.
- 계획을 `architecture.md`에 사실처럼 적지 않는다.
- Release 계획과 실제 결과를 같은 파일에 섞지 않는다.
- Secret 값을 어떤 문서에도 저장하지 않는다.
