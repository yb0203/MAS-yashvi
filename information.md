# Master Project & Stitch Reference Registry (`information.md`)

This file is the single source of truth for all active Stitch Project IDs, Screen IDs, URLs, Design System tokens, and MCP configurations. It eliminates redundant API lookups and ensures all design updates target the correct active canvas.

---

## 🎯 Active Working Stitch Project

* **Project Title**: `MAS - Student Dashboard - WIP`
* **Stitch Project ID**: `4064452573833842540`
* **Canonical Web URL**: [https://stitch.withgoogle.com/projects/4064452573833842540?pli=1](https://stitch.withgoogle.com/projects/4064452573833842540?pli=1)
* **Design System Name**: `Academic Nexus`
* **Color Mode**: `LIGHT` | **Base Font**: `Inter` | **Theme Primary**: `#0F172A` (Slate Ink)

---

## 🖥️ Final Master Screens Registry

| Screen Label / Milestone | Screen ID | Direct Stitch URL | Purpose & Active Modules |
| :--- | :--- | :--- | :--- |
| **`[FINAL] 4-Module Suite Dashboard (Senior / Placement-Ready)`** | `2810515ec62c48ce8040c30f93aeed82` | [Open 4-Module Screen](https://stitch.withgoogle.com/projects/4064452573833842540/screens/2810515ec62c48ce8040c30f93aeed82) | **Year 3-4 Placement Tier**: Coursework + Placement Readiness Radar + Upcoming Campus Drives + 1-on-1 Mentorship (with Credits). |
| **`[FINAL] 2-Module Academic Suite Dashboard (Junior / Learn + Test)`** | `c8065a4b533c4c73baea3d3acd232a4b` | [Open 2-Module Screen](https://stitch.withgoogle.com/projects/4064452573833842540/screens/c8065a4b533c4c73baea3d3acd232a4b) | **Year 1-2 Academic Tier**: Coursework (Identical) + Academic Standing Radar (Dean's List) + Assessments Lab (Mandatory/Practice) + Recent Submissions. |

---

## 🎨 Master Design System & Palette Tokens

```css
/* Core Palette Tokens */
--bg-canvas: #F8FAFC;        /* Soft Slate Tint Canvas */
--bg-surface: #FFFFFF;       /* Crisp White Card Container */
--text-primary: #0F172A;     /* Deep Slate Ink */
--text-secondary: #64748B;   /* Slate Neutral Gray */
--border-subtle: #E2E8F0;    /* 1px Hairline Card Border */
--card-radius: 16px;         /* Smooth Modern Squircle */
--header-height: 64px;       /* Pinned Institutional Top Bar */
--sidebar-width: 240px;      /* Expanded Nav Width (72px Collapsed) */

/* Academic Semantic Status Tokens */
--status-verified-bg: #ECFDF5;   --status-verified-text: #047857;  /* Emerald */
--status-urgent-bg: #FEF2F2;     --status-urgent-text: #B91C1C;    /* Crimson */
--status-warning-bg: #FFFBEB;    --status-warning-text: #B45309;   /* Amber */
--status-info-bg: #EFF6FF;       --status-info-text: #1D4ED8;      /* Royal Blue */
--badge-monogram-ml: #EEF2FF;    --badge-monogram-ml-text: #4338CA;/* Indigo */
--badge-monogram-sd: #F0FDF4;    --badge-monogram-sd-text: #15803D;/* Mint */
```

---

## 🗄️ Archive / Previous Projects Reference

* **Project Title**: `Student Management Dashboard` (Initial Sandbox)
* **Project ID**: `507089825794270011`
* **Canonical URL**: [https://stitch.withgoogle.com/projects/507089825794270011](https://stitch.withgoogle.com/projects/507089825794270011)
* **Status**: Archived (used for early layout inspiration).

---

## ⚙️ Active MCP Tooling Connection

```json
{
  "mcpServers": {
    "stitch": {
      "serverUrl": "https://stitch.googleapis.com/mcp",
      "tools": ["list_projects", "get_project", "get_screen", "generate_screen_from_text", "edit_screens", "generate_variants", "update_design_system"]
    },
    "mobbin": {
      "tools": ["search_screens", "search_flows", "search_sections"]
    }
  }
}
```
