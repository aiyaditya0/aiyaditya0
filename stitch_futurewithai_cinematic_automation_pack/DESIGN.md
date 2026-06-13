---
name: Cinematic Automation
colors:
  surface: '#1b110a'
  surface-dim: '#1b110a'
  surface-bright: '#43372e'
  surface-container-lowest: '#150c06'
  surface-container-low: '#241912'
  surface-container: '#281d15'
  surface-container-high: '#33281f'
  surface-container-highest: '#3f3229'
  on-surface: '#f3dfd1'
  on-surface-variant: '#ddc1ae'
  inverse-surface: '#f3dfd1'
  inverse-on-surface: '#3a2e25'
  outline: '#a58c7b'
  outline-variant: '#564334'
  surface-tint: '#ffb77f'
  primary: '#ffb77f'
  on-primary: '#4e2600'
  primary-container: '#ff8a00'
  on-primary-container: '#613100'
  inverse-primary: '#914c00'
  secondary: '#c9c6c5'
  on-secondary: '#313030'
  secondary-container: '#4a4949'
  on-secondary-container: '#bab8b7'
  tertiary: '#88ceff'
  on-tertiary: '#00344d'
  tertiary-container: '#00b3fc'
  on-tertiary-container: '#004260'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdcc4'
  primary-fixed-dim: '#ffb77f'
  on-primary-fixed: '#2f1500'
  on-primary-fixed-variant: '#6f3900'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c9c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474646'
  tertiary-fixed: '#c8e6ff'
  tertiary-fixed-dim: '#88ceff'
  on-tertiary-fixed: '#001e2e'
  on-tertiary-fixed-variant: '#004c6d'
  background: '#1b110a'
  on-background: '#f3dfd1'
  surface-variant: '#3f3229'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  section-gap: 120px
---

## Brand & Style

This design system is built on the narrative of "Cinematic Automation"—a fusion of high-end luxury editorial and cutting-edge industrial technology. It targets a sophisticated audience that values precision, power, and elegance. 

The aesthetic is a hybrid of **Glassmorphism** and **Corporate Modern**, utilizing deep obsidian surfaces to create a sense of infinite depth. By leveraging high-contrast typography and vibrant, glowing accents, the UI feels alive and responsive, like a premium flight deck or a high-end fashion digital experience.

**Key Principles:**
- **Cinematic Depth:** Use layering, backdrop blurs, and subtle noise textures to create a multi-dimensional environment.
- **Luminous Focus:** The vibrant orange is used sparingly but powerfully to direct attention and signal energy.
- **Editorial Precision:** High-contrast serif headlines provide an authoritative, luxurious voice.

## Colors

The palette is strictly dark-mode, emphasizing high-contrast readability and energy. 

- **The Void (#050505):** The fundamental base layer, providing total immersion.
- **Vibrant Glow (#FF8A00):** The primary action color. It should be treated as a light source, often accompanied by soft glows (outer glows) rather than flat fills.
- **Hierarchical Grays:** Use Primary White for headers and critical data, and Secondary Gray for metadata and descriptions to maintain visual calm.
- **The Glass Layer:** Elevated components use a semi-transparent surface with a heavy blur to maintain legibility while showcasing background depth.

## Typography

Typography is used to create a stark contrast between "Heritage Luxury" and "Modern Utility."

- **Serif Accents:** Use **Playfair Display** for large headlines, hero sections, and editorial quotes. It introduces a human, sophisticated touch to the technical interface.
- **Sans-serif Utility:** **Inter** handles all functional data, body text, and labels. It ensures maximum legibility at small sizes and maintains a professional, neutral tone.
- **Case Styling:** Labels and small headers should frequently use uppercase with increased letter-spacing to reinforce the "Automation" and "Systemic" feel.

## Layout & Spacing

This design system utilizes a **Fluid Grid** model with significant vertical "breathing room" to maintain the cinematic feel.

- **Desktop:** 12-column grid with wide 64px margins. Content is often centered or offset to create dynamic, editorial layouts.
- **Mobile:** 4-column grid with 16px margins. 
- **Rhythm:** All spacing is based on a 4px baseline. Use larger "Section Gaps" (120px+) to separate distinct thematic areas, preventing the dark interface from feeling cluttered.
- **Safe Areas:** Background blurs should extend to the edges of containers, but content must remain within defined safe margins to ensure focus.

## Elevation & Depth

Depth is not communicated through shadows, but through **light and transparency**.

- **Level 0 (Base):** Deep Black (#050505) with a subtle grain/noise texture overlay (2% opacity) to prevent banding.
- **Level 1 (Surfaces):** Dark Surface (#0D0D0D) for static containers.
- **Level 2 (Interactive/Floating):** Glassmorphism layer. Use `backdrop-filter: blur(20px)` and `rgba(20, 20, 20, 0.55)`. 
- **Borders:** Containers should have a 1px solid border (#232323). For active states, this border can transition to a subtle Orange Glow.
- **Glows:** High-priority elements use a "drop-shadow" that mimics a light source: `0px 0px 20px rgba(255, 138, 0, 0.3)`.

## Shapes

The shape language is "Hyper-Softened Industrial." While the colors are aggressive, the shapes are welcoming and ergonomic.

- **Primary Radius:** A base of 28px (`rounded-xl` in this system) is used for cards and primary containers to create a premium, "molded" look.
- **Small Elements:** Buttons and input fields use 12px to 16px radius to maintain a consistent softness without becoming fully circular (unless they are pill-shaped chips).
- **Icons:** Use medium-stroke icons (2px) with rounded caps to match the typography's weight.

## Components

### Buttons
- **Primary:** Solid #FF8A00 fill with #050505 text. On hover, add an external glow.
- **Secondary:** Transparent fill with a 1px #FF8A00 border. 
- **Tertiary:** Subtle gray text that turns white on hover, with no border or background.

### Cards
- Always use the Glassmorphism style with 20px blur and 28px corner radius.
- Internal padding should be generous (24px to 32px).

### Input Fields
- Dark Surface fill (#0D0D0D) with a #232323 border.
- On focus, the border glows #FF8A00 and the label shifts upwards using the `label-sm` style.

### Transitions & Motion
- All interactive states must use the signature transition: `600ms cubic-bezier(.22,.61,.36,1)`.
- Use "fade-in and slide-up" motions for page transitions to reinforce the cinematic narrative.

### Progress Bars
- Use a dual-layered approach: a dark track (#141414) and a glowing orange fill. The fill should have a leading-edge light burst effect.