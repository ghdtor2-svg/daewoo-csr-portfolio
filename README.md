# 이대우 사회공헌 포트폴리오

기존 Netlify 포트폴리오의 디자인과 사진을 유지하고, 굿윌스토어 건립지원 사업을 추가한 관리용 원본입니다.

- 굿윌스토어: **인천 지부장 재임 당시 직접 개발·총괄, 3년간 총 10억 원 규모**
- 굿윌스토어 사진은 사용자가 지정한 밀알인천점 전경입니다. 원본과 워터마크를 보존하고 기사 출처를 표시합니다.
- 이 저장소 업로드만으로 기존 Netlify 사이트가 바뀌지는 않습니다. 아래 절차로 기존 프로젝트에 GitHub를 연결하면 이후 변경 사항이 자동으로 배포됩니다.

## GitHub 화면에서 내용 수정하기

1. 수정할 파일을 열고 연필 모양 **Edit this file**을 누릅니다.
2. 따옴표 안의 문구만 수정합니다. 쉼표, 대괄호, 중괄호는 유지합니다.
3. **Commit changes**로 저장합니다. `main` 브랜치에 저장하면 Netlify 연결 이후에는 자동 배포됩니다.
4. 큰 수정은 새 브랜치와 Pull request로 검토한 뒤 반영할 수 있습니다.

| 수정할 내용 | 파일 |
| --- | --- |
| 이름, 연락처, 기본 소개, 사업 섹션 설명 | [content/site.json](content/site.json) |
| 사업명, 역할, 성과, 규모, 상세 설명, 사진 경로, 영상 | [content/projects.json](content/projects.json) |
| 사진 추가 및 교체 | [assets/images/](assets/images/) |
| 자기소개서와 사업 추진 스토리 | [content/stories.json](content/stories.json) |
| 역량 수치, 가족 소개, 전체 배치 | [templates/index.html](templates/index.html) |
| 색상 외 추가 스타일 | [assets/css/site.css](assets/css/site.css) |
| 사진 확대 동작 | [assets/js/main.js](assets/js/main.js) |

`public/`은 빌드할 때 자동 생성됩니다. 이 폴더의 파일을 직접 고치지 마세요.

## 굿윌스토어 사진 교체하기

1. GitHub에서 `assets/images` 폴더를 열고 **Add file → Upload files**로 사진을 추가합니다. 예: `goodwill-store.jpg`.
2. `content/projects.json`에서 `"id": "goodwill-store"`인 항목을 찾습니다.
3. 다음 두 항목을 수정합니다.

```json
"image": "assets/images/goodwill-store.jpg",
"imageAlt": "굿윌스토어 건립지원 사업 현장"
```

현재 사진은 `assets/images/goodwill-incheon.jpg`이며, `imageCredit`에 출처가 기록되어 있습니다. `imageFit: "contain"`은 세로 사진 전체를 표시하고, `"cover"`는 일반 카드처럼 영역을 채웁니다. 사진을 교체하면 출처 정보도 함께 바꿔 주세요.

`image`가 빈 문자열이면 아이콘과 `metric` 문구가 표시됩니다. 사진을 지정하면 해당 영역에 사진이 나타납니다. `fields`의 사업 규모는 사진을 넣어도 계속 표시됩니다. 업로드한 파일 이름과 경로가 정확히 일치해야 하며, JPG·PNG·WebP 등을 사용할 수 있습니다.

## 사업 추가 또는 순서 변경

`content/projects.json`은 사업 목록입니다. 목록 안의 사업 객체 하나를 복사하고 다음을 바꿉니다.

- `id`: 다른 사업과 겹치지 않는 영문 소문자·숫자·하이픈 이름
- `title`, `category`, `description`: 화면에 표시할 제목, 분류, 상세 설명
- `image`, `imageAlt`: 사진 경로와 설명. 사진이 없으면 `image`는 `""`로 두고 `metric`에 대표 문구 입력
- `fields`: 배경·역할·목표·성과 등을 표시하는 항목. `highlight: true`이면 강조 표시
- `video`: 선택 사항. YouTube 영상의 11자리 `id`와 표시할 `title`. 영상이 없으면 이 객체를 삭제

객체의 순서를 바꾸면 화면의 순서도 바뀝니다. 사업 번호와 ‘핵심 N대 사업’ 문구는 자동 계산됩니다. 소개 문구인 `projectsDescription`은 `content/site.json`에서 별도로 수정합니다.

## 스토리 추가 및 수정

`content/stories.json`에서 `title`과 `description`을 수정합니다. `icon`은 Lucide 아이콘 이름이고, `featured: true`는 넓은 카드로 강조합니다. 굿윌스토어 협업 사례는 담당자의 우려 파악과 현장 라운딩을 통한 신뢰 회복을 중심으로 정리했습니다.

## 기존 Netlify 프로젝트에 GitHub 연결

기존 주소를 유지하려면 **새 프로젝트를 만들지 말고 기존 프로젝트에 연결**하세요.

1. 기존 프로젝트 열기: https://app.netlify.com/projects/resonant-jelly-51ba9b/overview
2. **Project configuration → Build & deploy → Continuous deployment → Repository**로 이동합니다. UI 버전에 따라 **Link repository** 또는 **Link to a Git repository**로 표시됩니다.
3. GitHub를 선택하고 이 저장소에 접근을 허용한 뒤 `daewoo-csr-portfolio`를 선택합니다. Netlify GitHub 앱에 해당 저장소 권한을 부여해야 합니다.
4. 배포 브랜치: `main`, Base directory: 비워 둠, Build command: `python3 scripts/build.py`, Publish directory: `public`.
5. 저장하고 첫 배포를 실행합니다. `netlify.toml`에도 같은 설정이 있습니다.
6. Deploys에서 성공 상태를 확인하고 기존 공개 사이트에서 4개 사업과 굿윌스토어 문구를 확인합니다.

그다음부터는 GitHub의 `main` 변경을 Netlify가 자동 배포합니다. GitHub Actions의 초록색 빌드 상태는 소스 검증 성공이며, Netlify 배포 성공 여부는 별도로 Deploys에서 확인합니다.

## 로컬 확인 및 수동 배포

Python 3.12가 권장됩니다. 추가 패키지는 필요 없습니다.

```bash
python3 scripts/build.py
python3 -m http.server 8001 --directory public
```

브라우저에서 http://localhost:8001 을 엽니다. JSON 형식, 중복 사업 ID, 없는 이미지, 잘못된 영상 ID는 빌드에서 오류로 알려줍니다. GitHub의 Actions에서도 같은 빌드를 실행합니다.

수동 Netlify 배포는 빌드한 **`public` 폴더**를 기존 프로젝트의 Deploys 화면에 업로드합니다. GitHub의 소스 ZIP은 빌드 전 원본이므로 그대로 업로드하면 안 됩니다.

## 되돌리기

GitHub의 이전 커밋 내용을 새 커밋으로 되돌리거나, Netlify Deploys에서 이전 성공 배포를 다시 게시할 수 있습니다.

## 구성 안내

브라우저는 기존과 같이 Tailwind CDN, Lucide 아이콘, Pretendard 글꼴을 사용합니다. 영상은 YouTube 임베드입니다. 외부 연결이 있어야 해당 자원이 표시됩니다. 내용은 빌드 단계에 HTML에 포함되어 검색·접근성에 활용할 수 있으며, JavaScript가 없어도 사업 문구를 읽을 수 있습니다.
