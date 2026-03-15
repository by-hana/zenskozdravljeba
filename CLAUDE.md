# CLAUDE.md — Project Guidelines

## Project: ŽenskoZdravlje.ba

Django 6.0.3 CMS for a Bosnian women's health portal. Windows environment; always use `PYTHONUTF8=1` when running management commands.

---

## Git: Commit and Push Regularly

**After every meaningful change, commit and push to GitHub.** Never let progress pile up uncommitted.

Rules:
- Commit after each logical unit of work (feature, fix, content change, new file)
- Write clear, descriptive commit messages in English (e.g. `Add SVG illustrations for blog posts`, `Fix Cyrillic typo in seed file`)
- Always push after committing: `git push origin main`
- Never leave the working tree dirty at the end of a session
- If the project has no git remote yet, ask the user to set one up before the first push

---

## Language

- All user-facing content is in **Bosnian (Latin script only)**
- Zero Cyrillic characters anywhere — not in templates, seed files, views, or static files
- No language emphasis phrases like "na bosanskom jeziku" in meta/SEO content

---

## Fonts

- Headings: `'Merriweather', Georgia, serif`
- Body: `'Open Sans', -apple-system, sans-serif`
- No em dashes anywhere on the site

---

## Content

- Blog post author: always `ŽenskoZdravlje.ba Tim`
- Categories (11 total): Hormoni i menstrualni ciklus, PCOS i hormonski poremecaji, Ginekolosko zdravlje, Ishrana za zensko zdravlje, Vitamini suplementi i minerali, Mentalno zdravlje zena, Plodnost i trudnoca, Fitness i kretanje za zene, Prirodni pristupi zdravlju, Koza kosa i hormoni, Medicinski testovi i analize
- No stock photos — use local SVG illustrations in `static/images/`
- No fake statistics or unverified claims

---

## Running the dev server

```bash
cd "E:\CLAUDE CODE HUB\Website Generator Discord"
PYTHONUTF8=1 py manage.py runserver
```

## Seeding content

```bash
PYTHONUTF8=1 py manage.py seed_cms_content
```
