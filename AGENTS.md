# Portfolio maintenance

- This repository maintains an existing Netlify portfolio; do not create a replacement hosting project without being asked.
- Preserve the current design, existing project copy, and local photos unless a requested change requires otherwise.
- Edit profile copy in `content/site.json`, project copy in `content/projects.json`, and personal/project stories in `content/stories.json`.
- The confirmed Goodwill scope is **3년간 총 10억 원**, developed and overseen while serving as **인천 지부장**. Do not describe this as an annual 10억 원 project or 30억 원 total.
- The user provided a Goodwill Milal Incheon storefront photo in chat, but the binary file is not available locally yet. Use that exact photo when its source becomes available; do not substitute unrelated photos.
- Put photos in `assets/images/`. Use `image: ""` for the icon/metric fallback.
- Templates, CSS, and JavaScript live in `templates/` and `assets/`. `public/` is generated and ignored.
- Run `python3 scripts/build.py` after changes. Keep the project build dependency-free.
- Do not commit credentials, Netlify tokens, `.env` files, or `.netlify/` local state.
- Netlify uses `main`, build command `python3 scripts/build.py`, and publish directory `public`. Linking the existing Netlify project to this repository requires account access; do not claim it is linked without verifying.
