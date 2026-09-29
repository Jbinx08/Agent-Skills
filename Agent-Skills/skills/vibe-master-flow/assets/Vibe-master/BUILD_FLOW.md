# BUILD_FLOW.md
# Initial Product Build Flow

이 문서는 **새 서비스를 처음 만들고 최초 Production Release까지 도달하는 과정**을 정의한다.

최초 배포 이후의 업데이트는 `RELEASE_BUILD_FLOW.md`를 따른다.

---

# Phase 0 — Foundation

목표:

> 코드를 본격적으로 작성하기 전에 서비스의 목적, 구조, 기능 우선순위, 디자인, 테스트 기준을 고정한다.

Phase 0에서 잘못된 결정을 하면 이후 모든 작업이 반복되므로 구현을 서두르지 않는다.

## Phase 0-A — Product Definition

다음을 확정한다.

- 서비스 이름과 목적
- 핵심 사용자
- 해결하려는 문제
- 핵심 사용자 흐름
- 기술 스택
- 배포 환경
- 외부 서비스
- 데이터 저장 방식
- 인증 방식
- 파일/폴더 구조

이 단계에서 생성 또는 초기화:

- `README.md`
- `AGENTS.md`
- `architecture.md`
- `progress.md`
- `DECISIONS.md`
- `TEST_MATRIX.md`
- `SECURITY_CHECKLIST.md`

`design.md`는 디자인 확정 후 작성한다.

---

## Phase 0-B — Feature Priority

모든 기능은 구현 전에 아래 세 범주 중 하나로 분류한다.

### Essential

없으면 서비스가 정상 작동하지 않거나 해당 서비스라고 할 수 없는 기능.

예:

- 회원가입/로그인
- 핵심 데이터 생성/조회
- 핵심 콘텐츠 저장
- 핵심 사용자 Flow
- 반드시 필요한 서비스 연결

**Phase 1에서 구현한다.**

### Important

없어도 작동은 하지만 실제 사용성이 크게 떨어지는 기능.

예:

- 검색
- 알림
- 필터
- 설정
- 로딩/빈 화면/오류 상태
- 주요 UX 개선

**Phase 2에서 구현한다.**

### Minor

없어도 서비스 사용에는 문제가 없지만 편의성과 완성도를 높이는 기능.

예:

- 추가 애니메이션
- 키보드 단축키
- 테마
- 세부 옵션
- 부가 편의 기능

**최초 배포 이후 필요에 따라 추가한다.**

중요:

> 기능의 중요도와 Semantic Version의 `MAJOR/MINOR/PATCH`는 서로 다른 개념이다.

---

## Phase 0-C — Design Exploration

3~5개의 디자인 Prototype을 만든다.

각 시안은 단순히 색만 다른 버전이 아니라 다음이 충분히 달라야 한다.

- 레이아웃
- 정보 밀도
- Navigation 방식
- Component 스타일
- Typography
- 공간감
- 전체 분위기

Prototype 단계에서는 실제 핵심 로직을 깊게 구현하지 않는다.

목적은 **디자인 방향 결정**이다.

---

## Phase 0-D — Design Lock

하나의 디자인을 선택한다.

선택한 디자인을 기준으로 `design.md`를 작성한다.

최소 포함:

- Design Direction
- Colors
- Typography
- Spacing
- Border Radius
- Buttons
- Inputs
- Cards
- Navigation
- Modals
- Icons
- Responsive Rules
- Motion / Animation
- Hover / Active / Disabled
- Accessibility 관련 기본 규칙

이후 UI는 특별한 이유가 없는 한 `design.md`를 따른다.

---

## Phase 0-E — Build Baseline

실제 구현 전에 마지막으로 확인한다.

- 폴더 구조가 확정되었는가
- Essential / Important / Minor가 분류되었는가
- 외부 서비스 연결 방식이 결정되었는가
- `architecture.md`가 현재 계획과 일치하는가
- `AGENTS.md`에 작업/테스트/문서 갱신 규칙이 있는가
- `TEST_MATRIX.md`에 최소 핵심 사용자 Flow가 정의되었는가
- 민감 정보가 코드에 직접 들어가지 않도록 규칙이 있는가

완료 후 Phase 1로 이동한다.

---

# Phase 1 — Core Build

목표:

> Essential 기능을 실제 서비스 환경과 연결해 “서비스가 작동하는 상태”를 만든다.

## 1-A — Page Implementation

선택된 Prototype과 `design.md`를 바탕으로 실제 페이지를 만든다.

예:

- signup
- signin
- main
- profile
- settings
- dashboard
- 서비스별 핵심 페이지

디자인 껍데기를 단순 복사하지 말고 실제 데이터와 상태를 고려해 구현한다.

## 1-B — Essential Features

Essential 기능을 우선 구현한다.

## 1-C — Required Service Integration

필수 외부 서비스는 Phase 3까지 미루지 않는다.

예:

- Firebase Authentication
- Firestore
- Firebase Storage
- Cloudflare Pages
- Cloudflare Workers
- Cloudflare R2
- Cloudflare D1
- 외부 API

서비스 연결은 핵심 기능 구현 중 함께 검증한다.

## 1-D — Core Validation

확인:

- 핵심 페이지
- Essential 기능
- 인증
- 데이터 생성/조회/수정/삭제
- 주요 사용자 Flow
- 기본 오류 처리
- 외부 서비스 연결

완료 후 `progress.md`를 최신 상태로 다시 작성한다.

---

# Phase 2 — Refinement

목표:

> “작동하는 서비스”를 “실제로 사용할 만한 서비스”로 만든다.

## 2-A — Feedback

실제 사용 흐름을 따라가며 확인한다.

- 불필요한 클릭
- 이해하기 어려운 UI
- 부족한 안내
- 모바일 불편
- 느린 부분
- 잘못된 상태 표시
- 오류/빈 화면 처리 부족
- 접근성 문제

## 2-B — Important Features

Important 기능을 구현한다.

## 2-C — UX Refinement

필요에 따라:

- Loading
- Empty State
- Error State
- Confirmation
- Toast / Notification
- Form Validation
- Responsive UI
- Mobile UX
- Navigation
- Accessibility
- Animation
- Performance

## 2-D — Regression Test

새 기능 때문에 Essential 기능이 깨지지 않았는지 `TEST_MATRIX.md` 기준으로 다시 확인한다.

완료 후 `progress.md` 최신화.

---

# Phase 3 — Production Readiness

목표:

> 새로운 대형 기능을 더 넣는 단계가 아니라, 현재 구현된 버전을 안전하게 Production으로 내보낼 수 있는지 확인한다.

## 3-A — Functional Review

전체 핵심 Flow를 처음부터 끝까지 테스트한다.

## 3-B — Security Review

`SECURITY_CHECKLIST.md`를 기준으로 검사한다.

## 3-C — Code Review

확인:

- Syntax / Type Error
- Dead Code
- Duplicate Code
- Debug Code
- console.log
- TODO / FIXME
- 하드코딩된 Secret
- 임시 테스트 코드
- 불필요한 Dependency
- 잘못된 예외 처리

## 3-D — Production Preview

가능하면 Production과 동일하거나 유사한 Preview/Staging 환경에서 확인한다.

- 실제 Domain/Preview Domain
- HTTPS
- 환경 변수
- Firebase Production 설정
- Cloudflare Production 설정
- 주요 브라우저
- Desktop / Mobile

## 3-E — Release Decision

다음 중 하나를 결정한다.

- GO — 배포 가능
- HOLD — 수정 후 재검증
- ROLLBACK — 현재 변경 폐기 또는 이전 상태 복구

GO일 때 최초 Production Release를 진행한다.

---

# First Release

최초 배포는 보통 `v1.0.0`으로 시작한다.

배포가 완료되면:

1. 실제 배포 결과 확인
2. `ReleaseLog/ReleaseResult/Rel_Result-ver.1.0.0.log` 생성
3. `README.md` 최종 상태 반영
4. `architecture.md` 최종 상태 반영
5. `design.md` 최종 상태 반영
6. `TEST_MATRIX.md` 최종 기준 반영
7. `progress.md`를 Production 상태로 초기화

이후부터 모든 업데이트는 `RELEASE_BUILD_FLOW.md`를 따른다.

---

# Session Rule

작업 하나가 끝날 때마다 무조건 세션을 바꿀 필요는 없다.

그러나 다음 중 하나가 발생하면 새 세션을 권장한다.

- 의미 있는 기능 단위 완료
- Phase 전환
- 외부 서비스 연결 완료
- DB 구조 변경 완료
- 대규모 버그 조사 종료
- 현재 대화가 너무 길어져 과거 내용이 방해됨

새 세션 시작 시 프로젝트 파일을 먼저 읽는다.

---

# Core Principle

Phase 0
= 무엇을 만들지 정한다.

Phase 1
= 서비스가 작동하게 만든다.

Phase 2
= 서비스가 쓸 만하게 만든다.

Phase 3
= 안전하게 배포할 수 있게 만든다.

Release 이후
= `RELEASE_BUILD_FLOW.md`를 따른다.
