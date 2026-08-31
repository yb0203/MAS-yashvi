"""
MAS AI Labs — Slack Block Kit UI Views & Templates
Author: MAS AI PM
Description: Centralized UI library generating clean, modern Slack Block Kit
             cards for Personal DMs, Modals, Channel Digests, and Gemini Day Highlights.
"""

import json
from typing import Dict, Any, List

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
                    f"Please take *30–45 seconds* to update your scheduled deliverable(s) below:"
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
                        "text": "⚡ Quick Update (< 45s)",
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
    """Generates the single-screen consolidated modal listing all assigned tasks for today."""
    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"Quickly update your tasks for **Day {day}** below. Select status and health, and add any blocker note."
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
                "label": {"type": "plain_text", "text": f"Status ({t['id']})"}
            },
            {
                "type": "input",
                "block_id": f"rag_{t['id']}",
                "element": {
                    "type": "static_select",
                    "action_id": f"select_rag_{t['id']}",
                    "options": [
                        {"text": {"type": "plain_text", "text": "🟢 Green (On Track)"}, "value": "🟢"},
                        {"text": {"type": "plain_text", "text": "🟡 Amber (At Risk)"}, "value": "🟡"},
                        {"text": {"type": "plain_text", "text": "🔴 Red (Blocked)"}, "value": "🔴"}
                    ],
                    "initial_option": {"text": {"type": "plain_text", "text": "🟢 Green (On Track)"}, "value": "🟢"}
                },
                "label": {"type": "plain_text", "text": f"RAG ({t['id']})"}
            },
            {"type": "divider"}
        ])

    blocks.extend([
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
            "label": {"type": "plain_text", "text": "Blocker / Delay Reason (If any)"}
        }
    ])

    return {
        "type": "modal",
        "callback_id": "submit_consolidated_standup_callback",
        "private_metadata": json.dumps({"owner": owner_name, "sprint": sprint_num, "day": day, "task_ids": [t["id"] for t in tasks]}),
        "title": {"type": "plain_text", "text": "Daily Standup Update", "emoji": True},
        "submit": {"type": "plain_text", "text": "Submit Update", "emoji": True},
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "blocks": blocks
    }

def build_pre_standup_digest_card(day: int, sprint_num: int, total_tasks: int, done_count: int, blocked_tasks: List[Dict[str, Any]], meet_url: str) -> Dict[str, Any]:
    """Generates the 7:45 PM summary card for #all-mas-ai-labs."""
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"📊 Standup Digest (Sprint {sprint_num} | Day {day})",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    f"📞 *Google Meet Standup starts at 8:00 PM IST (in 15 mins)*\n"
                    f"• *Progress Today:* `{done_count}/{total_tasks} tasks completed`\n"
                    f"• *Active Blockers Flagged:* `{len(blocked_tasks)}`"
                )
            }
        },
        {"type": "divider"}
    ]

    if blocked_tasks:
        blocker_text = []
        for t in blocked_tasks:
            blocker_text.append(f"🚨 *`{t['id']}` ({t['owner']})*: {t['task']}\n   ↳ *Blocker:* _{t['blocker']}_")
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*⚠️ Priority Items to Discuss & Unblock on Call:*\n" + "\n".join(blocker_text)
            }
        })
    else:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "🎉 *Zero Blockers Logged!* All active deliverables on track."
            }
        })

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
    """Generates the 8:25 PM Post-Standup Day Highlights card."""
    return {
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f"📝 Post-Standup Highlights & Decisions (Day {day})",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"✨ *Key Standup Takeaways (Powered by Google Meet Gemini Notes):*\n\n{highlight_text}"
                }
            },
            {"type": "divider"},
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"✅ Synced directly into `SPRINT_0{sprint_num}_WEEK_0{sprint_num}.md` Daily Log."
                    }
                ]
            }
        ]
    }
