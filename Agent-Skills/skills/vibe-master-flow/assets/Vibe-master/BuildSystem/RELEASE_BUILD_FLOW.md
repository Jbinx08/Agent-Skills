# RELEASE_BUILD_FLOW.md
# Production Release Reference

`VIBE_MASTER.md`가 최상위 규칙이다. 이 문서는 Production 이후 변경을 위한 상세 참고 규칙이다.

## 분류

### Hotfix
명확한 Production 버그. 보통 PATCH.

### Small Improvement
구조를 바꾸지 않는 작은 개선. 보통 PATCH 또는 범위에 따라 MINOR.

### Feature Update
호환 가능한 의미 있는 기능 추가. 보통 MINOR. ReleaseWork 계획을 만든다.

### Major Update
호환성, 핵심 구조, 핵심 UX/게임 루프, 대규모 데이터 구조 등이 크게 바뀜. MAJOR 후보이며 사용자 승인 필수.

## ReleaseWork

`ReleaseLog/ReleaseWork/Rel_Buildflow-ver.X.Y.Z.md`

최소 포함:
- Goal
- Scope / Out of Scope
- 사용자 영향
- 변경 대상
- Data/Save Migration
- Dependency/External Service
- Compatibility
- Security/Permission 영향
- Risk
- Rollback
- Test Plan
- Release Phases
- Exit Conditions

## Release Loop

`Plan → Build → Test → User Review → Fix → Re-Test → Full Regression → GO/HOLD/ROLLBACK → Deploy → Smoke Test → Result Log`

주관적 검수가 필요 없는 작업은 User Review를 생략할 수 있다.

## Production Result

실제로 배포된 경우에만:

`ReleaseLog/ReleaseResult/Rel_Result-ver.X.Y.Z.log`

계획이 아니라 실제 사실을 기록한다.

- 배포 시각/환경
- 실제 변경
- Migration 결과
- Test/Smoke 결과
- Known Issues
- Rollback 정보

## 진행 중 큰 업데이트와 긴급 Hotfix

큰 Release가 진행 중인데 Production Hotfix가 필요하면 Hotfix를 별도 PATCH로 처리한다. 이후 그 수정 내용을 진행 중 Release에도 반영하고 다시 테스트한다.
