# Technical Stack & Guidelines

## Core Technologies
- **Language**: Python 3.11+
- **Backend Framework**: Django 5.2 (MVT Pattern)
- **Database**: SQLite 3 (Development/Production)
- **Frontend Framework**: Bootstrap 5.3 (CSS/JS)
- **Templating Engine**: Django Templates
- **Content Management**: CKEditor 5 + Custom Markdown Filters
- **Interactive Visuals**: Particles.js, Mermaid.js
- **Deployment**: PythonAnywhere (Linux/WSGI)

## Directory Structure
- `/portfolio`: Main application logic (Models, Views, Templates).
- `/projects`: Likely another app or project-specific logic (need to verify).
- `/templates`: Global base templates.
- `/specs`: Documentation, requirements, and skill definitions.
- `/media`: User-uploaded content (Project images).
- `/portfolio/static`: App-specific CSS/JS/Images.

## Development Protocols
1. **Spec-Driven**: Every new feature must have a corresponding spec in `specs/features/`.
2. **Style Consistency**: Use semantic tokens derived from `specs/ui_ux.md`.
3. **Frontend Performance**: Prioritize Vanilla JS and CSS over heavy libraries.
4. **Localization**: Maintain EN/ES toggle logic in the frontend.
5. **Quality Assurance**: All logic must be validated with Django `tests.py` and UI verified with Playwright.

## Styling Rules
- **No Inline Styles**: Use classes and semantic CSS.
- **Responsive-First**: All layouts must be verified on Mobile (375px), Tablet (768px), and Desktop (1920px).
- **Transitions**: Interactive elements must have smooth 200ms transitions.
