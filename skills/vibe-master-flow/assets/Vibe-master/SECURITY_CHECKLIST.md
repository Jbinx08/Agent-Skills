# SECURITY_CHECKLIST.md
# Production Security Checklist

이 문서는 Production 배포 전 반복적으로 확인할 보안 기준이다.

프로젝트 기술 스택에 따라 항목을 추가/삭제할 수 있다.

---

# 1. Secrets

- [ ] API Key/Secret이 소스 코드에 하드코딩되어 있지 않음
- [ ] `.env` 등 민감 파일이 공개 저장소에 포함되지 않음
- [ ] 클라이언트에 노출되면 안 되는 Secret이 브라우저 코드에 없음
- [ ] Production/Development 환경 변수가 구분됨
- [ ] 로그에 민감 정보가 출력되지 않음

---

# 2. Authentication

- [ ] 인증이 필요한 기능은 서버/Rules 수준에서도 보호됨
- [ ] 로그인 UI만 숨기는 방식으로 권한을 처리하지 않음
- [ ] 세션 만료/로그아웃이 정상 작동
- [ ] 비활성/삭제 사용자 처리 확인

---

# 3. Authorization

- [ ] 일반 사용자와 관리자 권한이 구분됨
- [ ] 다른 사용자의 데이터에 임의 접근할 수 없음
- [ ] ID/URL을 직접 바꿔 권한을 우회할 수 없음
- [ ] 서버/API/Rules가 최종 권한 검사를 수행함

---

# 4. Input Validation

- [ ] 필수 입력 검증
- [ ] 길이 제한
- [ ] 타입 검증
- [ ] 파일 형식 검증
- [ ] 파일 크기 제한
- [ ] 위험한 HTML/Script 입력 처리
- [ ] 예상하지 못한 값 처리

---

# 5. Database / Storage

- [ ] Firestore/D1/DB 권한 규칙 확인
- [ ] 공개되면 안 되는 데이터가 공개 Query로 노출되지 않음
- [ ] Storage/R2 업로드 권한 확인
- [ ] 삭제 권한 확인
- [ ] Migration 전 복구 방법 확인

---

# 6. API / Workers

- [ ] 인증 필요한 API 보호
- [ ] CORS 정책 확인
- [ ] Rate Limit 필요 여부 확인
- [ ] 오류 응답에 내부 정보가 과도하게 노출되지 않음
- [ ] 관리자 Endpoint 보호
- [ ] 외부 API 실패 시 안전한 처리

---

# 7. Frontend

- [ ] 민감 데이터가 Local Storage 등에 불필요하게 저장되지 않음
- [ ] 디버그 정보 제거
- [ ] Production Source에서 Secret 노출 없음
- [ ] 사용자 입력을 그대로 HTML에 삽입하지 않음

---

# 8. Deployment

- [ ] HTTPS
- [ ] Production 환경 변수 확인
- [ ] Preview와 Production 설정 혼동 없음
- [ ] Domain/Redirect 설정 확인
- [ ] 공개 디렉터리에 민감 파일 없음

---

# 9. Release Decision

모든 필수 항목 통과 후 Production 배포.

보안상 확인되지 않은 항목이 있으면 GO가 아니라 HOLD로 처리한다.
