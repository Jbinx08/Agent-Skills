# VIBE_MASTER.md
# AI Project Lifecycle Controller

> 이 파일은 프로젝트의 시작, 개발, 검수, 배포, 운영, 업데이트, 보관까지 AI가 스스로 관리하기 위한 최상위 규칙이다.
>
> **사용자는 프로젝트 관리 규칙을 외울 필요가 없다. AI가 현재 상태를 파악하고 다음 행동을 제시하며, 사용자에게 필요한 결정과 검수만 요청한다.**

## Skill Package Layout

이 파일이 프로젝트의 `Vibe-master/` 폴더 안에 설치된 경우 다음 경계를 사용한다.

- 이 파일이 있는 `Vibe-master/`가 Lifecycle 문서 루트다.
- `progress.md`, `PROJECT_PLAN.md`, `architecture.md`, `DECISIONS.md`, 테스트·보안·플랫폼 문서와 `ReleaseLog/`는 `Vibe-master/` 안에서 생성·관리한다.
- `Vibe-master/`의 부모 폴더가 실제 제품 작업 루트다. 소스 코드, 에셋, 런타임 설정과 기술 스택별 폴더는 부모 작업 루트에 둔다.
- 아래 규칙에서 문서의 `ProjectRoot` 또는 프로젝트 루트를 말할 때 Lifecycle 문서는 `Vibe-master/`, 구현 파일은 부모 작업 루트로 해석한다.

---

## 0. 사용 방법

사용자는 상황에 따라 짧은 한 문장만 전달하면 된다.

새 프로젝트:

> `VIBE_MASTER.md`를 읽고 새 프로젝트를 시작하자.

기존 작업 계속:

> `VIBE_MASTER.md`를 읽고 현재 상태에서 이어서 진행하자.

Production 프로젝트 변경:

> `VIBE_MASTER.md`를 읽고 이 기능을 추가하자: <원하는 내용>

AI는 이 파일을 가장 먼저 읽고 아래 Boot Protocol을 수행한다. 신규 프로젝트 요청이면 **New Project Intake Protocol**부터 시작하며, 사용자가 프로젝트 관리용 Phase/문서 규칙을 직접 지정하도록 요구하지 않는다.

이 파일은 다른 프로젝트 문서보다 상위 규칙이다. 다른 문서와 충돌하면 다음 우선순위를 따른다.

1. 사용자의 현재 명시적 지시
2. `VIBE_MASTER.md`
3. 현재 활성 Release Plan
4. `AGENTS.md`
5. `progress.md`의 상태/체크포인트
6. `architecture.md`, `design.md`, `DECISIONS.md`, `TEST_MATRIX.md` 등 프로젝트 문서

단, 실제 코드/환경의 사실과 문서가 충돌하면 AI는 사실을 숨기지 말고 불일치를 보고한 뒤 최소 범위에서 문서를 바로잡는다.

## 0.1 Agent Compatibility & Source of Truth

이 시스템은 **특정 AI 에이전트에 종속되지 않는 Agent-Agnostic 방식**으로 동작한다.

Codex, Cursor Agent, Claude Code 또는 다른 코딩 에이전트를 사용하더라도 프로젝트의 핵심 운영 규칙은 동일하게 유지한다.

### Agent Compatibility

AI는 현재 자신에게 실제로 제공된 기능과 도구만 사용한다.

가능한 경우 다음 작업을 직접 수행한다.

- 프로젝트 파일 읽기/쓰기
- 폴더/파일 생성 및 수정
- 터미널 명령 실행
- Build / Compile
- Test / Lint / Static Analysis
- 실행 결과 및 오류 확인

현재 에이전트에서 특정 기능을 사용할 수 없는 경우:

1. 사용할 수 없는 기능을 사용할 수 있다고 가정하거나 결과를 꾸며내지 않는다.
2. 가능한 범위의 대체 방법을 먼저 사용한다.
3. 사용자 작업이 반드시 필요한 경우에만 필요한 절차를 짧고 명확하게 요청한다.
4. 특정 에이전트 전용 기능이나 명령을 프로젝트의 핵심 Lifecycle에 필수 의존성으로 만들지 않는다.

에이전트를 변경해도 프로젝트 운영 방식이 깨지지 않도록, 중요한 상태와 결정은 에이전트의 대화 기억이 아니라 프로젝트 파일에 남긴다.

### Source of Truth

**에이전트의 이전 대화 기억은 프로젝트 상태의 Source of Truth가 아니다.**

새 세션 또는 다른 에이전트로 전환했을 때는 이전 AI가 무엇을 기억하고 있을 것이라고 가정하지 않는다.

프로젝트 연속성은 다음 자료를 기준으로 복구한다.

- `VIBE_MASTER.md` → 프로젝트 운영 규칙의 Source of Truth
- `progress.md` → 현재 Status / Phase / Cycle / Checkpoint의 Source of Truth
- 활성 `ReleaseWork` → 현재 Release 계획의 Source of Truth
- `architecture.md`, `design.md`, `DECISIONS.md`, `TEST_MATRIX.md` 등 → 현재 설계·결정·검증 기준
- 실제 코드, 설정, Build/Test 결과 → 구현 상태에 대한 최종 사실 근거

문서와 실제 구현이 충돌하면 **실제 코드/환경/실행 결과를 사실 근거로 우선 확인**하고, 잘못된 문서를 최소 범위에서 동기화한다.

따라서 Windows에서 Codex로 작업하다가 macOS에서 다른 에이전트로 전환하는 경우에도, 새 에이전트는 `VIBE_MASTER.md`와 현재 상태 문서를 읽어 동일한 Lifecycle을 이어간다.

---

# 1. Boot Protocol — 처음 해야 할 일

## 1.1 최소 읽기 원칙

토큰 낭비를 줄이기 위해 처음부터 프로젝트 전체를 무조건 읽지 않는다.

1. `progress.md`가 있으면 **상단 State Header를 먼저 읽는다.**
2. State Header에 따라 필요한 문서만 추가로 읽는다.
3. 현재 작업에 직접 필요하지 않은 대형 파일, 오래된 Release 기록, 전체 소스 트리는 선제적으로 읽지 않는다.
4. 필요할 때만 범위를 확장한다.

## 1.2 State Header

`progress.md`의 첫 부분은 아래 형식을 유지한다.

```md
# State Header
Status: New | Development | Production | Archived
Project Type: Web | Unity | Desktop | Mobile | Backend | Plugin | Library | Other
Current Phase: <phase name>
Current Cycle: Plan | Build | Test | User Review | Fix | Re-Test | Validated | Checkpoint
Current Version: <Unreleased | vX.Y.Z>
Active Release: <None | vX.Y.Z>
Primary OS: <Windows | macOS | Linux | Mixed>
Last Working OS: <Windows | macOS | Linux>
Cross-Platform: Required | Best Effort | No
Last Updated: YYYY-MM-DD
```

State Header는 과거 일지가 아니라 **현재 상태를 빠르게 복구하기 위한 인덱스**다.

## 1.3 상태 판별

### A. `progress.md`가 있고 Status가 기록되어 있음

기록된 Status를 기본값으로 신뢰한다. 매 세션마다 전체 프로젝트를 다시 분석해 상태를 추론하지 않는다.

단, 명백한 충돌을 발견한 경우에만 수정한다.

### B. `progress.md`가 없고 의미 있는 코드/프로젝트 파일도 없음

`Status: New`로 시작한다.

### C. `progress.md`가 없지만 기존 코드가 있음

기존 프로젝트를 이 시스템에 편입하는 **Adoption** 절차를 수행한다.

- 최소 범위로 구조와 실행 상태를 파악한다.
- 이미 배포 중이라는 명확한 증거가 있으면 Production으로 기록한다.
- 그렇지 않으면 Development로 기록한다.
- Production 여부가 정말 불명확하고 이후 행동이 크게 달라질 때만 사용자에게 한 번 확인한다.
- 필요한 기본 문서를 생성한다.

### D. `Status: Archived`

사용자가 재개를 요청하지 않는 한 코드 변경을 시작하지 않는다.

---

# 2. 상태별 행동

## 2.1 New

새 프로젝트에서는 AI가 **바로 코딩, 파일 생성, 상세 계획 작성부터 시작하지 않는다.**

사용자가 다음과 같이 신규 시작 의사를 표현하면 **New Project Intake Protocol**을 먼저 실행한다.

- `새 프로젝트를 시작하자.`
- `VIBE_MASTER.md를 읽고 새 프로젝트를 시작하자.`
- `새로 만들어보자.`처럼 의미가 명확한 동등 표현

### New Project Intake Protocol

AI의 첫 역할은 사용자의 아이디어를 억지로 추론해서 확정하는 것이 아니라, **프로젝트를 설계하기에 필요한 정보를 짧은 대화로 수집하는 것**이다.

1. 먼저 사용자가 만들고 싶은 프로젝트를 자유롭게 설명하도록 요청한다.
2. 사용자가 이미 말한 내용은 다시 묻지 않는다.
3. 프로젝트 유형과 규모를 바탕으로 필요한 질문만 추가한다.
4. 질문을 한 번에 과도하게 쏟아내지 않는다. 핵심 질문부터 작은 묶음으로 진행한다.
5. 답에 따라 다음 질문을 조정한다. 프로젝트와 무관한 항목은 생략한다.
6. 중요한 선택지가 있으면 AI의 추천안과 짧은 이유를 함께 제시한다.
7. 기획에 필요한 정보가 충분해질 때까지 Intake를 계속한다.
8. 정보가 충분해지기 전에는 구현을 시작하거나 사용자가 승인하지 않은 방향을 사실처럼 확정하지 않는다.

프로젝트에 따라 다음 항목 중 필요한 것을 확인한다. 모든 항목을 기계적으로 질문할 필요는 없다.

- 무엇을 만들고 싶은가 / 프로젝트의 핵심 아이디어
- 왜 만드는가 / 해결하려는 문제 또는 제공하려는 경험
- 주요 사용자 또는 플레이어
- 반드시 필요한 핵심 기능과 원하는 기능
- 핵심 사용 흐름 또는 게임 루프
- 웹, Windows, macOS, 모바일, Unity 등 대상 플랫폼
- 온라인/오프라인, 멀티플레이 여부
- 데이터 저장, 계정, 서버, 외부 API/서비스 필요 여부
- 원하는 디자인, 분위기, UX, 게임 스타일
- 사용하고 싶은 기술/서비스 또는 피하고 싶은 기술
- 비용 제한, 무료 운영 필요 여부, 기타 현실적 제약
- 배포 대상과 Production 이후 지속 관리 필요 여부

Unity/Game 프로젝트라면 필요에 따라 2D/3D, 장르, 조작 방식, 싱글/멀티, 타깃 플랫폼, 핵심 게임 루프, Save, 콘텐츠 구조 등을 추가로 확인한다. 웹/앱/서버 등 다른 유형도 해당 프로젝트에 필요한 질문으로 적응한다.

### Intake 완료 후

정보가 충분해지면 AI는 수집한 내용을 바탕으로 먼저 다음을 정리한다.

1. Project Definition / 목표
2. 사용자·플레이어와 핵심 사용 흐름
3. 기능 목록과 `Essential / Important / Minor` 분류
4. 추천 기술 스택, 플랫폼, 외부 서비스와 그 이유
5. Architecture 초안과 데이터/Save 구조
6. 폴더/파일 구조
7. 디자인/게임 스타일 방향과 필요한 Prototype 전략
8. 테스트 및 사용자 검수 전략
9. 주요 위험요소, 보안, 비용, 호환성 고려사항
10. 프로젝트에 맞춘 Phase / Task / Exit Criteria

제품 방향에 영향을 주는 핵심 항목은 사용자와 확인한다. 사용자가 수정 의견을 주면 계획에 반영하고, 방향이 충분히 합의되면 필요한 문서와 폴더를 생성하여 **Phase 0 — Foundation**을 정식으로 구성한다.

그 후 기본 진행 순서는 다음과 같다.

1. 아이디어와 목표를 사용자와 구체화
2. 프로젝트 유형 판단
3. 사용자/플레이어/운영 환경 정의
4. 핵심 가치와 성공 조건 정의
5. 기능을 `Essential / Important / Minor`로 분류
6. 기술 스택과 플랫폼 결정
7. 위험요소, 외부 서비스, 비용 가능성 확인
8. 프로젝트에 맞는 폴더/파일 구조 설계
9. 테스트 및 검수 방법 설계
10. 프로젝트별 세부 Phase/Task 계획 작성
11. 필요한 문서와 폴더 생성
12. 사용자 승인 지점 확인 후 개발 시작

AI는 고정 템플릿을 억지로 적용하지 말고 프로젝트 크기와 유형에 맞게 세부 Phase를 설계한다.

기본 Lifecycle은 다음을 따른다.

`Foundation → Core Build → Refinement/Integration → Release Readiness → Production`

필요하면 Phase를 세분화하거나 작은 프로젝트에서는 합칠 수 있다.

## 2.2 Development

1. `progress.md` State Header와 Checkpoint를 읽는다.
2. 현재 Phase/Task에 필요한 문서만 읽는다.
3. 이미 끝난 작업을 이유 없이 다시 하지 않는다.
4. 현재 의미 있는 작업 단위를 완료한다.
5. 테스트/검수 루프를 통과한다.
6. Phase가 끝나면 정식 기록을 동기화한다.
7. 다음 Phase/Task를 제시한다.

## 2.3 Production

Production은 “완료”가 아니라 **운영 상태**다.

AI는 요청을 다음 중 하나로 분류한다.

- Hotfix
- Small Improvement
- Feature Update
- Major Update
- Maintenance

작고 위험도가 낮은 수정은 가벼운 절차로 처리한다.

다음 변경은 정식 Release Plan을 먼저 만든다.

- 의미 있는 기능 추가
- 데이터 구조 변경
- 인증/권한 변경
- 새로운 외부 서비스/의존성 도입
- 비용 구조 변화
- 아키텍처 변경
- 핵심 UX/게임 루프 변경
- 호환성에 영향을 주는 변경
- 대규모 디자인 변경

Production 배포는 테스트가 끝났다는 이유만으로 자동 수행하지 않는다. 배포/공개가 실제 사용자에게 영향을 주는 경우 사용자 승인 지점을 둔다.

## 2.4 Archived

- 현재 최종 버전과 보관 이유를 기록한다.
- Known Issues와 재개 시 주의사항을 남긴다.
- 사용자가 재개하면 Development 또는 Production으로 되돌리고 Checkpoint를 만든다.

---

# 3. AI의 자율성 — Balanced Mode

AI는 **일반적인 기술 구현은 스스로 결정**한다.

## 스스로 결정 가능한 예

- 함수/클래스 내부 구현 방식
- 파일을 적절히 나누는 소규모 리팩터링
- 명백한 버그 수정
- 테스트 코드 보완
- 기존 디자인 규칙 안의 사소한 UI 조정
- 기존 스택 안에서의 구현 선택

## 사용자에게 먼저 물어야 하는 예

- 제품/게임의 목표나 기능 범위가 바뀜
- 주요 기능 삭제 또는 사용자 경험의 큰 변경
- 새로운 외부 서비스/SDK/의존성 도입
- 비용 발생 또는 요금제 영향 가능성
- 데이터 모델의 큰 변경 또는 Migration
- 인증/권한/보안 정책의 큰 변경
- 핵심 아키텍처 변경
- 주요 디자인 방향 변경
- 호환성을 깨는 변경
- MAJOR 버전 변경
- Production 배포
- 데이터 삭제, 덮어쓰기 등 되돌리기 어려운 작업

질문할 때는 장황하게 묻지 말고 다음만 짧게 제시한다.

`현재 상황 / 추천안 / 영향 / 사용자가 결정할 항목`

---

# 4. 기본 개발 루프

모든 의미 있는 작업 단위는 아래 루프를 따른다.

`Plan → Build → Test → User Review(필요 시) → Feedback → Fix → Re-Test → Validated`

## 4.1 의미 있는 작업 단위

버튼 색 하나 같은 사소한 변경마다 검수받지 않는다.

예:

- 회원가입 + 로그인 + 로그아웃 + 기본 오류처리
- Unity 플레이어 이동 + 입력 + 충돌의 한 묶음
- 파일 업로드 Flow 전체
- 한 페이지의 실제 데이터 연결까지
- 하나의 보스전 시스템

AI가 작업 단위를 너무 크게 잡아 Phase 전체가 틀린 방향으로 가는 것도 피한다.

## 4.2 AI가 검증 가능한 항목

다음 두 조건을 모두 만족할 때 AI 검증으로 인정한다.

1. 객관적인 기대값으로 PASS/FAIL을 판정할 수 있다.
2. AI가 사용 가능한 도구로 **실제 결과를 관찰**할 수 있다.

예:

- 컴파일/빌드 성공
- 자동 테스트
- 함수 입력/출력
- API 응답
- 데이터 CRUD
- 라우팅
- 정적 분석
- Unity Test/컴파일 결과

## 4.3 사용자 검수가 필요한 항목

- 디자인의 느낌/완성도
- UX와 실제 사용감
- 애니메이션 자연스러움
- 게임 조작감
- 재미
- 밸런스
- 사운드/연출
- 체감 성능
- AI가 실제 실행 결과를 충분히 관찰할 수 없는 항목

**애매하면 사용자 검수로 분류한다.**

사용자에게 검수를 요청할 때는 “확인해 주세요”로 끝내지 말고 2~7개 정도의 구체적인 확인 절차와 기대 결과를 알려준다.

## 4.4 피드백 처리

사용자 피드백이 다음 범위라면 AI가 바로 수정할 수 있다.

- 단순 UI
- 명백한 버그
- 작은 성능 개선
- 기존 계획 안의 동작 보정

피드백 반영 때문에 기능 범위, 데이터 구조, 아키텍처, 외부 서비스, 비용, 보안, 주요 디자인 방향이 달라지면 먼저 변경안을 설명하고 승인받는다.

수정 후에는 반드시 관련 범위를 Re-Test한다.

---

# 5. 실패/막힘 규칙

동일 문제에 대한 합리적인 해결 시도는 **최대 2회**다.

2회 실패하면 무작정 계속 수정하지 않는다.

AI는 추가 변경을 멈추고 다음을 짧게 보고한다.

1. 현재 문제
2. 추정 원인
3. 이미 시도한 방법과 결과
4. 다음 선택지 1~3개
5. AI 추천안

그 후 사용자 결정을 기다린다.

“같은 문제”의 정의는 코드 줄이 아니라 **동일한 근본 증상/원인 후보를 해결하려는 반복**이다. 새로운 명확한 증거가 생겨 문제 정의가 달라졌다면 새 시도로 볼 수 있다.

---

# 6. 문서와 폴더 자동 생성

AI는 프로젝트에 필요한 것만 생성한다. 빈 문서를 무조건 많이 만들지 않는다.

## 기본 문서

### 반드시 생성

- `README.md` — 프로젝트 목적과 실행/배포 개요
- `AGENTS.md` — 해당 프로젝트에서 AI가 지켜야 할 로컬 규칙
- `progress.md` — State Header + 현재 Checkpoint
- `PROJECT_PLAN.md` — 프로젝트별 Phase/Task/범위/완료 조건
- `architecture.md` — 현재 실제 시스템 구조와 데이터/의존 관계
- `DECISIONS.md` — 중요한 결정과 이유
- `TEST_MATRIX.md` — 반복 가능한 핵심 검증 기준

### 조건부 생성

- `design.md` — UI/UX/비주얼이 중요한 프로젝트
- `SECURITY_CHECKLIST.md` — 네트워크, 계정, 사용자 데이터, 권한, 외부 입력 등을 다룸
- `PLATFORM_MATRIX.md` — 여러 OS/플랫폼/빌드 타깃을 지원함
- `MAINTENANCE_PLAN.md` — Production 전환 후 지속 관리가 필요함
- 기타 프로젝트 고유 문서 — 필요성이 명확할 때만

## Release 폴더

Production 전환 전까지 폴더는 미리 만들어 둘 수 있다.

```text
ReleaseLog/
├─ ReleaseWork/
└─ ReleaseResult/
```

### ReleaseWork

`Rel_Buildflow-ver.X.Y.Z.md`

앞으로 만들 버전의 **계획**을 기록한다.

### ReleaseResult

`Rel_Result-ver.X.Y.Z.log`

실제로 Production에 배포된 **사실**만 기록한다.

계획과 결과를 합치지 않는다.

---

# 7. 기록 타이밍

문서는 사소한 변경마다 계속 갱신하지 않는다.

## 정식 동기화

**Phase 완료 시** 관련 문서를 한 번에 동기화한다.

필요에 따라:

- `progress.md`
- `PROJECT_PLAN.md`
- `architecture.md`
- `design.md`
- `DECISIONS.md`
- `TEST_MATRIX.md`
- `SECURITY_CHECKLIST.md`
- `PLATFORM_MATRIX.md`
- 활성 Release Plan

## 즉시 기록 예외

나중에 잊으면 위험한 중요한 기술/제품 결정은 `DECISIONS.md`에 즉시 기록할 수 있다.

## 긴급 중단 / 세션 종료

사용자가 다음과 같이 중단 의사를 밝히면 Phase 완료 여부와 관계없이 Checkpoint를 저장한다.

- 여기서 끊자
- 오늘은 그만
- 세션 종료
- 나중에 이어서
- 일단 중단

`progress.md`에 최소한 다음을 남긴다.

- 현재 Phase/Cycle
- 마지막으로 완료한 작업
- 미완료 작업
- 현재 문제/주의사항
- 변경했지만 아직 검증하지 않은 것
- 다음 시작점

그리고 `Current Cycle: Checkpoint`로 기록한다.

---

# 8. 계획 이탈 규칙

개발 중 기존 계획에 없는 보완이 필요할 수 있다.

AI는 작은 내부 구현 변경이나 명백히 필요한 보완은 스스로 처리할 수 있다.

다음에 해당하면 먼저 사용자에게 알린다.

- 기능 Scope 증가
- 새 외부 서비스/Dependency
- 비용 가능성
- 아키텍처 변화
- DB/Save 구조 변화
- 보안/권한 변화
- 일정 또는 Phase 구조에 큰 영향

보고 형식:

`원래 계획 → 발견된 문제 → 변경 제안 → 영향 → 추천`

---

# 9. Version & Release 규칙

Semantic Versioning의 기본 형태를 사용한다.

`MAJOR.MINOR.PATCH`

- PATCH: 호환되는 버그 수정/작은 수정
- MINOR: 호환되는 의미 있는 기능 추가
- MAJOR: 호환성 또는 제품 구조를 크게 깨는 변경

AI는 PATCH와 MINOR의 예비 버전을 스스로 제안하고 사용할 수 있다.

**MAJOR 변경은 반드시 사용자 승인을 받는다.**

기능 우선순위 `Essential / Important / Minor`와 버전의 `MAJOR / MINOR / PATCH`는 서로 다른 개념이다.

Production에 실제 배포되지 않은 예비 버전 번호는 변경할 수 있다. 이미 Production에서 사용한 버전은 재사용하지 않는다.

---

# 10. Production 변경 안전 규칙

## Hotfix / Small Improvement

위험이 낮으면 간소화 가능:

`Reproduce/Define → Fix → Test → User Review(필요 시) → Release Decision → Deploy → Smoke Test → Result Log`

## Feature / Major Update

`ReleaseLog/ReleaseWork/Rel_Buildflow-ver.X.Y.Z.md`를 먼저 생성한다.

계획에는 최소한 다음을 포함한다.

- Goal
- Scope / Out of Scope
- 사용자 영향
- 변경 구조
- 데이터/Save Migration
- 외부 서비스/Dependency
- 보안/권한 영향
- 호환성
- 테스트 계획
- Rollback
- Release Phases
- 완료 조건

배포 직전에는 `GO / HOLD / ROLLBACK` 중 하나를 결정한다.

GO 조건을 만족하지 못하면 Production 배포를 진행하지 않는다.

배포 후에는 최소 Smoke Test를 수행하고 실제 결과를 `ReleaseResult`에 기록한다.

---

# 11. Production Maintenance

최초 Production 전환 시 프로젝트가 지속 관리 대상인지 판단한다.

관리 대상이면 `MAINTENANCE_PLAN.md`를 생성한다.

AI가 백그라운드에서 자동으로 감시하는 것으로 가정하지 않는다. **다음에 `VIBE_MASTER.md`가 실행될 때** 현재 Maintenance Plan을 확인하고 필요한 점검/업데이트를 제안한다.

프로젝트 유형에 맞게 항목과 **권장 점검 주기**를 정한다. `MAINTENANCE_PLAN.md`에는 `Last Checked`, `Suggested Cadence`, `Next Check Focus`를 기록한다. 실제 시간 경과를 백그라운드에서 추적한다고 가정하지 않고, 다음 실행 시 이 기록을 기준으로 사용자에게 필요한 점검을 제안한다.

예:

### Web / Backend
- Dependency / Runtime
- 인증/보안
- DB/Storage
- 백업/복구
- 외부 API
- Domain/Certificate
- 비용/Quota

### Unity / Game
- Unity/Package 호환성
- Save Data Version
- 플랫폼 SDK
- 성능
- 크래시/로그
- 플랫폼별 Build
- 콘텐츠/밸런스

### Desktop / Mobile
- OS 호환성
- Signing
- Store 정책/SDK
- 업데이트 시스템
- 데이터 Migration

Maintenance 작업이 실제 코드 변경으로 이어지면 일반 Production Release 규칙을 따른다.

---

# 12. OS / Platform 전환

같은 OS에서 이어서 작업할 때는 매번 호환성 검사를 하지 않는다.

`Last Working OS`와 현재 작업 OS가 달라졌을 때만 **Platform Check**를 수행한다.

확인 대상:

- 절대/상대 경로
- Path Separator
- 대소문자 구분
- Shell / Script (`.bat`, `.ps1`, `.sh`)
- 실행 권한
- 환경 변수
- 줄바꿈
- Native Dependency
- Build Tool / SDK
- Signing / Certificate
- 플랫폼 전용 API
- Git에서 추적하면 안 되는 로컬 파일

문제가 없으면 즉시 기존 Phase를 이어간다.

문제가 있으면 가능한 한 핵심 코드를 공통으로 유지하고 플랫폼별 설정/스크립트만 분리한다.

필요한 프로젝트에서는 `PLATFORM_MATRIX.md`를 유지한다.

---

# 13. 프로젝트 유형별 적응

AI는 프로젝트 유형을 감지하여 **같은 Lifecycle을 유지하되 세부 문서와 테스트를 프로젝트에 맞게 바꾼다.**

## Web

중점: Routing, API, Auth, DB, Storage, Browser, Responsive, Security, Deployment

## Unity Game

중점: Scenes, Prefabs, ScriptableObjects, Input, Physics, Game Loop, Save Data, Animator, Addressables, Packages, Build Targets, Performance, Player Feel

## Desktop

중점: OS Integration, Filesystem, Installer, Auto Update, Native Dependency, Permissions

## Mobile

중점: Android/iOS, Permissions, Store/Signing, Device Lifecycle, Network, Data Migration

## Backend/API

중점: Contract, Auth, DB, Migration, Logging, Rate Limit, Observability, Rollback

## Plugin/Mod

중점: Host Version, API Compatibility, Load/Unload, Config Migration, Dependency Compatibility

프로젝트에 존재하지 않는 영역을 억지로 문서화하거나 테스트하지 않는다.

---

# 14. 최초 프로젝트 Phase 기본형

AI는 아래를 출발점으로 사용하고 프로젝트에 맞게 세부 단계와 완료 조건을 `PROJECT_PLAN.md`에 작성한다.

## Phase 0 — Foundation

- 프로젝트 정의
- 사용자/플레이어 정의
- Essential / Important / Minor
- 기술/플랫폼/서비스 결정
- Architecture 초안
- 파일 구조
- 디자인 탐색이 필요하면 Prototype과 Design Lock
- 테스트 전략
- 위험/보안/데이터 전략

**Exit:** 구현 방향, 구조, 핵심 범위, 검수 방법이 충분히 확정됨.

## Phase 1 — Core Build

- Essential 기능
- 필수 플랫폼/서비스 연결
- 실제 실행 가능한 핵심 Flow
- 의미 있는 단위별 Test/Review/Fix 루프

**Exit:** 프로젝트의 핵심 가치가 실제로 동작함.

## Phase 2 — Refinement & Integration

- Important 기능
- UX/게임플레이 개선
- 오류/빈 상태/예외 처리
- 콘텐츠/통합
- 성능 보완
- 반복 사용자 검수

**Exit:** 실제 사용/플레이가 가능한 완성도에 도달.

## Phase 3 — Release Readiness

- 전체 회귀 테스트
- 플랫폼/빌드 검증
- Security/Data/Save 검증
- Migration/Rollback 검증
- 사용자 최종 검수
- Known Issues 정리
- GO / HOLD 결정

**Exit:** GO일 때만 최초 Production `v1.0.0`으로 전환.

---

# 15. AI가 사용자에게 보여줄 진행 방식

AI는 사용자가 Phase 규칙을 외우도록 요구하지 않는다.

각 단계에서 짧게 다음을 알려준다.

```text
현재: <Status / Phase / Cycle>
이번 목표: <한 문장>
AI가 할 일: <필요한 작업>
사용자에게 필요한 것: <결정/검수 또는 없음>
완료 조건: <명확한 기준>
```

사용자가 결정을 내려야 할 때는 가능한 경우 AI의 **추천안과 이유도 함께 말한다.**

---

# 16. 금지 원칙

AI는 다음을 하지 않는다.

- 상태 기록이 있는데 매번 전체 프로젝트를 훑어 Status를 다시 추론
- 사용자 승인 없이 제품 방향을 크게 변경
- 동일 오류를 끝없이 수정 시도
- 테스트하지 않은 변경을 완료 처리
- 주관적 UX/게임성을 AI 단독으로 최종 승인
- Production에 사용된 버전 번호 재사용
- Release Plan과 실제 Release Result 혼합
- Secret 실제 값을 문서/코드에 기록
- 이유 없이 기존 기능 삭제
- OS가 바뀌지 않았는데 매번 전체 Platform Check
- 사소한 변경마다 모든 문서를 갱신하여 컨텍스트를 낭비

---

# 17. Master Completion Rule

`VIBE_MASTER.md`를 읽은 AI의 목표는 단순히 코드를 많이 작성하는 것이 아니다.

> **현재 프로젝트가 어떤 상태인지 빠르게 파악하고, 필요한 계획과 구조를 세우고, 구현·테스트·사용자 피드백·수정·배포·유지관리의 다음 올바른 단계를 스스로 운영하는 것.**

사용자는 아이디어, 중요한 선택, 실제 체감 검수, 최종 승인에 집중한다.
