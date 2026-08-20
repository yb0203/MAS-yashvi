# MAS B2B SaaS Platform — Design System Specification (`design-system.md`)

This document outlines the visual design system, typography scale, color tokens, button styles, cards, status badges, and component tokens for Figma mockup creation and frontend implementation.

---

## 🎨 1. Color Palette & Token System

### 1.1 Neutral Palette (UI Foundation)
```css
--slate-50:  #F8FAFC;  /* Canvas Background */
--slate-100: #F1F5F9;  /* Card Hover / Subtle Fill */
--slate-200: #E2E8F0;  /* Borders & Dividers */
--slate-300: #CBD5E1;  /* Disabled Borders */
--slate-400: #94A3B8;  /* Placeholder Text / Icons */
--slate-500: #64748B;  /* Secondary Label Text */
--slate-700: #334155;  /* Sub-headings / Body Text */
--slate-900: #0F172A;  /* Primary Headings */
```

### 1.2 Status & Semantic Colors
- **Success / Eligible**: `#10B981` (Emerald 500) | Light Fill: `#ECFDF5`
- **Warning / Pending**: `#F59E0B` (Amber 500) | Light Fill: `#FFFBEB`
- **Danger / Urgent / Mandatory**: `#EF4444` (Red 500) | Light Fill: `#FEF2F2`
- **Info / Primary Action**: `#3B82F6` (Blue 500) | Light Fill: `#EFF6FF`
- **Accent / Token Credits**: `#8B5CF6` (Purple 500) | Light Fill: `#F5F3FF`

---

## 🔤 2. Typography Scale (Inter / Google Font Sans)

| Token Name | Size / Line Height | Font Weight | Usage |
| :--- | :--- | :--- | :--- |
| `display-lg` | `32px / 40px` | Bold (`700`) | Main Page Titles (e.g. *Dashboard Overview*) |
| `heading-md` | `24px / 32px` | SemiBold (`600`) | Section Headers (e.g. *Active Placement Drives*) |
| `heading-sm` | `18px / 24px` | SemiBold (`600`) | Card Titles, Modal Headers |
| `body-md` | `14px / 20px` | Regular (`400`) | Standard Body Paragraphs, Table Text |
| `body-sm` | `13px / 18px` | Medium (`500`) | Sub-labels, Input Field Labels |
| `caption` | `11px / 16px` | Regular (`400`) | Timestamps, Footer Notes, Secondary Badges |

---

## 🧱 3. Component Specs & Tokens

### 3.1 Buttons
- **Primary Button**: `background: var(--brand-primary); color: #FFFFFF; border-radius: 8px; height: 40px; padding: 0 16px; font-weight: 600;`
- **Secondary Button**: `background: #FFFFFF; color: var(--slate-700); border: 1px solid var(--slate-200); border-radius: 8px; height: 40px; padding: 0 16px;`
- **CTA Action Button (High Contrast)**: `background: #0F172A; color: #FFFFFF; border-radius: 8px;`

### 3.2 Cards & Containers
- **Standard Card Container**:
  - `background: #FFFFFF`
  - `border: 1px solid #E2E8F0`
  - `border-radius: 12px`
  - `box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05)`
  - `padding: 20px`

### 3.3 Status Pills & Badges
- **Pill Container**: `height: 24px; padding: 2px 10px; border-radius: 9999px; font-size: 12px; font-weight: 600;`
- **Variants**:
  - `🟢 Applied / Eligible`: Green fill (`#ECFDF5`), Text (`#047857`)
  - `🟡 In Progress / Scheduled`: Amber fill (`#FFFBEB`), Text (`#B45309`)
  - `🔴 Urgent / Action Required`: Red fill (`#FEF2F2`), Text (`#B91C1C`)
  - `🔵 Recommended`: Blue fill (`#EFF6FF`), Text (`#1D4ED8`)

---

## ♿ 4. Accessibility & UI Guidelines
- All text-to-background contrast ratios must satisfy **WCAG AA standard ($\ge 4.5:1$)**.
- Interactive buttons and inputs must have visible focus rings (`2px solid var(--brand-primary)`).
- Touch target minimum dimensions for mobile: `44px x 44px`.
