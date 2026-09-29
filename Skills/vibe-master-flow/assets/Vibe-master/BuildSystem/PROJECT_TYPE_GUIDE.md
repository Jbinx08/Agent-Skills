# PROJECT_TYPE_GUIDE.md
# Project-Specific Adaptation Reference

Master Lifecycle은 동일하지만 프로젝트 유형에 따라 계획/테스트/문서 초점이 달라진다.

## Web
- Routing / State / Responsive
- API / Auth / DB / Storage
- Browser support
- Security / CORS / Permission
- Deployment / Domain

## Unity Game
- Scene flow
- Prefabs / ScriptableObjects
- Input System / Physics
- Game Loop / State
- Save Data + version migration
- Animator / Audio / Addressables
- Packages
- Build Targets
- Performance
- 조작감/재미/밸런스 사용자 검수

## Desktop
- Filesystem / OS integration
- Installer / updater
- permissions
- native dependencies
- signing

## Mobile
- Android / iOS
- lifecycle
- permission
- store / signing
- device variability
- data migration

## Backend/API
- API contract
- auth/authorization
- DB migration
- logging
- rate limit
- observability
- rollback

## Plugin/Mod
- host/version compatibility
- lifecycle/load-unload
- config migration
- dependency/API compatibility

프로젝트에 없는 영역은 생성하지 않는다.
