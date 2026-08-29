"""
MAS AI Labs — Sprint Markdown Sync & Rollover Engine
Author: MAS AI PM
Description: Provides core read/write/sync operations on SPRINT_0X_WEEK_0X.md 
             and MONTH_01_MASTER_PLAN.md for the Slack Standup Bot.
"""

import os
import re
from datetime import datetime
from typing import List, Dict, Any, Tuple

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MASTER_PLAN_PATH = os.path.join(BASE_DIR, "MONTH_01_MASTER_PLAN.md")

def get_sprint_file_for_day(day: int) -> Tuple[str, int]:
    """Returns the file path and sprint number for a given day in September 2026."""
    if 1 <= day <= 4:
        return os.path.join(BASE_DIR, "SPRINT_01_WEEK_01.md"), 1
    elif 5 <= day <= 11:
        return os.path.join(BASE_DIR, "SPRINT_02_WEEK_02.md"), 2
    elif 12 <= day <= 18:
        return os.path.join(BASE_DIR, "SPRINT_03_WEEK_03.md"), 3
    else:
        return os.path.join(BASE_DIR, "SPRINT_04_WEEK_04.md"), 4

def parse_sprint_tasks(file_path: str) -> List[Dict[str, Any]]:
    """Parses task rows from a sprint markdown file."""
    if not os.path.exists(file_path):
        return []

    tasks = []
    task_regex = re.compile(
        r"\|\s*\*\*(S\d+\.\d+)\*\*\s*\|\s*([^|]+)\s*\|\s*\*\*([^*]+)\*\*(?:\s*\*\([^*]+\)\*)?\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|"
    )

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = task_regex.search(line)
            if match:
                task_id = match.group(1).strip()
                desc = match.group(2).strip()
                owner = match.group(3).strip()
                date_str = match.group(4).strip()
                status = match.group(5).strip().replace("`", "")
                expected_outcome = match.group(6).strip()
                actual_outcome = match.group(7).strip()
                blocker = match.group(8).strip()
                delay_reason = match.group(9).strip()
                rag = match.group(10).strip()

                tasks.append({
                    "id": task_id,
                    "task": desc,
                    "owner": owner,
                    "date_str": date_str,
                    "status": status,
                    "expected_outcome": expected_outcome,
                    "actual_outcome": actual_outcome,
                    "blocker": blocker,
                    "delay_reason": delay_reason,
                    "rag": rag,
                    "raw_line": line
                })

    return tasks

def update_sprint_task(file_path: str, task_id: str, new_status: str, actual_outcome: str, blocker: str, rag: str) -> bool:
    """Updates a specific task row in the sprint markdown file."""
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
                    # parts: ['', '**ID**', 'Task', '**Owner**', 'Date', 'Status', 'Expected', 'Actual', 'Blocker', 'Delay Reason', 'RAG', '']
                    parts[5] = f"`{new_status}`"
                    if actual_outcome and actual_outcome != "-":
                        parts[7] = actual_outcome
                    if blocker and blocker.lower() != "none" and blocker != "-":
                        parts[8] = blocker
                    parts[10] = rag
                    new_line = " | ".join(parts).strip() + "\n"
                    lines.append(new_line)
                    updated = True
                    continue
            lines.append(line)

    if updated:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)

    return updated

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

    if not os.path.exists(from_file) or not os.path.exists(to_file):
        return []

    from_tasks = parse_sprint_tasks(from_file)
    incomplete = [t for t in from_tasks if "done" not in t["status"].lower() and "[x]" not in t["status"]]

    rolled_over_ids = []
    with open(to_file, "a", encoding="utf-8") as f:
        f.write(f"\n\n### 🔄 Rollover Tasks from Sprint {from_sprint}\n")
        f.write("| ID | Task / Activity | Owner (Support) | Target Date | Status | Expected Outcome | Actual Outcome | Blocker | Delay Reason | RAG |\n")
        f.write("|:---:|---|:---:|:---:|:---:|---|---|---|---|:---:|\n")
        for t in incomplete:
            f.write(
                f"| **{t['id']}-R** | [Rollover] {t['task']} | **{t['owner']}** | Sprint {to_sprint} | `[!] Rollover` | {t['expected_outcome']} | - | {t['blocker']} | Rolled over from Sprint {from_sprint} | 🟡 |\n"
            )
            rolled_over_ids.append(t["id"])

    return rolled_over_ids
