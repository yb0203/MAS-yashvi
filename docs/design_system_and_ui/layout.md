# MAS B2B SaaS Platform — Application Layout Architecture (`layout.md`)

This document defines the structural grid, navigation shell, white-label customization points, and responsive layout specifications for the generalized B2B Educational SaaS platform.

---

## 🏛️ 1. Master Shell Architecture

The application layout uses a **persistent 2-column sidebar shell** with a top header and a main content canvas:

```
+---------------------------------------------------------------------------------------------------+
|  [TOP HEADER BAR]                                                                                 |
|  [INSTITUTION LOGO]     [🔍 Global Search...]                [🔔 Notifications (3)]  [👤 Avatar]   |
+---------------------------------------------------------------------------------------------------+
|  [LEFT SIDEBAR]     |  MAIN CONTENT CANVAS (`/student/*`)                                         |
|  (Fixed 240px)      |  (Fluid 100% minus 240px)                                                   |
|                     |                                                                             |
|  • Dashboard        |  +-----------------------------------------------------------------------+  |
|  • My Courses       |  | BREADCRUMB / PAGE TITLE                                               |  |
|  • Assessments      |  +-----------------------------------------------------------------------+  |
|  • Placement Drives |  |                                                                       |  |
|  • Mentorship       |  |  DYNAMIC ROUTE CONTENT CANVAS                                         |  |
|                     |  |  (Cards, Grids, Data Tables, Charts)                                  |  |
|  -----------------  |  |                                                                       |  |
|  • My Profile       |  +-----------------------------------------------------------------------+  |
|  • Settings         |                                                                             |
|  • Help & Support   |-----------------------------------------------------------------------------|
|                     |  [FOOTER STRIP] Institutional Copyright & Support Links                     |
|  [Collapse < ]      |                                                               [ ✨ AI Button ]|
+---------------------+-------------------------------------------------------------------------------+
```

---

## 🎛️ 2. Detailed Shell Component Specifications

### 2.1 Top Header Bar
- **Height**: `64px` (Fixed)
- **Background**: Surface Primary (`var(--bg-surface)`) with a subtle bottom border (`1px solid var(--border-subtle)`).
- **Left Region**: 
  - College/Institution Logo (`max-height: 36px`).
  - Optional Institution Name text (if logo image is square/icon-only).
- **Center Region**:
  - Global Search Input (`320px` width): Instant search for courses, test titles, and active placement drive company names.
- **Right Region**:
  - **Notification Bell**: Badge counter showing unread TPO alerts, test reminders, and mentor slot updates.
  - **Profile Avatar Dropdown**: Displays student initials/avatar. Clicking opens a dropdown menu with: `View Profile`, `Account Settings`, `Switch Theme`, `Logout`.

### 2.2 Left Navigation Sidebar
- **Width**: `240px` (Expanded) / `72px` (Collapsed).
- **Behavior**: Persistent on Desktop ($>1024\text{px}$); Collapsible drawer on Mobile/Tablet ($<1024\text{px}$).
- **Primary Section**:
  - 🏠 **Dashboard**: `/student/dashboard`
  - 📘 **My Courses**: `/student/courses` (Mr. Learn)
  - 📝 **Assessments & Exams**: `/student/assessments` (Mr. Test)
  - 💼 **Placement Drives**: `/student/placements` (Mr. Hire)
  - 🤝 **1-on-1 Mentorship**: `/student/mentorship` (Mr. Mentor)
- **Secondary Footer Section** (Pinned to Bottom):
  - 👤 **My Profile**: `/student/profile`
  - ⚙️ **Settings**: `/student/settings`
  - ❓ **Help & Support**: `/student/support` (TPO helpline)
  - ◀ **Collapse Sidebar Button**: Toggle icon button.

### 2.3 Main Content Canvas
- **Padding**: `32px` on Desktop, `16px` on Mobile.
- **Max Width Container**: `1440px` centered canvas.
- **Grid Layout**: 12-Column CSS Grid / Flexbox system.

### 2.4 Floating Action Button (AI Assistant)
- **Position**: Fixed bottom-right corner (`bottom: 24px`, `right: 24px`).
- **Icon**: Sparkle AI icon (`✨ Aarya AI`).
- **Behavior**: Clicking opens a sliding drawer modal for AI voice/chat student assistance.

---

## 🎨 3. White-Label Customization Token Mapping

To maintain 100% white-label capability for any partner university, the layout injects dynamic institutional CSS tokens at the `:root` level:

```css
:root {
  /* Institution Brand Colors (Configured in College Admin Panel) */
  --brand-primary: #1E3A8A;       /* e.g., Deep University Blue */
  --brand-secondary: #0D9488;     /* Teal Accent */
  --brand-header-bg: #FFFFFF;     /* Header Background */
  --brand-logo-url: url('/tenant/logo.png');
  
  /* System UI Neutral Tokens */
  --bg-canvas: #F8FAFC;
  --bg-surface: #FFFFFF;
  --text-primary: #0F172A;
  --text-secondary: #475569;
  --border-subtle: #E2E8F0;
}
```

---

## 📱 4. Responsive Breakpoints

| Breakpoint Name | Target Devices | Layout Adjustments |
| :--- | :--- | :--- |
| **Mobile (`< 640px`)** | Smartphones | Sidebar converts to bottom navigation bar or hamburger drawer. Canvas padding `12px`. Grid converts to 1-column. |
| **Tablet (`640px - 1024px`)** | iPads / Tablets | Sidebar auto-collapses to `72px` icon-only mode. Grid converts to 2-column. |
| **Desktop (`> 1024px`)** | Laptops & Monitors | Full `240px` sidebar expanded. 3-column / 12-column grid layout enabled. |
