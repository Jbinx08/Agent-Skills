# START_HERE.md
# Vibe Build System

이 패키지의 시작점은 `VIBE_MASTER.md` 하나다.

사용자는 상황에 따라 아래처럼 짧게 말하면 된다.

## 새 프로젝트

> `VIBE_MASTER.md`를 읽고 새 프로젝트를 시작하자.

AI는 바로 코딩하지 않고 **New Project Intake Protocol**을 시작한다. 어떤 프로젝트를 만들고 싶은지 먼저 묻고, 답에 따라 필요한 기능·플랫폼·디자인·기술·제약사항 등을 추가로 질문한다. 정보가 충분해지면 프로젝트 정의, 기능 우선순위, 구조, 테스트 전략, Phase 계획을 만들고 사용자와 방향을 확인한 뒤 개발을 시작한다.

## 기존 프로젝트 이어서

> `VIBE_MASTER.md`를 읽고 현재 상태에서 이어서 진행하자.

AI는 `progress.md`의 State Header와 Checkpoint를 우선 읽고 현재 Phase와 다음 시작점을 복구한다.

## Production 프로젝트 변경

> `VIBE_MASTER.md`를 읽고 이 기능을 추가하자: <원하는 내용>

AI는 현재 Production 버전과 요청 규모를 확인하고 Hotfix / Small Improvement / Feature Update / Major Update / Maintenance 중 적절한 흐름으로 진행한다.

## 핵심 철학

- 사용자가 Phase와 문서 규칙을 외우지 않는다.
- AI가 프로젝트 운영을 맡고 사용자는 중요한 결정과 체감 검수에 집중한다.
- 객관적으로 검증 가능한 것은 AI가 검증한다.
- 디자인/UX/게임 감각처럼 사람이 확인해야 하는 것은 사용자 검수를 요청한다.
- 의미 있는 작업 단위마다 Test → Review → Feedback → Fix → Re-Test 루프를 적용한다.
- Phase 완료 시 정식 기록을 동기화한다.
- 급하게 중단하면 `progress.md` Checkpoint를 남긴다.
- Production 이후에는 Release + Maintenance 체계로 전환한다.
- OS가 실제로 바뀐 경우에만 Platform Check를 수행한다.

## 포함 파일

`BuildSystem/`은 Master가 필요할 때 참고할 상세 규칙이다. AI에게 매번 전부 읽히지 않아도 된다.

`Templates/`는 새 프로젝트 문서를 생성할 때 참고할 가벼운 예시다.
