# SECURITY_CHECKLIST.md

프로젝트에 실제 적용되는 항목만 유지한다.

## Secrets
- [ ] Secret이 코드/공개 파일에 없음

## Authentication / Authorization
- [ ] 필요한 권한 검증이 실제 Backend/Rules 수준에서 적용됨

## Input / Data
- [ ] 외부 입력 검증
- [ ] 민감 데이터 노출 방지

## Network / API
- [ ] 필요한 인증, CORS, Rate Limit, 오류 노출 정책 확인

## Storage / Database
- [ ] 읽기/쓰기/삭제 권한 확인
- [ ] Migration 및 복구 방법 확인

## Release
- [ ] Production 환경 변수/권한/공개 범위 확인
