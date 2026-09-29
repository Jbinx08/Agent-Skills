# TEST_MATRIX.md
# Regression & Release Test Matrix

이 문서는 Release마다 반복해서 확인해야 할 핵심 테스트를 정의한다.

서비스 기능이 늘어나면 이 문서도 함께 확장한다.

---

# Test Status

권장 표기:

- `[ ]` Not Tested
- `[x]` Passed
- `[!]` Failed
- `[-]` Not Applicable

Release를 시작할 때 체크 상태는 새로 초기화해서 사용할 수 있다.

---

# 1. Authentication

- [ ] 회원가입 성공
- [ ] 잘못된 입력 차단
- [ ] 로그인 성공
- [ ] 잘못된 로그인 처리
- [ ] 로그아웃
- [ ] 새로고침 후 인증 상태
- [ ] 세션 만료 처리
- [ ] 비로그인 사용자의 보호 페이지 접근 차단
- [ ] 권한이 없는 사용자의 관리자 기능 접근 차단

---

# 2. Core User Flow

프로젝트별 핵심 Flow를 여기에 적는다.

예:

- [ ] 사용자가 핵심 콘텐츠를 생성할 수 있음
- [ ] 생성된 데이터가 정상 저장됨
- [ ] 저장된 데이터를 다시 조회할 수 있음
- [ ] 수정 가능
- [ ] 삭제 가능
- [ ] 잘못된 상태에서 안전하게 실패함

---

# 3. Navigation

- [ ] 주요 페이지 이동
- [ ] 뒤로가기/새로고침
- [ ] 직접 URL 접근
- [ ] 존재하지 않는 경로 처리
- [ ] 로그인 전/후 Navigation 차이

---

# 4. Data

- [ ] 기존 데이터 조회
- [ ] 신규 데이터 생성
- [ ] 수정
- [ ] 삭제
- [ ] 권한 없는 데이터 접근 차단
- [ ] 빈 데이터 상태
- [ ] 잘못된 데이터 처리

---

# 5. External Services

프로젝트에 사용하는 서비스만 유지한다.

- [ ] Firebase Auth
- [ ] Firestore
- [ ] Firebase Storage
- [ ] Cloudflare Pages
- [ ] Cloudflare Workers
- [ ] Cloudflare R2
- [ ] Cloudflare D1
- [ ] 외부 API

---

# 6. UI / UX

- [ ] Loading State
- [ ] Empty State
- [ ] Error State
- [ ] Success Feedback
- [ ] Form Validation
- [ ] Disabled State
- [ ] Mobile Layout
- [ ] Desktop Layout
- [ ] Keyboard Interaction
- [ ] 기본 Accessibility

---

# 7. Browser / Device

프로젝트에서 실제 지원하는 범위만 유지한다.

- [ ] Chromium 기반 브라우저
- [ ] Mobile Chromium
- [ ] 기타 필요한 브라우저

---

# 8. Release-Specific Tests

각 Release의 `Rel_Buildflow-ver.X.Y.Z.md`에서 이번 버전 전용 테스트를 추가한다.

이 문서는 프로젝트 전체의 **고정 회귀 테스트**만 담당한다.
