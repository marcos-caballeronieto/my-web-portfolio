# Web Portfolio Roadmap

This document outlines the next steps and planned features for the Web Portfolio project.

## 1. Miniprojects Integration
**Goal**: Add first-class support for miniprojects, allow each one to be linked to a main project, and present them with a lighter visual treatment than regular projects.
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
- **Frontend (Templates)**:
  - Modify `project_list.html`. 
  - Define which categories are "Main" (via a new boolean in the `Category` model `is_main = models.BooleanField()`).
  - Render "Main" categories as standard buttons.
  - Render the remaining categories inside a Bootstrap Dropdown menu.

## 3. Certificates UI Update
**Goal**: Improve the display of certificates by placing them in a dropdown or accordion layout.
- **Frontend (Templates)**:
  - Modify `about.html` and/or `home.html` where certificates are displayed.
  - Wrap the description of each certificate in a Bootstrap Dropdown, Accordion, or Modal to save vertical space and improve UX.

## 4. Conditional Rendering for Related Projects
**Goal**: Clean up the project detail page by hiding the "Related Projects/Related Miniprojects" section if a project doesn't have any.
- **Frontend (Templates)**:
  - Modify `project_detail.html`.
  - Wrap the Related Projects HTML section in a Django template condition: `{% if related_projects %}` ... `{% endif %}`.

---

*This roadmap is a living document and will be updated as we progress through the implementation.*
