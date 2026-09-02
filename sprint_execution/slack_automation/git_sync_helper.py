"""
MAS AI Labs — Automated Git Synchronizer
Author: MAS AI PM
Description: Automatically stages, commits, and pushes sprint file changes to GitHub
             whenever a task is updated, added, or de-prioritised from Slack.
"""

import os
import subprocess
import logging

logger = logging.getLogger("MAS_GitSync")

def auto_git_commit_and_push(commit_message: str):
    """Executes a non-blocking git add, commit, and push back to origin main."""
    try:
        repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        
        # Check if git is available
        subprocess.run(["git", "add", "sprint_execution/"], cwd=repo_dir, check=True, capture_output=True)
        
        result = subprocess.run(
            ["git", "commit", "-m", f"{commit_message} [skip ci]"],
            cwd=repo_dir,
            capture_output=True,
            text=True
        )
        
        if "nothing to commit" in result.stdout or "nothing to commit" in result.stderr:
            return
            
        push_res = subprocess.run(["git", "push", "origin", "main"], cwd=repo_dir, capture_output=True, text=True)
        if push_res.returncode == 0:
            logger.info(f"🚀 Auto-pushed sprint changes to GitHub: {commit_message}")
        else:
            logger.warning(f"Git push warning: {push_res.stderr}")
    except Exception as e:
        logger.error(f"Failed to auto-push to git: {e}")
