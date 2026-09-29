# BUILD_FLOW.md
# Initial Project Build Reference

`VIBE_MASTER.md`가 최상위 규칙이다. 이 문서는 New / Development 상태에서 최초 Production까지의 상세 참고 규칙이다.

## Phase 0 — Foundation

AI가 프로젝트에 맞는 `PROJECT_PLAN.md`를 만든다.

필수 결정:
- 프로젝트 목적과 사용자/플레이어
- 성공 조건
- Project Type
- Essential / Important / Minor
- 기술 스택/엔진/플랫폼
- 저장/데이터/인증이 필요한지
- 외부 서비스와 비용 위험
- Architecture와 폴더 구조
- 테스트 전략
- 사용자 검수가 필요한 영역
- Cross-Platform 요구

디자인이 중요한 프로젝트는 3~5개의 충분히 다른 방향을 탐색하고 하나를 Design Lock한다.

## Phase 1 — Core Build

Essential을 구현한다. 하나의 Phase 전체를 한 번에 밀지 말고 의미 있는 작업 단위마다:

`Plan → Build → Test → User Review(필요 시) → Fix → Re-Test → Validated`

필수 서비스/SDK/플랫폼 연결은 마지막 Phase까지 미루지 않는다.

## Phase 2 — Refinement & Integration

Important 기능, 예외 처리, UX/게임플레이, 통합, 성능, 접근성/조작성 등을 보완한다.

실제 사용감이 중요한 영역은 사용자 검수 루프를 반복한다.

## Phase 3 — Release Readiness

- 전체 회귀 테스트
- 최종 빌드
- 데이터/Save 호환성
- 플랫폼 호환성
- Security가 적용되는 프로젝트는 보안 검증
- Migration/Rollback
- 사용자 최종 검수
- Known Issues
- GO/HOLD

GO일 때만 최초 Production 버전을 확정한다. 일반적인 최초 정식 버전은 `v1.0.0`이다.

Phase 종료 시 Master의 기록 규칙에 따라 문서를 동기화한다.
