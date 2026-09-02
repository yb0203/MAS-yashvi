"""
MAS AI Labs — Slack Block Kit UI Views & Templates
Author: MAS AI PM
Description: Clean, sleek, high-signal Slack Block Kit views with zero visual noise.
"""

import json
from typing import Dict, Any, List

def map_status_to_rag(status: str, has_blocker: bool = False) -> str:
    """
    4 Canonical RAG Color Mappings:
    - Blocked: 🔴 (Red)
    - Completed: 🟢 (Green)
    - In Progress: 🟡 (Yellow / Amber)
    - Not Started / Planned: ⚪ (White)
    """
    s_lower = status.lower()
    if "blocked" in s_lower or "[!]" in s_lower or has_blocker:
        return "🔴"
    elif "completed" in s_lower or "done" in s_lower or "[x]" in s_lower:
        return "🟢"
    elif "in progress" in s_lower or "[-]" in s_lower:
        return "🟡"
    elif "planned" in s_lower or "not started" in s_lower or "[ ]" in s_lower:
        return "⚪"
    else:
        return "⚪"

def build_personal_dm_view(owner_name: str, tasks: List[Dict[str, Any]], day: int, sprint_num: int) -> List[Dict[str, Any]]:
    """Compact, sleek DM view for teammates."""
    task_bullets = []
    for t in tasks:
        rag = t.get("rag", "⚪")
        status = t.get("status", "Planned").replace("`", "").replace("[ ]", "").replace("[-]", "").replace("[x]", "").replace("[!]", "").strip()
        task_bullets.append(f"{rag} *`{t['id']}`*: {t['task']} `({status})`")

    return [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": f"👋 Standup Update • Day {day}", "emoji": True}
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"Hi *{owner_name}*! Google Meet Standup is at *8:00 PM IST*.\nPlease take 15 seconds to update your deliverables:"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "\n".join(task_bullets)
            }
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "⚡ Update Status (< 20s)", "emoji": True},
                    "style": "primary",
                    "value": json.dumps({"owner": owner_name, "sprint": sprint_num, "day": day}),
                    "action_id": "open_consolidated_modal_action"
                }
            ]
        }
    ]

def build_consolidated_update_modal(owner_name: str, all_owner_tasks: List[Dict[str, Any]], sprint_num: int, day: int) -> Dict[str, Any]:
    """Sleek, compact task update modal with zero clutter."""
    blocks = [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"Update status for your active deliverables (**Day {day}**):"}
        }
    ]

    status_options = [
        {"text": {"type": "plain_text", "text": "⚪ Not Started"}, "value": "[ ] Planned"},
        {"text": {"type": "plain_text", "text": "⏳ In Progress"}, "value": "[-] In Progress"},
        {"text": {"type": "plain_text", "text": "🚨 Blocked"}, "value": "[!] Blocked"},
        {"text": {"type": "plain_text", "text": "✅ Completed"}, "value": "[x] Completed"}
    ]

    for t in all_owner_tasks:
        t_id = t["id"]
        t_task = t["task"]
        curr_status = t.get("status", "[ ] Planned")

        # Initial option match
        initial_opt = status_options[0]
        if "completed" in curr_status.lower() or "done" in curr_status.lower() or "[x]" in curr_status:
            initial_opt = status_options[3]
        elif "in progress" in curr_status.lower() or "[-]" in curr_status:
            initial_opt = status_options[1]
        elif "blocked" in curr_status.lower() or "[!]" in curr_status:
            initial_opt = status_options[2]

        curr_outcome = t.get("actual_outcome", "")
        if curr_outcome == "-":
            curr_outcome = ""

        outcome_element = {
            "type": "plain_text_input",
            "action_id": f"input_outcome_{t_id}",
            "placeholder": {"type": "plain_text", "text": "Progress note / outcome / PR link (optional)"}
        }
        if curr_outcome and isinstance(curr_outcome, str) and curr_outcome.strip():
            outcome_element["initial_value"] = curr_outcome.strip()

        blocks.extend([
            {
                "type": "input",
                "block_id": f"status_block_{t_id}",
                "element": {
                    "type": "static_select",
                    "action_id": f"select_status_{t_id}",
                    "options": status_options,
                    "initial_option": initial_opt
                },
                "label": {"type": "plain_text", "text": f"{t_id}: {t_task[:60]}"}
            },
            {
                "type": "input",
                "block_id": f"outcome_block_{t_id}",
                "optional": True,
                "element": outcome_element,
                "label": {"type": "plain_text", "text": f"Note for {t_id}"}
            }
        ])

    # Global Blocker input
    blocks.append({
        "type": "input",
        "block_id": "global_blocker_block",
        "optional": True,
        "element": {
            "type": "plain_text_input",
            "action_id": "input_global_blocker",
            "placeholder": {"type": "plain_text", "text": "Any blocker or help needed on 8 PM call (optional)"}
        },
        "label": {"type": "plain_text", "text": "🚨 Blockers / Dependencies"}
    })

    task_ids_json = json.dumps([t["id"] for t in all_owner_tasks])

    return {
        "type": "modal",
        "callback_id": "submit_consolidated_standup_callback",
        "private_metadata": json.dumps({"owner": owner_name, "sprint": sprint_num, "day": day, "tasks": task_ids_json}),
        "title": {"type": "plain_text", "text": "Standup Update", "emoji": True},
        "submit": {"type": "plain_text", "text": "Save Update", "emoji": True},
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "blocks": blocks[:100]
    }

def build_add_task_modal(sprint_num: int) -> Dict[str, Any]:
    """Modal to add a sprint task."""
    return {
        "type": "modal",
        "callback_id": "submit_add_task_callback",
        "private_metadata": json.dumps({"sprint": sprint_num}),
        "title": {"type": "plain_text", "text": "Add New Task", "emoji": True},
        "submit": {"type": "plain_text", "text": "Add Task", "emoji": True},
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "blocks": [
            {
                "type": "input",
                "block_id": "add_owner_block",
                "element": {
                    "type": "static_select",
                    "action_id": "select_add_owner",
                    "options": [
                        {"text": {"type": "plain_text", "text": "👤 Yashvi"}, "value": "Yashvi"},
                        {"text": {"type": "plain_text", "text": "👤 Prakhar"}, "value": "Prakhar"},
                        {"text": {"type": "plain_text", "text": "👤 Shubham"}, "value": "Shubham"},
                        {"text": {"type": "plain_text", "text": "👤 Rohan"}, "value": "Rohan"},
                        {"text": {"type": "plain_text", "text": "👤 Gaurav"}, "value": "Gaurav"}
                    ],
                    "initial_option": {"text": {"type": "plain_text", "text": "👤 Yashvi"}, "value": "Yashvi"}
                },
                "label": {"type": "plain_text", "text": "Assignee"}
            },
            {
                "type": "input",
                "block_id": "add_comp_block",
                "element": {
                    "type": "static_select",
                    "action_id": "select_add_comp",
                    "options": [
                        {"text": {"type": "plain_text", "text": "📦 C1: Market & Intake"}, "value": "1"},
                        {"text": {"type": "plain_text", "text": "📦 C2: Product & Demos"}, "value": "2"},
                        {"text": {"type": "plain_text", "text": "📦 C3: Cloud & Automation"}, "value": "3"},
                        {"text": {"type": "plain_text", "text": "📦 C4: Leadership & Compute"}, "value": "4"}
                    ],
                    "initial_option": {"text": {"type": "plain_text", "text": "📦 C2: Product & Demos"}, "value": "2"}
                },
                "label": {"type": "plain_text", "text": "Compartment"}
            },
            {
                "type": "input",
                "block_id": "add_title_block",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "add_title_input",
                    "placeholder": {"type": "plain_text", "text": "e.g. Sales Suite architecture plan"}
                },
                "label": {"type": "plain_text", "text": "Task Title"}
            },
            {
                "type": "input",
                "block_id": "add_outcome_block",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "add_outcome_input",
                    "placeholder": {"type": "plain_text", "text": "e.g. Architecture doc ready for review"}
                },
                "label": {"type": "plain_text", "text": "Target Outcome"}
            },
            {
                "type": "input",
                "block_id": "add_date_block",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "add_date_input",
                    "placeholder": {"type": "plain_text", "text": "Fri, Sept 4 (Day 4)"}
                },
                "label": {"type": "plain_text", "text": "Deadline"}
            }
        ]
    }

def build_deprioritize_modal(sprint_num: int, all_tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Modal to de-prioritize a task."""
    task_options = []
    for t in all_tasks:
        task_options.append({
            "text": {"type": "plain_text", "text": f"{t['id']} ({t['owner']}): {t['task'][:50]}"},
            "value": t["id"]
        })

    return {
        "type": "modal",
        "callback_id": "submit_deprioritize_callback",
        "private_metadata": json.dumps({"sprint": sprint_num}),
        "title": {"type": "plain_text", "text": "De-prioritize Task", "emoji": True},
        "submit": {"type": "plain_text", "text": "De-prioritize", "emoji": True},
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "blocks": [
            {
                "type": "input",
                "block_id": "deprioritize_task_block",
                "element": {
                    "type": "static_select",
                    "action_id": "select_deprioritize_task",
                    "options": task_options[:100],
                    "placeholder": {"type": "plain_text", "text": "Select task"}
                },
                "label": {"type": "plain_text", "text": "Task to De-prioritize"}
            },
            {
                "type": "input",
                "block_id": "deprioritize_reason_block",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "deprioritize_reason_input",
                    "placeholder": {"type": "plain_text", "text": "Reason for deferral"}
                },
                "label": {"type": "plain_text", "text": "Reason"}
            }
        ]
    }

def build_pre_standup_digest_card(day: int, sprint_num: int, all_tasks: List[Dict[str, Any]], meet_url: str) -> Dict[str, Any]:
    """Sleek, high-signal Pre-Standup Summary Card for #all-mas-ai-labs."""
    completed = [t for t in all_tasks if "completed" in t["status"].lower() or "done" in t["status"].lower() or "[x]" in t["status"]]
    in_progress = [t for t in all_tasks if ("in progress" in t["status"].lower() or "[-]" in t["status"]) and t.get("rag") != "🔴"]
    not_started = [t for t in all_tasks if ("planned" in t["status"].lower() or "[ ]" in t["status"]) and t.get("rag") != "🔴"]
    blocked = [t for t in all_tasks if (t["blocker"] and t["blocker"].lower() != "none" and t["blocker"] != "-") or "[!]" in t["status"] or t.get("rag") == "🔴"]

    owner_groups = {}
    for t in all_tasks:
        owner_groups.setdefault(t["owner"], []).append(t)

    owner_sections = []
    for owner, tasks in owner_groups.items():
        lines = []
        for t in tasks:
            rag = t.get("rag", "⚪")
            status_clean = t["status"].replace("`", "").replace("[-]", "").replace("[x]", "").replace("[!]", "").replace("[ ]", "").strip()
            line = f"• {rag} *`{t['id']}`*: {t['task']} `[{status_clean}]`"
            if t.get("actual_outcome") and t["actual_outcome"] != "-" and t["actual_outcome"].strip():
                line += f"\n  ↳ _{t['actual_outcome'].strip()}_"
            if t.get("blocker") and t["blocker"].lower() != "none" and t["blocker"] != "-":
                line += f"\n  ↳ 🚨 *Blocker:* _{t['blocker'].strip()}_"
            lines.append(line)

        owner_sections.append(f"*{owner}:*\n" + "\n".join(lines))

    blocks = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": f"📊 Pre-Standup Task Summary • Day {day}", "emoji": True}
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    f"📞 *Google Meet starts at 8:00 PM IST*\n"
                    f"🟢 `{len(completed)} Done`  |  🟡 `{len(in_progress)} Active`  |  ⚪ `{len(not_started)} Planned`  |  🔴 `{len(blocked)} Blocked`"
                )
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "\n\n".join(owner_sections)
            }
        }
    ]

    if blocked:
        b_lines = []
        for t in blocked:
            b_lines.append(f"• 🔴 *{t['owner']} (`{t['id']}`)*: {t['blocker']}")
        blocks.extend([
            {"type": "divider"},
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "*🚨 Priority Blockers for 8:00 PM Call:*\n" + "\n".join(b_lines)}
            }
        ])

    blocks.extend([
        {"type": "divider"},
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "🟢 Join Google Meet", "emoji": True},
                    "url": meet_url or "https://meet.google.com/iek-smrh-zgg?authuser=0&hl=en_GB",
                    "style": "primary",
                    "action_id": "join_meet_button"
                },
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "📂 Sprint Plan", "emoji": True},
                    "url": "https://github.com/yb0203/MAS-yashvi/tree/main/sprint_execution",
                    "action_id": "open_sprint_link"
                }
            ]
        }
    ])

    return {"blocks": blocks}

def build_post_standup_structured_summary_card(
    day: int,
    sprint_num: int,
    owner_updates: Dict[str, List[str]],
    new_tasks: List[str],
    call_decisions: List[str],
    blockers: List[str]
) -> Dict[str, Any]:
    """
    Sleek, executive Post-Standup Highlights Card.
    Zero clutter, high readability, and clean formatting.
    """
    blocks = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": f"📝 Standup Call Summary • Day {day}", "emoji": True}
        }
    ]

    # 1. Pod Updates (Clean single bullets)
    owner_bullets = []
    for owner, bullets in owner_updates.items():
        if bullets:
            clean_bullets = "; ".join(bullets)
            owner_bullets.append(f"• *{owner}*: {clean_bullets}")

    if owner_bullets:
        blocks.extend([
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*🚀 Today's Progress & Discussions:*\n" + "\n".join(owner_bullets)
                }
            }
        ])

    # 2. Key Decisions
    if call_decisions:
        dec_bullets = "\n".join([f"• {d}" for d in call_decisions])
        blocks.extend([
            {"type": "divider"},
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "*🎯 Decisions & Alignment:*\n" + dec_bullets}
            }
        ])

    # 3. New Tasks Added
    if new_tasks:
        nt_bullets = "\n".join([f"• 🆕 {t}" for t in new_tasks])
        blocks.extend([
            {"type": "divider"},
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "*✨ New Scope / Action Items:*\n" + nt_bullets}
            }
        ])

    # 4. Blockers
    if blockers:
        blk_bullets = "\n".join([f"• 🔴 {b}" for b in blockers])
        blocks.extend([
            {"type": "divider"},
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "*🚨 Open Blockers:*\n" + blk_bullets}
            }
        ])

    blocks.extend([
        {"type": "divider"},
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"✅ Synced with `SPRINT_0{sprint_num}_WEEK_0{sprint_num}.md` and master Excel tracker."
                }
            ]
        }
    ])

    return {"blocks": blocks}
