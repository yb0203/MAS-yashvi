"""
MAS AI Labs — Slack Block Kit UI Views & Templates
Author: MAS AI PM
Description: Centralized UI library generating clean, modern Slack Block Kit
             cards for Personal DMs, Modals, Pre-Standup Digests, and Structured Post-Standup Summaries.
"""

import json
from typing import Dict, Any, List

def map_status_to_rag(status: str, has_blocker: bool = False) -> str:
    """Automatically maps the 4 task statements (Planned, In Progress, Blocked, Completed) to RAG indicator."""
    s_lower = status.lower()
    if "blocked" in s_lower or "[!]" in s_lower or has_blocker:
        return "🔴"
    elif "completed" in s_lower or "done" in s_lower or "[x]" in s_lower:
        return "🟢"
    elif "in progress" in s_lower or "[-]" in s_lower:
        return "🟢"
    else:  # Planned
        return "🟢"

def build_personal_dm_view(owner_name: str, tasks: List[Dict[str, Any]], day: int, sprint_num: int) -> List[Dict[str, Any]]:
    """Builds a compact, personalized 1-screen DM view for task owners."""
    task_bullets = []
    for t in tasks:
        task_bullets.append(
            f"• *`{t['id']}`*: {t['task']}\n"
            f"   ↳ *Status:* `{t['status']}` | *RAG:* {t['rag']}"
        )

    return [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"👋 Hey {owner_name}! Daily Standup (Day {day})",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    f"⏰ *Google Meet Standup is at 8:00 PM IST.*\n"
                    f"Which tasks did you pick and work on today? Take *20 seconds* to update:"
                )
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*📌 Your Sprint Deliverables:*\n" + "\n".join(task_bullets)
            }
        },
        {"type": "divider"},
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "⚡ Update Today's Focus (< 20s)",
                        "emoji": True
                    },
                    "style": "primary",
                    "value": json.dumps({"owner": owner_name, "sprint": sprint_num, "day": day}),
                    "action_id": "open_consolidated_modal_action"
                }
            ]
        }
    ]

def build_consolidated_update_modal(owner_name: str, all_owner_tasks: List[Dict[str, Any]], sprint_num: int, day: int) -> Dict[str, Any]:
    """
    Tier 2 Modal: Task-Wise Progress & Status Update Form.
    Provides dedicated completion & progress tracking for EVERY task assigned to the person.
    """
    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"👋 *Hi {owner_name}!* Update today's progress & status for each of your deliverables (**Day {day}**):"
            }
        },
        {"type": "divider"}
    ]

    status_options = [
        {"text": {"type": "plain_text", "text": "⚪ Planned"}, "value": "[ ] Planned"},
        {"text": {"type": "plain_text", "text": "⏳ In Progress"}, "value": "[-] In Progress"},
        {"text": {"type": "plain_text", "text": "🚨 Blocked"}, "value": "[!] Blocked"},
        {"text": {"type": "plain_text", "text": "✅ Completed"}, "value": "[x] Completed"}
    ]

    for t in all_owner_tasks:
        t_id = t["id"]
        t_task = t["task"]
        curr_status = t.get("status", "[ ] Planned")

        # Match initial option
        initial_opt = status_options[0] # Default Planned
        if "completed" in curr_status.lower() or "done" in curr_status.lower() or "[x]" in curr_status:
            initial_opt = status_options[3]
        elif "in progress" in curr_status.lower() or "[-]" in curr_status:
            initial_opt = status_options[1]
        elif "blocked" in curr_status.lower() or "[!]" in curr_status:
            initial_opt = status_options[2]

        curr_outcome = t.get("actual_outcome", "")
        if curr_outcome == "-":
            curr_outcome = ""

        blocks.extend([
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*📌 `{t_id}`: {t_task}*\n*Target:* _{t.get('expected_outcome', '-')}_"
                }
            },
            {
                "type": "input",
                "block_id": f"status_block_{t_id}",
                "element": {
                    "type": "static_select",
                    "action_id": f"select_status_{t_id}",
                    "options": status_options,
                    "initial_option": initial_opt
                },
                "label": {"type": "plain_text", "text": f"Status for {t_id}"}
            },
            {
                "type": "input",
                "block_id": f"outcome_block_{t_id}",
                "optional": True,
                "element": {
                    "type": "plain_text_input",
                    "action_id": f"input_outcome_{t_id}",
                    "initial_value": curr_outcome if curr_outcome else None,
                    "placeholder": {"type": "plain_text", "text": "e.g. Completed draft / 50% done / PR link"}
                },
                "label": {"type": "plain_text", "text": f"Today's Progress / Outcome for {t_id}"}
            },
            {"type": "divider"}
        ])

    # Global Blocker input
    blocks.append({
        "type": "input",
        "block_id": "global_blocker_block",
        "optional": True,
        "element": {
            "type": "plain_text_input",
            "action_id": "input_global_blocker",
            "placeholder": {"type": "plain_text", "text": "None / Waiting on API key / Need sync with Rohan"}
        },
        "label": {"type": "plain_text", "text": "🚨 Active Blocker / Help Needed on Call (If any)"}
    })

    task_ids_json = json.dumps([t["id"] for t in all_owner_tasks])

    return {
        "type": "modal",
        "callback_id": "submit_consolidated_standup_callback",
        "private_metadata": json.dumps({"owner": owner_name, "sprint": sprint_num, "day": day, "tasks": task_ids_json}),
        "title": {"type": "plain_text", "text": "Daily Standup Update", "emoji": True},
        "submit": {"type": "plain_text", "text": "Submit All", "emoji": True},
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "blocks": blocks[:100]
    }

def build_add_task_modal(sprint_num: int) -> Dict[str, Any]:
    """Generates the modal to add a brand-new sprint task dynamically."""
    return {
        "type": "modal",
        "callback_id": "submit_add_task_callback",
        "private_metadata": json.dumps({"sprint": sprint_num}),
        "title": {"type": "plain_text", "text": "Add New Sprint Task", "emoji": True},
        "submit": {"type": "plain_text", "text": "Add Task", "emoji": True},
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "blocks": [
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Add a new deliverable to **Sprint {sprint_num}**. It will immediately be assigned and synced to the markdown file and Excel tracker."}
            },
            {"type": "divider"},
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
                "label": {"type": "plain_text", "text": "Task Owner"}
            },
            {
                "type": "input",
                "block_id": "add_comp_block",
                "element": {
                    "type": "static_select",
                    "action_id": "select_add_comp",
                    "options": [
                        {"text": {"type": "plain_text", "text": "📦 C1: Market, Intake & Client POCs"}, "value": "1"},
                        {"text": {"type": "plain_text", "text": "📦 C2: Product, In-House LMS & Demos"}, "value": "2"},
                        {"text": {"type": "plain_text", "text": "📦 C3: Cloud, Cost & Internal Automation"}, "value": "3"},
                        {"text": {"type": "plain_text", "text": "📦 C4: Leadership, Compute & Enablers"}, "value": "4"}
                    ],
                    "initial_option": {"text": {"type": "plain_text", "text": "📦 C2: Product, In-House LMS & Demos"}, "value": "2"}
                },
                "label": {"type": "plain_text", "text": "Compartment"}
            },
            {
                "type": "input",
                "block_id": "add_title_block",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "add_title_input",
                    "placeholder": {"type": "plain_text", "text": "e.g. Document Sales Suite setup & research plan"}
                },
                "label": {"type": "plain_text", "text": "Task Title / Description"}
            },
            {
                "type": "input",
                "block_id": "add_outcome_block",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "add_outcome_input",
                    "placeholder": {"type": "plain_text", "text": "e.g. Architecture document ready for review"}
                },
                "label": {"type": "plain_text", "text": "Expected Outcome"}
            },
            {
                "type": "input",
                "block_id": "add_date_block",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "add_date_input",
                    "placeholder": {"type": "plain_text", "text": "Fri, Sept 4 (Day 4)"}
                },
                "label": {"type": "plain_text", "text": "Target Deadline"}
            }
        ]
    }

def build_deprioritize_modal(sprint_num: int, all_tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Generates the modal to de-prioritize or defer an active task."""
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
                "type": "section",
                "text": {"type": "mrkdwn", "text": "Select a task discussed in standup to mark as **De-prioritised / Deferred**."}
            },
            {"type": "divider"},
            {
                "type": "input",
                "block_id": "deprioritize_task_block",
                "element": {
                    "type": "static_select",
                    "action_id": "select_deprioritize_task",
                    "options": task_options[:100],
                    "placeholder": {"type": "plain_text", "text": "Select task to defer"}
                },
                "label": {"type": "plain_text", "text": "Select Task"}
            },
            {
                "type": "input",
                "block_id": "deprioritize_reason_block",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "deprioritize_reason_input",
                    "placeholder": {"type": "plain_text", "text": "e.g. Scope deferred to Month 2 engineering backlog"}
                },
                "label": {"type": "plain_text", "text": "Reason for De-prioritisation"}
            }
        ]
    }

def build_pre_standup_digest_card(day: int, sprint_num: int, all_tasks: List[Dict[str, Any]], meet_url: str) -> Dict[str, Any]:
    """Generates the 7:45 PM Pre-Standup Card in #all-mas-ai-labs."""
    done_tasks = [t for t in all_tasks if "done" in t["status"].lower() or "[x]" in t["status"]]
    in_progress = [t for t in all_tasks if "in progress" in t["status"].lower() or "[-]" in t["status"]]
    blocked_tasks = [t for t in all_tasks if (t["blocker"] and t["blocker"].lower() != "none" and t["blocker"] != "-") or "[!]" in t["status"]]

    owner_groups = {}
    for t in all_tasks:
        owner_groups.setdefault(t["owner"], []).append(t)

    owner_summary_blocks = []
    for owner, tasks in owner_groups.items():
        task_lines = []
        for t in tasks:
            status_emoji = "✅" if ("done" in t["status"].lower() or "[x]" in t["status"]) else ("🚨" if ("[!]" in t["status"] or t["rag"] == "🔴") else "⏳")
            task_lines.append(f"   {status_emoji} *`{t['id']}`*: {t['task']} `[{t['status']}]`")
        owner_summary_blocks.append(f"*👤 {owner}:*\n" + "\n".join(task_lines))

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"📊 MAS AI Labs — Standup Summary (Sprint {sprint_num} | Day {day})",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    f"📞 *Google Meet Standup starts at 8:00 PM IST (in 15 mins)*\n"
                    f"• *Sprint Progress:* `{len(done_tasks)}/{len(all_tasks)} completed` | "
                    f"`{len(in_progress)} in progress` | `{len(blocked_tasks)} blocked`"
                )
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*📋 Pod Deliverables & Live Status:*\n\n" + "\n\n".join(owner_summary_blocks)
            }
        }
    ]

    if blocked_tasks:
        blocker_text = []
        for t in blocked_tasks:
            blocker_text.append(f"• 🚨 *`{t['id']}` ({t['owner']})*: {t['task']}\n   ↳ *Blocker:* _{t['blocker']}_")
        blocks.extend([
            {"type": "divider"},
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*⚠️ Priority Items to Discuss & Unblock on Call:*\n" + "\n".join(blocker_text)
                }
            }
        ])

    blocks.extend([
        {"type": "divider"},
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "🟢 Join Google Meet (8:00 PM)", "emoji": True},
                    "url": meet_url or "https://meet.google.com/iek-smrh-zgg?authuser=0&hl=en_GB",
                    "style": "primary",
                    "action_id": "join_meet_button"
                },
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "📂 Open Sprint Plan", "emoji": True},
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
    Generates the high-signal, beautifully formatted Post-Standup Card in #all-mas-ai-labs:
    1. Person-by-Person Task Highlights & Discussions
    2. 🆕 New Tasks / Action Items Added from the Call
    3. 🎯 Agreed Decisions & Alignment
    4. 🚨 Active Blockers
    """
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"📝 MAS AI Labs — Post-Standup Highlights (Sprint {sprint_num} | Day {day})",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"✨ *Daily Standup Call Summary & Pod Alignments (Day {day})*"
            }
        },
        {"type": "divider"}
    ]

    # 1. Person-by-person task updates
    owner_sections = []
    for owner, bullets in owner_updates.items():
        if bullets:
            b_text = "\n".join([f"   {b}" for b in bullets])
            owner_sections.append(f"*👤 {owner}:*\n{b_text}")

    if owner_sections:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*📋 Updates & Discussions on Active Tasks:*\n\n" + "\n\n".join(owner_sections)
            }
        })

    # 2. 🆕 New tasks added from the call
    if new_tasks:
        new_bullets = "\n".join([f"• 🆕 {t}" for t in new_tasks])
        blocks.extend([
            {"type": "divider"},
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*✨ New Tasks & Action Items Added from Call:*\n" + new_bullets
                }
            }
        ])

    # 3. 🎯 Key decisions
    if call_decisions:
        decisions_bullets = "\n".join([f"• {d}" for d in call_decisions])
        blocks.extend([
            {"type": "divider"},
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*🎯 Key Decisions & Pod Alignment:*\n" + decisions_bullets
                }
            }
        ])

    # 4. 🚨 Blockers
    if blockers:
        blockers_bullets = "\n".join([f"• 🚨 {b}" for b in blockers])
        blocks.extend([
            {"type": "divider"},
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*⚠️ Active Blockers & Dependencies:*\n" + blockers_bullets
                }
            }
        ])

    blocks.extend([
        {"type": "divider"},
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"✅ Synced directly into `SPRINT_0{sprint_num}_WEEK_0{sprint_num}.md` and `MAS_AI_LABS_SPRINT_TRACKER.xlsx`."
                }
            ]
        }
    ])

    return {"blocks": blocks}
