# Feature Requirements: Hybrid Cybernetic Navbar

## 1. Overview
A premium, responsive navigation bar that visually partitions the two core engineering domains of the portfolio: **Biomedical Engineering** and **Mechanical Engineering**. The design centers on a "Cybernetic Interface" aesthetic using glassmorphism and domain-specific visual cues.

## 2. Structural Specs
- **Total Width**: 100% of viewport.
- **Partitioning**:
    - **Left Zone (40%)**: Biomedical Engineering Focus.
    - **Center Zone (20%)**: Transition/Neutral/Logo Area.
    - **Right Zone (40%)**: Mechanical Engineering Focus.
- **Glassmorphism**: `backdrop-filter: blur(12px)` with a semi-transparent background (`rgba(10, 10, 15, 0.7)`).

## 3. Visual Domain Requirements

### Left Zone: Biomedical (The "Bio-Pulse")
- **Color Accent**: Clinical Teal / Electric Cyan (`#00f5ff`).
- **Styling**: 
    - Rounded corners for hover states (`border-radius: 20px`).
    - Subtle "pulse" glow animation on active items.
- **Elements**: 
    - Smooth, organic transitions on hover.
    - Potential "ECG/EKG" underline for the active link.

### Right Zone: Mechanical (The "Gear-Shift")
- **Color Accent**: Industrial Amber / Burnished Gold (`#ffaa00`) or Steel Blue (`#4a9eff`).
- **Styling**: 
    - Sharp, 45-degree chamfered hover states (`clip-path` or sharp borders).
    - "Riveted" border effect (subtle dots in corners).
- **Elements**: 
    - Precise, "staccato" hover animations (snappy rather than fluid).
    - Active link marked by a "Blueprint Grid" or "Measuring Scale" underline.

### Center Zone: The Transition (The "Neural Link")
- **Aesthetic**: Blended gradient (`Teal -> Neutral -> Amber`).
- **Elements**: 
    - Primary site logo or "M" monogram.
    - Interaction point for the language toggle (EN/ES).
    - Background: A "circuit-organic" fusion pattern where lines transition from curves to right angles.

## 4. Functional Requirements
- **Sticky Behavior**: Stays at the top of the viewport on scroll.
- **Responsive Design**:
    - **Desktop**: Full 3-zone layout.
    - **Mobile/Tablet**: Collapse into a single-theme burger menu (Neutral Dark) but maintain the accent gradients.
- **Theme Support**: Consistent with the `specs/ui_ux.md` dark-tech theme.
- **Django Integration**: Must use Django's `url` tags for navigation and handle active state logic.

## 5. Accessibility
- All text must pass WCAG AA contrast ratios against the blurred background.
- Keyboard navigation (Tab) must be visually clear on all three zones.
- ARIA labels for the split-zone navigation.
