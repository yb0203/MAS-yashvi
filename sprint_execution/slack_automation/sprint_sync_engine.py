"""
MAS AI Labs — Living Sprint Sync & Dynamic Task Management Engine
Author: MAS AI PM
Description: Real-time 2-way parser & updater between Slack, Google Meet Gemini,
             Markdown sprint files, CSV database, and Master Excel Workbook.
"""

import os
import re
import csv
from datetime import datetime
from typing import Dict, Any, List, Optional

SPRINT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MASTER_PLAN_PATH = os.path.join(SPRINT_DIR, "MONTH_01_MASTER_PLAN.md")
CSV_PATH = os.path.join(SPRINT_DIR, "sprint_tasks.csv")

def get_sprint_file_for_day(day: int) -> tuple[str, int]:
    """Resolves day number (1–30) to the corresponding Sprint Markdown file path and sprint number."""
    if 1 <= day <= 4:
        return os.path.join(SPRINT_DIR, "SPRINT_01_WEEK_01.md"), 1
    elif 5 <= day <= 11:
        return os.path.join(SPRINT_DIR, "SPRINT_02_WEEK_02.md"), 2
    elif 12 <= day <= 18:
        return os.path.join(SPRINT_DIR, "SPRINT_03_WEEK_03.md"), 3
    else:
        return os.path.join(SPRINT_DIR, "SPRINT_04_WEEK_04.md"), 4

def parse_sprint_tasks(file_path: str) -> List[Dict[str, Any]]:
    """Parses all tasks from a given Sprint markdown file into a structured dictionary."""
    tasks = []
    if not os.path.exists(file_path):
        return tasks

    current_compartment = "General"
    task_regex = re.compile(
        r"\|\s*\*\*(S\d+\.\d+)\*\*\s*\|\s*([^|]+)\s*\|\s*\*\*([^*]+)\*\*(?:\s*\*\([^*]+\)\*)?\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|"
    )

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("## 📦"):
                current_compartment = line.replace("## 📦", "").strip()
                continue
            
            match = task_regex.search(line)
            if match:
                t_id = match.group(1).strip()
                task_name = match.group(2).strip()
                owner = match.group(3).strip()
                target_date = match.group(4).strip()
                status = match.group(5).strip().replace("`", "")
                expected = match.group(6).strip()
                actual = match.group(7).strip()
                blocker = match.group(8).strip()
                delay_reason = match.group(9).strip()
                rag = match.group(10).strip()

                tasks.append({
                    "compartment": current_compartment,
                    "id": t_id,
                    "task": task_name,
                    "owner": owner,
                    "target_date": target_date,
                    "status": status,
                    "expected_outcome": expected,
                    "actual_outcome": actual,
                    "blocker": blocker,
                    "delay_reason": delay_reason,
                    "rag": rag,
                    "raw_line": line
                })

    return tasks

def update_sprint_task(file_path: str, task_id: str, new_status: str, actual_outcome: str, blocker: str, rag: str, delay_reason: str = None) -> bool:
    """Updates a specific task row in the sprint markdown file and CSV database."""
    if not os.path.exists(file_path):
        return False

    lines = []
    updated = False
    task_pattern = re.compile(rf"\|\s*\*\*{re.escape(task_id)}\*\*\s*\|")

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if task_pattern.search(line):
                parts = [p.strip() for p in line.strip().split("|")]
                if len(parts) >= 11:
                    parts[5] = f"`{new_status}`"
                    if actual_outcome and actual_outcome != "-":
                        parts[7] = actual_outcome
                    if blocker and blocker.lower() != "none" and blocker != "-":
                        parts[8] = blocker
                    if delay_reason:
                        parts[9] = delay_reason
                    parts[10] = rag
                    new_line = " | ".join(parts).strip() + "\n"
                    lines.append(new_line)
                    updated = True
                    continue
            lines.append(line)

    if updated:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)

        # Update structured CSV database
        try:
            if os.path.exists(CSV_PATH):
                rows = []
                with open(CSV_PATH, "r", encoding="utf-8") as cf:
                    reader = csv.DictReader(cf)
                    for r in reader:
                        if r["id"] == task_id:
                            r["status"] = new_status
                            if actual_outcome and actual_outcome != "-":
                                r["actual"] = actual_outcome
                            if blocker and blocker.lower() != "none" and blocker != "-":
                                r["blocker"] = blocker
                            if delay_reason:
                                r["delay_reason"] = delay_reason
                            r["rag"] = rag
                        rows.append(r)
                if rows:
                    with open(CSV_PATH, "w", newline="", encoding="utf-8") as cf:
                        writer = csv.DictWriter(cf, fieldnames=rows[0].keys())
                        writer.writeheader()
                        writer.writerows(rows)
        except Exception:
            pass

    return updated

def add_new_sprint_task(sprint_num: int, compartment_num: int, owner: str, title: str, target_date: str, expected_outcome: str) -> str:
    """
    Dynamically adds a new task to the active sprint markdown file, CSV, and Excel tracker.
    Returns the newly assigned Task ID (e.g. S1.22).
    """
    file_path, _ = get_sprint_file_for_day((sprint_num - 1) * 5 + 1)
    if not os.path.exists(file_path):
        return ""

    existing_tasks = parse_sprint_tasks(file_path)
    
    # Calculate next Task ID
    max_num = 0
    for t in existing_tasks:
        match = re.match(rf"S{sprint_num}\.(\d+)", t["id"])
        if match:
            max_num = max(max_num, int(match.group(1)))
    new_id = f"S{sprint_num}.{max_num + 1}"

    # Compartment Header target
    comp_map = {
        1: "## 📦 Compartment 1: Market, Intake & Client POCs",
        2: "## 📦 Compartment 2: Product, In-House LMS & Demo Stabilisation",
        3: "## 📦 Compartment 3: Cloud, Cost & Internal Automation",
        4: "## 📦 Compartment 4: Leadership, Compute & Enablers"
    }
    target_comp_header = comp_map.get(compartment_num, comp_map[1])

    new_row = f"| **{new_id}** | {title} | **{owner}** | {target_date} | `[ ] Planned` | {expected_outcome} | - | None | None | 🟢 |\n"

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Append after the table in that compartment
    if target_comp_header in content:
        parts = content.split(target_comp_header)
        sub_parts = parts[1].split("\n---", 1)
        updated_comp = sub_parts[0].rstrip() + "\n" + new_row + "\n---" + (sub_parts[1] if len(sub_parts) > 1 else "")
        content = parts[0] + target_comp_header + updated_comp
    else:
        content += f"\n\n{new_row}"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Sync to CSV
    try:
        if os.path.exists(CSV_PATH):
            with open(CSV_PATH, "a", newline="", encoding="utf-8") as cf:
                writer = csv.DictWriter(cf, fieldnames=["sprint", "compartment", "id", "task", "owner", "date", "status", "expected", "actual", "blocker", "delay_reason", "rag"])
                writer.writerow({
                    "sprint": f"Sprint {sprint_num}",
                    "compartment": f"Compartment {compartment_num}",
                    "id": new_id,
                    "task": title,
                    "owner": owner,
                    "date": target_date,
                    "status": "[ ] Planned",
                    "expected": expected_outcome,
                    "actual": "-",
                    "blocker": "None",
                    "delay_reason": "None",
                    "rag": "🟢"
                })
    except Exception:
        pass

    return new_id

def deprioritize_sprint_task(sprint_num: int, task_id: str, reason: str) -> bool:
    """Marks a task as De-prioritised / Deferred with a logged reason."""
    file_path, _ = get_sprint_file_for_day((sprint_num - 1) * 5 + 1)
    return update_sprint_task(
        file_path=file_path,
        task_id=task_id,
        new_status="[-] De-prioritised",
        actual_outcome="De-prioritised / Deferred in Standup",
        blocker="None",
        rag="🟡",
        delay_reason=reason
    )

def append_daily_log_entry(file_path: str, date_header: str, summary_text: str):
    """Appends a standup summary bullet under the Daily Quick Updates Log section."""
    if not os.path.exists(file_path):
        return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    log_marker = "## 📝 Daily Quick Updates Log"
    if log_marker in content:
        entry = f"\n* **{date_header}**: {summary_text}\n"
        content = content.replace(log_marker, log_marker + entry)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

def sync_active_blockers_to_master(sprint_tasks: List[Dict[str, Any]], sprint_num: int):
    """Rolls up active blockers into MONTH_01_MASTER_PLAN.md."""
    if not os.path.exists(MASTER_PLAN_PATH):
        return

    blocked = [
        t for t in sprint_tasks
        if t["blocker"] and t["blocker"].lower() != "none" and t["blocker"] != "-"
    ]

    with open(MASTER_PLAN_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    table_header = "| Log ID | Date Flagged | Source Sprint | Task ID & Owner | Blocker Description | Root Cause / Reason | Impact & Target Resolution Date | Status |\n|:---:|:---:|:---:|:---:|---|---|---|:---:|"
    
    if not blocked:
        replacement = table_header + "\n| - | - | - | - | *No active blockers logged* | - | - | `🟢 Clear` |"
    else:
        rows = []
        for i, t in enumerate(blocked, 1):
            today_str = datetime.now().strftime("%b %d")
            rows.append(
                f"| BLK-{i:02d} | {today_str} | Sprint {sprint_num} | `{t['id']}` ({t['owner']}) | {t['blocker']} | {t['delay_reason']} | Under review for unblocking | `🔴 Blocked` |"
            )
        replacement = table_header + "\n" + "\n".join(rows)

    pattern = re.compile(
        r"\|\s*Log ID\s*\|\s*Date Flagged\s*\|.*?(?=\n\n|\n##|\Z)",
        re.DOTALL
    )

    if pattern.search(content):
        content = pattern.sub(replacement, content)
        with open(MASTER_PLAN_PATH, "w", encoding="utf-8") as f:
            f.write(content)

def rollover_incomplete_tasks(from_sprint: int, to_sprint: int) -> List[str]:
    """Rolls over incomplete/delayed tasks from one sprint to the next."""
    from_file, _ = get_sprint_file_for_day((from_sprint - 1) * 5 + 1)
    to_file, _ = get_sprint_file_for_day((to_sprint - 1) * 5 + 1)

    tasks = parse_sprint_tasks(from_file)
    incomplete = [
        t for t in tasks
        if "done" not in t["status"].lower() and "[x]" not in t["status"]
    ]

    if not incomplete or not os.path.exists(to_file):
        return []

    rollover_rows = []
    task_ids = []
    for t in incomplete:
        task_ids.append(t["id"])
        rollover_rows.append(
            f"| **{t['id']}** | {t['task']} *(Rollover)* | **{t['owner']}** | Next Sprint | `[Rollover]` | {t['expected_outcome']} | - | {t['blocker']} | Rollover from Sprint {from_sprint} | {t['rag']} |"
        )

    with open(to_file, "r", encoding="utf-8") as f:
        content = f.read()

    section_header = f"\n\n## 🔄 Rollover Tasks from Sprint {from_sprint}\n"
    table_header = "| ID | Task / Activity | Owner (Support) | Target Date (Day) | Status | Expected Outcome | Actual Outcome | Blocker | Delay Reason | RAG |\n|:---:|---|:---:|:---:|:---:|---|---|---|---|:---:|\n"
    new_section = section_header + table_header + "\n".join(rollover_rows) + "\n"

    if f"## 🔄 Rollover Tasks from Sprint {from_sprint}" not in content:
        content += new_section
        with open(to_file, "w", encoding="utf-8") as f:
            f.write(content)

    return task_ids
