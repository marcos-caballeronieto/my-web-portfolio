# UI/UX Design System

## Current State (Baseline)
- **Framework**: Bootstrap 5.3 (Standard components).
- **Theme**: Dark/Tech aesthetic with `Particles.js` background.
- **Components**: Cards for projects, standard Navbar, Mermaid diagrams for technical flows.
- **Interactions**: Basic hover effects, instant language toggle.

## Target Experience: "Premium Engineering Suite"
The goal is to move from a standard "bootstrap look" to a bespoke, premium engineering portfolio.

### 1. Visual Language
- **Accent Color**: Deep Teal or Electric Blue (to be finalized).
- **Background**: Multi-layered dark surface (not pure black).
- **Glassmorphism**: Subtle `backdrop-filter: blur(10px)` on cards and navigation.
- **Typography**: Shift from standard stacks to "Outfit" (Modern Sans) or "Inter" for readability.

### 2. Design Tokens (Initial Draft)
| Token | Value (Target) | Note |
|-------|----------------|------|
| `bg-primary` | HSL(220, 20%, 5%) | Deep Navy/Black |
| `surface-mid` | HSL(220, 20%, 12%) | Card backgrounds |
| `brand-accent`| HSL(190, 100%, 50%)| Electric Cyan |
| `border-subtle`| rgba(255, 255, 255, 0.1)| Ghost borders |

### 3. Micro-Animations (Using Framer Motion or Vanilla)
- **Scroll reveal**: Projects should fade and slide into view.
- **Magnetic buttons**: Navigation items should have a slight "pull" on hover.
- **Code highlighting**: Smooth transition between light/dark code themes if applicable.

## Core Improvement Areas
1. **Navigation**: More modern, minimal navbar with breadcrumbs.
2. **Project Cards**: Higher depth, cleaner typography, and better image-to-text ratio.
3. **Typography**: Establishing a clear hierarchy (Scale, Weight, Letter-spacing).
4. **Consistency**: Moving all hardcoded values to the `.css` token matrix.
