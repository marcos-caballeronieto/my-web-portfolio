# Validation Plan: Hybrid Cybernetic Navbar

## 1. Unit & Integration Tests (Django)
- [ ] **Navigation Link Integrity**: Verify that all `<a>` tags in `navbar.html` use valid Django `{% url %}` tags and resolve to correct views.
- [ ] **Active Link Logic**: Test the template filters/tags used to apply the `.active` class to the correct navigation item based on the request path.

## 2. UI/UX Verification (Manual & Playwright)
- [ ] **Visual Layout**:
    - Left 40% shows Bio-Teal accents.
    - Right 40% shows Mech-Amber accents.
    - Center 20% displays the logo and transition gradient.
- [ ] **Glassmorphism**: Confirm background content is blurred behind the navbar on scroll.
- [ ] **Hover Interactions**:
    - Bio items: Rounded edges and soft pulse animation.
    - Mech items: Sharp edges and snappy glow.
- [ ] **Responsiveness**:
    - Layout switch to Burger Menu on viewports below 992px.
    - Burger menu retains the hybrid gradient/accent colors.

## 3. Performance & Accessibility
- [ ] **Performance**: Ensure no significant "Layout Shift" (CLS) when the navbar mounts.
- [ ] **Contrast**: Check all text color ratios against the background with Chrome DevTools Lighthouse or Axe.
- [ ] **Keyboard Nav**: Verify that `Tab` focus ring appears and matches the domain theme (Teal for left, Amber for right).

## 4. Acceptance Criteria (Definition of Done)
1. Navbar is sticky and visible on all pages.
2. Distinct visual styles for Bio vs. Mech zones are clearly distinguishable.
3. Transition area blends smoothly without a harsh vertical line.
4. Language toggle functions correctly within the center zone.
5. All links are functional.
