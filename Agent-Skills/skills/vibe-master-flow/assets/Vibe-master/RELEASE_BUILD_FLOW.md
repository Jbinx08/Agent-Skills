# RELEASE_BUILD_FLOW.md
# Post-Release Development Flow

이 문서는 최초 Production Release 이후 서비스의 버그 수정, 기능 추가, 구조 변경, 대형 업데이트를 어떻게 계획하고 구현할지 정의한다.

핵심 원칙:

> 작은 수정은 빠르게 처리하되, 의미 있는 기능과 대형 업데이트는 기존 Production을 보호하면서 별도의 Release Plan으로 진행한다.

---

# 1. Update Classification

업데이트를 시작하기 전에 먼저 규모를 분류한다.

## Hotfix

작고 명확한 버그 수정.

예:

- 버튼 동작 오류
- 잘못된 링크
- CSS 깨짐
- 단순 JavaScript 오류
- 텍스트/표시 오류

기본 흐름:

문제 재현
→ 원인 확인
→ 수정
→ 영향 범위 테스트
→ 배포
→ ReleaseResult 기록

Hotfix는 보통 PATCH 버전을 올린다.

예:

`v1.1.0 → v1.1.1`

---

## Small Improvement

서비스 구조를 바꾸지 않는 작은 편의 기능.

예:

- 버튼 추가
- 작은 설정
- 정렬 옵션
- 작은 UI 개선
- 키보드 단축키

별도의 Release Phase가 필요하지 않을 수 있다.

하지만 Production에 배포했다면 반드시 ReleaseResult를 남긴다.

---

## Feature Update

하나의 의미 있는 기능 추가.

예:

- 검색
- 알림
- 프로필 시스템
- 파일 업로드
- 관리자 화면
- 친구 기능
- 새로운 핵심 페이지

이 단계부터는 `ReleaseWork/Rel_Buildflow-ver.X.Y.Z.md` 작성을 권장한다.

---

## Major Update

서비스 구조, 핵심 Flow, 데이터 구조, 인증, 디자인 시스템 또는 핵심 기능이 크게 바뀌는 업데이트.

예:

- 전체 UI 리뉴얼
- 인증 시스템 변경
- DB 구조 대규모 변경
- Firebase에서 다른 Backend로 이전
- 핵심 서비스 영역 추가
- 실시간 시스템 추가
- 전체 Navigation 재설계
- Breaking Change 포함

Major Update는 **하나의 작은 신규 프로젝트처럼** Release Phase를 사용한다.

---

# 2. Version Reservation

의미 있는 Feature Update 또는 Major Update를 시작할 때 **예비 버전**을 정한다.

예:

`v1.1.0`

계획 파일:

`ReleaseLog/ReleaseWork/Rel_Buildflow-ver.1.1.0.md`

중요:

- 이 버전은 계획 단계의 예비 버전이다.
- 구현 중 범위가 달라지면 버전을 변경할 수 있다.
- 버전 변경 시 파일명과 문서 내부 버전을 함께 변경한다.
- 아직 Production에 배포되지 않은 버전은 `ReleaseResult`에 기록하지 않는다.
- 이미 사용된 Production 버전 번호는 재사용하지 않는다.

---

# 3. Release Planning Meeting

대형 기능을 바로 구현하지 않는다.

먼저 AI와 기획 회의를 진행한다.

회의 시작 시 AI는 다음을 읽는다.

- `README.md`
- `AGENTS.md`
- `architecture.md`
- `design.md`
- `progress.md`
- `DECISIONS.md`
- `TEST_MATRIX.md`
- `RELEASE_BUILD_FLOW.md`
- 최근 관련 `ReleaseResult`
- 이번 `Rel_Buildflow-ver.X.Y.Z.md`

기획 회의에서는 최소한 아래를 결정한다.

## Goal

- 무엇을 추가/변경하는가
- 왜 필요한가
- 사용자에게 무엇이 달라지는가

## Scope

이번 릴리스에 포함할 것과 제외할 것을 명확히 한다.

## Feature Priority

- Essential
- Important
- Minor

## Impact Analysis

### Frontend
- 페이지
- Navigation
- Component
- Design System
- Responsive UI

### Backend
- API
- Worker
- Server Logic

### Database
- Schema
- Collection/Table
- Existing Data
- Index
- Migration

### Authentication / Authorization
- Login
- Session
- Role
- Permission

### External Services
- Firebase
- Cloudflare
- R2
- D1
- Workers
- 외부 API

## Compatibility

- 기존 계정
- 기존 데이터
- 기존 URL
- 기존 설정
- 기존 API
- 기존 사용자 Flow

## Risks

- 데이터 손실
- 인증 장애
- 배포 실패
- 기존 기능 깨짐
- 비용 증가
- Rate Limit
- 서비스 의존성

## Rollback

문제가 생겼을 때 어디까지 되돌릴 수 있는지 미리 정한다.

---

# 4. Release Phase Structure

Feature Update / Major Update는 필요에 따라 아래 Phase를 사용한다.

---

## Release Phase 0 — Planning

- 현재 Production 구조 분석
- Goal / Scope 확정
- Essential / Important / Minor 분류
- 영향 분석
- 데이터/서비스 변경 결정
- Migration 계획
- Test Plan
- Rollback Plan
- 예비 버전 확정

완료 조건:

> 구현 전에 무엇을 어떻게 바꿀지 문서만 보고 설명할 수 있어야 한다.

---

## Release Phase 1 — Isolated Core Build

업데이트의 핵심 기능을 가능한 한 기존 Production 코드와 분리해 구현한다.

원칙:

- 기존 기능을 임의 삭제하지 않는다.
- 기존 API 변경 전 사용처를 확인한다.
- DB 변경 전 기존 데이터 호환성을 확인한다.
- Auth 변경 시 기존 Session과 계정을 고려한다.
- 구조 변경은 `architecture.md` 또는 계획 문서에 반영한다.

가능하면 독립된 Component / Module / Route / Service로 먼저 구현한다.

---

## Release Phase 2 — Integration

새 기능을 기존 시스템과 연결한다.

예:

- Navigation
- Authentication
- Firestore
- R2
- Worker
- 기존 사용자 데이터
- 기존 API

Integration 후 즉시 관련 기존 기능을 다시 테스트한다.

---

## Release Phase 3 — Refinement

실사용 피드백을 바탕으로 완성도를 높인다.

- Important 기능
- Loading
- Error State
- Empty State
- Responsive
- Accessibility
- Validation
- Performance
- Animation
- UX 개선

---

## Release Phase 4 — Production Validation

새 기능뿐 아니라 기존 서비스 전체를 검증한다.

### New Feature Test
이번 업데이트 기능 전부.

### Regression Test
`TEST_MATRIX.md` 전체 핵심 항목.

### Data Validation
Migration이 있었다면 기존/신규 데이터 모두 확인.

### Security Review
`SECURITY_CHECKLIST.md` 기준.

### Code Review
임시 코드, Secret, Dead Code, Debug 코드 등 확인.

### Preview/Staging
가능하면 Production과 유사한 환경에서 최종 테스트.

완료 후 GO/HOLD/ROLLBACK을 결정한다.

---

# 5. Production Protection Rules

대형 업데이트는 현재 Production을 보호해야 한다.

권장:

- Git 사용 시 별도 feature/release branch에서 작업
- Production 기준 commit/tag 보존
- DB Migration 전 백업 또는 복구 방법 확보
- 기존 환경 변수 목록 확인
- 배포 전 현재 Production version 기록
- Preview/Staging에서 선검증

## 대형 업데이트 중 Hotfix 발생

현재 Production에 긴급 Hotfix가 필요하면:

1. Production 기준으로 Hotfix를 별도 처리
2. Hotfix 배포
3. PATCH 버전 ReleaseResult 기록
4. 진행 중인 대형 업데이트 브랜치/코드에도 해당 수정 반영
5. 충돌 여부 재테스트

대형 업데이트 때문에 Production Hotfix를 미루지 않는다.

---

# 6. Versioning Rules

Semantic Versioning을 기본으로 사용한다.

`MAJOR.MINOR.PATCH`

## PATCH

기존 동작을 유지하는 버그 수정.

예:

`1.2.0 → 1.2.1`

## MINOR

기존 사용자와 호환되는 새로운 기능 추가.

예:

`1.2.1 → 1.3.0`

## MAJOR

Breaking Change 또는 대규모 구조/동작 변경.

예:

`1.8.4 → 2.0.0`

주의:

> 우리가 기능을 `Essential / Important / Minor`로 분류하는 것과 Semantic Version의 `MINOR`는 다른 개념이다.

---

# 7. ReleaseResult

Production 배포가 실제로 완료된 경우에만:

`ReleaseLog/ReleaseResult/Rel_Result-ver.X.Y.Z.log`

를 생성한다.

계획과 실제 구현 결과가 다르면 **실제 결과를 기준으로 기록**한다.

최소 기록:

- Release Version
- Release Date
- Update Type
- Summary
- Added
- Changed
- Fixed
- Removed
- Architecture
- Database / Migration
- Services
- Security
- Breaking Changes
- Known Issues
- Rollback Reference
- Validation Result

ReleaseResult는 과거 사실 기록이므로 원칙적으로 삭제하지 않는다.

---

# 8. ReleaseWork

`ReleaseLog/ReleaseWork/Rel_Buildflow-ver.X.Y.Z.md`

는 계획과 구현 과정의 기준 문서다.

Production 배포 후에도 보존한다.

이유:

- 무엇을 계획했는지 확인
- 실제 결과와 비교
- 다음 대형 업데이트 설계 시 참고
- 왜 특정 범위를 제외했는지 추적

계획 파일을 ReleaseResult로 옮기지 않는다.

두 기록은 역할이 다르다.

---

# 9. Documentation Sync

Release 완료 후 다음 문서를 실제 Production 상태와 동기화한다.

## README.md
사용자/개발자에게 보이는 기능, 실행, 환경이 바뀐 경우.

## architecture.md
구조, DB, API, 서비스 연결이 바뀐 경우.

## design.md
디자인 시스템이 바뀐 경우.

## AGENTS.md
Agent 작업 규칙이 바뀐 경우.

## DECISIONS.md
중요한 기술/구조 결정이 있었다면 이유를 남긴다.

## TEST_MATRIX.md
새 핵심 기능이 생겼다면 회귀 테스트 항목을 추가한다.

## progress.md
현재 Production 상태만 남기도록 다시 작성한다.

---

# 10. progress.md Reset Rule

`progress.md`는 영구 작업 로그가 아니다.

Release 완료 후 오래된 작업 기록을 지우고 현재 상태만 유지한다.

예:

```md
# Current Status

Current Version: v1.3.0
Current Phase: Production
Current Task: None

## Completed
- v1.3.0 Production Release

## In Progress
- None

## Known Issues
- None

## Next
- Bug fixes
- Small improvements
- Next release planning
```

과거 이력은 `ReleaseLog/`와 `DECISIONS.md`가 보존한다.

---

# 11. Session Strategy

## Hotfix / Small Improvement

작은 작업 여러 개는 같은 세션에서 처리 가능.

## Feature Update

기획과 구현을 분리하는 것을 권장.

## Major Update

Release Phase가 바뀔 때 새 세션을 권장.

예:

- Session 1 — Release Phase 0
- Session 2 — Release Phase 1
- Session 3 — Release Phase 2
- Session 4 — Release Phase 3
- Session 5 — Release Phase 4

각 세션 종료 전 `progress.md`를 최신화한다.

---

# 12. Release Completion

배포 완료 조건:

- Production 배포 성공
- 핵심 기능 확인
- 회귀 테스트 통과
- 보안 검사 완료
- 데이터 검증 완료
- `Rel_Result-ver.X.Y.Z.log` 생성
- 관련 문서 최신화
- `progress.md` Production 상태로 Reset

이 조건이 끝나기 전에는 해당 Release를 “완료”로 간주하지 않는다.
