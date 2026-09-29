# PROJECT_STRUCTURE.md
# Document & Folder Reference

`VIBE_MASTER.md`가 프로젝트 유형에 맞게 필요한 것만 만든다.

권장 예시:

```text
ProjectRoot/
├─ VIBE_MASTER.md
├─ README.md
├─ AGENTS.md
├─ progress.md
├─ PROJECT_PLAN.md
├─ architecture.md
├─ DECISIONS.md
├─ TEST_MATRIX.md
├─ design.md                 # 필요 시
├─ SECURITY_CHECKLIST.md     # 필요 시
├─ PLATFORM_MATRIX.md        # 필요 시
├─ MAINTENANCE_PLAN.md       # Production + 지속관리 시
├─ BuildSystem/              # 선택: 상세 참고 문서
├─ ReleaseLog/
│  ├─ ReleaseWork/
│  └─ ReleaseResult/
└─ <source / assets / tests / platform folders>
```

실제 소스 폴더는 기술 스택에 맞춰 만든다.

예:
- Web: `src/`, `public/`, `tests/`
- Unity: `Assets/`, `Packages/`, `ProjectSettings/`
- Kotlin/Paper: `src/main/kotlin/`, `src/main/resources/`
- Python: package/source directory + `tests/`

## 문서 역할

- `progress.md`: 현재 상태/체크포인트만. 장기 일지 아님.
- `PROJECT_PLAN.md`: 현재 개발 Phase, Task, Scope, Exit Condition.
- `architecture.md`: 현재 실제 구조.
- `DECISIONS.md`: 왜 중요한 결정을 했는지.
- `TEST_MATRIX.md`: 반복 회귀 테스트 기준.
- `design.md`: 현재 확정된 비주얼/UX 규칙.
- `PLATFORM_MATRIX.md`: OS/빌드 타깃 차이.
- `MAINTENANCE_PLAN.md`: Production 이후 점검 항목.
- `ReleaseWork`: 미래 Release 계획.
- `ReleaseResult`: 실제 배포 결과.
