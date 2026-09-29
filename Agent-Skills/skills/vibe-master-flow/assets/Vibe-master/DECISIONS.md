# DECISIONS.md
# Architecture & Product Decision Log

이 문서는 프로젝트의 중요한 결정과 그 이유를 보존한다.

`architecture.md`는 “현재 구조”를 설명하고,
`DECISIONS.md`는 “왜 그 구조를 선택했는지”를 설명한다.

이 파일은 Release 후에도 Reset하지 않는다.

---

# Entry Format

## DEC-0001 — Decision Title

- Date:
- Status: Proposed / Accepted / Superseded / Rejected
- Related Version:
- Related Release Plan:

### Context

어떤 문제 또는 선택지가 있었는지.

### Decision

무엇을 선택했는지.

### Reason

왜 이 선택을 했는지.

### Alternatives

검토했지만 선택하지 않은 대안.

### Consequences

좋아지는 점, 나빠지는 점, 이후 주의할 점.

### Supersedes

대체하는 기존 결정이 있다면 기록.

---

# Example

## DEC-0001 — Use Cloudflare R2 for User Uploads

- Date: YYYY-MM-DD
- Status: Accepted
- Related Version: v1.2.0
- Related Release Plan: `ReleaseLog/ReleaseWork/Rel_Buildflow-ver.1.2.0.md`

### Context

사용자 업로드 파일을 저장할 Storage가 필요하다.

### Decision

Cloudflare R2를 사용한다.

### Reason

현재 배포 구조와 결합하기 쉽고 파일 저장 역할을 명확히 분리할 수 있다.

### Alternatives

- Firebase Storage
- 별도 Object Storage

### Consequences

- R2 관련 환경 변수와 권한 관리가 추가된다.
- 업로드/다운로드 흐름을 별도로 관리해야 한다.
