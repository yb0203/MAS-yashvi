"""
MAS AI Labs — Slack Block Kit UI Views & Templates
Author: MAS AI PM
Description: Centralized UI library generating clean, modern Slack Block Kit
             cards for Personal DMs, Modals, Channel Digests, and Gemini Day Highlights.
             - Automated Status -> RAG mapping (Zero redundant dropdowns for teammates).
             - Structured "Planned vs Done" standup cards.
"""

import json
from typing import Dict, Any, List

def map_status_to_rag(status: str, has_blocker: bool = False) -> str:
    """Automatically maps task status to RAG indicator to eliminate manual dropdowns."""
    s_lower = status.lower()
    if "blocked" in s_lower or "[!]" in s_lower or has_blocker:
        return "🔴"
    elif "done" in s_lower or "[x]" in s_lower:
        return "🟢"
    else:
        return "🟢"

def build_personal_dm_view(owner_name: str, tasks: List[Dict[str, Any]], day: int, sprint_num: int) -> List[Dict[str, Any]]:
    """Builds a compact, personalized 1-screen DM view for task owners."""
    task_bullets = []
    for t in tasks:
        task_bullets.append(
            f"• *`{t['id']}`*: {t['task']}\n"
            f"   ↳ *Target:* _{t['expected_outcome']}_\n"
            f"   ↳ *Status:* `{t['status']}` | *RAG:* {t['rag']}"
        )

    return [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"👋 Hey {owner_name}! Daily Standup Quick Update (Day {day})",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    f"⏰ *Standup Call is at 8:00 PM IST.*\n"
                    f"Please take *20–30 seconds* to update your status below:"
                )
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*📌 Your Scheduled Deliverables Today:*\n" + "\n".join(task_bullets)
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
                        "text": "⚡ Quick Update (< 30s)",
                        "emoji": True
                    },
                    "style": "primary",
                    "value": json.dumps({"owner": owner_name, "sprint": sprint_num, "day": day}),
                    "action_id": "open_consolidated_modal_action"
                }
            ]
        }
    ]

def build_consolidated_update_modal(owner_name: str, tasks: List[Dict[str, Any]], sprint_num: int, day: int) -> Dict[str, Any]:
    """
    Generates the simplified single-screen modal:
    - Teammate selects ONLY the Status dropdown (RAG is mapped automatically).
    - Optional PR/outcome link and blocker notes.
    """
    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"Select status for your tasks today (**Day {day}**). RAG health is calculated automatically."
            }
        },
        {"type": "divider"}
    ]

    for t in tasks:
        blocks.extend([
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*`{t['id']}`*: {t['task']}"
                }
            },
            {
                "type": "input",
                "block_id": f"status_{t['id']}",
                "element": {
                    "type": "static_select",
                    "action_id": f"select_status_{t['id']}",
                    "options": [
                        {"text": {"type": "plain_text", "text": "✅ Done / Completed"}, "value": "[x] Done"},
                        {"text": {"type": "plain_text", "text": "⏳ In Progress"}, "value": "[-] In Progress"},
                        {"text": {"type": "plain_text", "text": "🚨 Blocked / Delayed"}, "value": "[!] Blocked"}
                    ],
                    "initial_option": {"text": {"type": "plain_text", "text": "⏳ In Progress"}, "value": "[-] In Progress"}
                },
                "label": {"type": "plain_text", "text": f"Status for {t['id']}"}
            }
        ])

    blocks.extend([
        {"type": "divider"},
        {
            "type": "input",
            "block_id": "deliverable_link_block",
            "optional": True,
            "element": {
                "type": "plain_text_input",
                "action_id": "deliverable_link_input",
                "placeholder": {"type": "plain_text", "text": "PR # / Doc link / Quick output summary"}
            },
            "label": {"type": "plain_text", "text": "Completed Output / PR Link"}
        },
        {
            "type": "input",
            "block_id": "blocker_notes_block",
            "optional": True,
            "element": {
                "type": "plain_text_input",
                "action_id": "blocker_notes_input",
                "placeholder": {"type": "plain_text", "text": "None / Waiting for API key / Dependency"}
            },
            "label": {"type": "plain_text", "text": "Blocker / Dependency (If any)"}
        }
    ])

    return {
        "type": "modal",
        "callback_id": "submit_consolidated_standup_callback",
        "private_metadata": json.dumps({"owner": owner_name, "sprint": sprint_num, "day": day, "task_ids": [t["id"] for t in tasks]}),
        "title": {"type": "plain_text", "text": "Daily Standup Update", "emoji": True},
        "submit": {"type": "plain_text", "text": "Submit", "emoji": True},
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "blocks": blocks
    }

def build_pre_standup_digest_card(day: int, sprint_num: int, all_tasks: List[Dict[str, Any]], meet_url: str) -> Dict[str, Any]:
    """
    Generates the comprehensive 7:45 PM Pre-Standup Card in #all-mas-ai-labs:
    - Displays all active tasks across all teammates (Yashvi, Prakhar, Shubham, Rohan, Gaurav).
    - Highlights Done, In Progress, and Blocked items.
    """
    done_tasks = [t for t in all_tasks if "done" in t["status"].lower() or "[x]" in t["status"]]
    in_progress = [t for t in all_tasks if "in progress" in t["status"].lower() or "[-]" in t["status"]]
    blocked_tasks = [t for t in all_tasks if (t["blocker"] and t["blocker"].lower() != "none" and t["blocker"] != "-") or "[!]" in t["status"]]

    # Group all tasks by Owner
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
                    "url": meet_url or "https://meet.google.com",
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

def build_post_standup_gemini_card(day: int, sprint_num: int, highlight_text: str) -> Dict[str, Any]:
    """Generates the structured 8:25 PM Post-Standup Day Highlights card."""
    return {
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f"📝 Post-Standup Day Highlights (Sprint {sprint_num} | Day {day})",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"✨ *Finalized Decisions & Action Items (Google Meet Gemini Notes):*\n\n{highlight_text}"
                }
            },
            {"type": "divider"},
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"✅ Daily record updated in `SPRINT_0{sprint_num}_WEEK_0{sprint_num}.md` and `MONTH_01_MASTER_PLAN.md`."
                    }
                ]
            }
        ]
    }
