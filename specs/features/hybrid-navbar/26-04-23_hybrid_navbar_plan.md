# Implementation Plan: Hybrid Cybernetic Navbar
**Date**: 26-04-23
**Feature**: Hybrid Cybernetic Navbar

## 1. Preparation & Assets
- [ ] Define CSS Variables for the split theme in `static/css/theme-tokens.css`.
    - `--bio-accent: #00f5ff;`
    - `--mech-accent: #ffaa00;`
    - `--nav-bg: rgba(10, 10, 15, 0.7);`
- [ ] Research/Download subtle SVG icons:
    - DNA/Heartbeat for Bio.
    - Gear/Blueprint grid for Mech.

## 2. Infrastructure (Django Templates)
- [ ] Locate `templates/base.html` and the navbar partial.
- [ ] Create `templates/components/navbar.html` if it doesn't exist as a separate file.
- [ ] Update `base.html` to include the new navbar.

## 3. UI Implementation (CSS/HTML)
- [ ] **Step 3.1: The CSS Grid/Flex Layout**
    - Create a container with `display: flex;` or `display: grid; grid-template-columns: 2fr 1fr 2fr;`.
    - Apply `backdrop-filter: blur(12px)` and sticky positioning.
- [ ] **Step 3.2: Zone Styling**
    - **Bio-Zone**: Implement rounded hover effects and teal text-shadows.
    - **Mech-Zone**: Implement chamfered (diagonal) hover effects using CSS `clip-path` and amber glows.
    - **Transition Area**: CSS linear-gradient background masking to blend the two zones at the center. 
- [ ] **Step 3.3: Link Components**
    - Apply domain-specific hover animations (pulse vs. snap).
    - Add logic to highlight the "active" zone based on the current page section.

## 4. Interaction & Logic
- [ ] **Step 4.1: Mobile Responsiveness**
    - Media queries to stack the zones or collapse into a single themed menu for screens < 992px.
    - Transitions for menu expansion.

## 5. Verification & Testing
- [ ] **Visual Check**: Cross-browser testing for `backdrop-filter` support.
- [ ] **Responsive Audit**: Mobile (375px), Tablet (768px), Desktop (1440px).
- [ ] **Logic Audit**: Verify Django navigation links point to correct views.
- [ ] **Accessibility**: Color contrast check with dev tools.

## 6. Cleanup & Documentation
- [ ] Remove old navbar code from templates.
- [ ] Update `specs/ui_ux.md` with the new design tokens.
- [ ] Archive this plan in `specs/features/hybrid-navbar/`.
