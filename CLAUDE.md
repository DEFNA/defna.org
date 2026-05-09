# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Django 5.2 web application for the Django Events Foundation North America (DEFNA). Content management site for events, blog posts, board members, grants, and sponsorships. Uses Python 3.13, PostgreSQL, and Tailwind CSS 4.x (via tailwind-cli, not npm).

## Common Commands

All commands use the `justfile` task runner and Docker Compose:

```bash
just bootstrap          # One-time project setup
just up                 # Start all services (foreground)
just start              # Start services (detached)
just down               # Stop services
just test               # Run pytest
just test <path>        # Run specific test
just lint               # Run pre-commit on all files
just migrate            # Apply database migrations
just makemigrations     # Create new migrations
just manage <cmd>       # Run Django management commands
just console            # Open bash in utility container
just pg_dump [file]     # Backup database
just pg_restore [file]  # Restore database
```

## Architecture

- **config/** - Django project config (settings, URLs, WSGI)
- **website/** - Single Django app with all models, views, admin, forms, templatetags
- **templates/** - Django templates extending `base.html`; partials in `templates/partials/`
- **frontend/** - Source CSS and favicons; Tailwind compiles to `static/`

### Models (`website/models.py`)

Announcement, BlogPost, BoardMember, DjangoConEdition, SponsoredEvent, GrantCycle

### Views (`website/views.py`)

Class-based views (TemplateView pattern) with custom `get_context_data()` for context injection.

### Docker Services (`compose.yml`)

- **db**: PostgreSQL (pgautoupgrade:17-alpine)
- **web**: Django dev server (port 8000)
- **worker**: Django-Q2 async task worker
- **tailwind**: Tailwind CSS watcher
- **utility**: One-off management commands

## Testing

- Framework: pytest-django with `model-bakery` for fixtures and `django-test-plus` for assertions
- Config in `pyproject.toml`: runs with `--nomigrations --reuse-db`
- Tests live in `website/tests.py` and `config/tests/`

## Linting & Formatting

Pre-commit hooks handle all formatting:
- **Ruff**: Python linting + formatting (120-char lines, Python 3.13 target)
- **django-upgrade**: Django 5.0+ patterns
- **djade**: Django template linting
- **djhtml**: Django template formatting
- **rustywind**: Tailwind CSS class ordering

## Configuration

- Environment variables via `environs[django]` — see `.env-dist` for defaults
- Database URL: `DATABASE_URL` env var (PostgreSQL)
- Static files served by Whitenoise
- Blog posts use `django-markdownx` for Markdown editing
- Version scheme: `YYYY.MM.INC1` (calendar versioning via bumpver)

## CI/CD

GitHub Actions (`.github/workflows/actions.yml`): runs tests on PR/push, then auto-bumps version on main and force-pushes to `production` branch for deployment.
