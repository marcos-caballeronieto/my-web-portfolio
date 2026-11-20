# Web Portfolio Roadmap

This document outlines completed work and the next planned features for the Web Portfolio project.

## 1. Miniprojects Integration
**Goal**: Add first-class support for miniprojects, allow each one to be linked to a main project, and present them with a lighter visual treatment than regular projects.
- **Status**: **Completed**
- **Backend (Models)**:
  - Add `is_miniproject = models.BooleanField(default=False)` to `Project` so the app can distinguish miniprojects from regular projects.
  - Add a relationship field that links miniprojects to their parent/main project(s). Use the simplest model that fits the current data structure, but make the connection explicit and easy to query.
- **Frontend (Templates)**:
  - Update `project_detail.html` to render an "Associated Miniprojects" section when a project has linked miniprojects.
  - Update `project_list.html` to include a subtle link or button to a new `mini_projects_list` page that shows only miniprojects.
  - Create `mini_projects_list` page that shows only miniprojects.
  - Display miniprojects with a smaller, flatter card style than regular projects.
  - For miniproject cards, show only the title and image. Do not show the short description.

## 2. Dynamic UI for Categories (Projects)
**Goal**: Clean up the project filter UI by using a dropdown for most categories while keeping main categories as prominent buttons.
- **Status**: **Completed**
- **Frontend (Templates)**:
  - Modify `project_list.html`.
  - Define which categories are "Main" (via a new boolean in the `Category` model `is_main = models.BooleanField()`).
  - Render "Main" categories as standard buttons.
  - Render the remaining categories inside a Bootstrap Dropdown menu.

## 3. Certificates UI Update
**Goal**: Improve the display of certificates by placing them in a dropdown or accordion layout.
- **Status**: **Completed**
- **Frontend (Templates)**:
  - Modify `about.html` and/or `home.html` where certificates are displayed.
  - Wrap the description of each certificate in a Bootstrap Dropdown, Accordion, or Modal to save vertical space and improve UX.

## 4. Conditional Rendering for Related Projects
**Goal**: Clean up the project detail page by hiding the "Related Projects/Related Miniprojects" section if a project doesn't have any.
- **Status**: **Completed**
- **Frontend (Templates)**:
  - Modify `project_detail.html`.
  - Wrap the Related Projects HTML section in a Django template condition: `{% if related_projects %}` ... `{% endif %}`.

## 5. Certificates, Courses, and Skills Content
**Goal**: Make certificates, courses, and skills manageable as structured content through Django Admin and present them on their own categorized pages.
- **Status**: **Completed**
- **Backend (Models)**:
  - Keep certificates as an editable Django model and extend or adapt the content model as needed to represent both certificates and courses.
  - Add a `Skill` model editable from Django Admin.
  - Add category support for certificates/courses and skills so each can be organized and filtered by category.
  - Add any required ordering, visibility, links, dates, icons, and descriptions to support the pages without hardcoded content.
- **Frontend (Pages and Templates)**:
  - Create a dedicated page for certificates and courses.
  - Create a dedicated page for skills.
  - Display certificates, courses, and skills grouped or filterable by category.
  - Add navigation links to the new pages from the relevant portfolio sections.
- **Routing and Admin**:
  - Add URLs and views for the certificates/courses page and the skills page.
  - Register and configure the new models in Django Admin.

## 6. Editable Overall Description
**Goal**: Manage the portfolio's overall introductory description from Django Admin instead of keeping it hardcoded in templates.
- **Status**: **Planned**
- **Backend (Model)**:
  - Add a model for the overall portfolio description, including the localized content required by the site.
  - Configure it as editable from Django Admin and support the intended single/current description entry.
- **Frontend (Templates)**:
  - Replace the hardcoded overall description with the value from the model wherever it is displayed.
  - Preserve the current language-aware presentation.

---

*This roadmap is a living document and will be updated as we progress through the implementation.*
