# ☁️ MAS AI Labs — GCP Deployment Guide for Slack Standup Bot

This guide provides the complete, production-grade instructions for deploying the **MAS Slack Standup Bot & Sprint Sync Engine** onto **Google Cloud Platform (GCP)**.

---

## 🎯 Architecture Summary

* **Protocol**: Slack Socket Mode (`WebSocket` outbound).
* **Ports Required**: **None (0 incoming ports)**. No public IP or domain name required.
* **Storage**: Persistent disk syncing markdown files (`SPRINT_0X_WEEK_0X.md`), `sprint_tasks.csv`, and Excel tracker (`MAS_AI_LABS_SPRINT_TRACKER.xlsx`).
* **Auto-Git Sync**: Automatically commits and pushes all sprint changes to `yb0203/MAS-yashvi.git`.

---

## 🚀 Option 1: GCP Compute Engine VM (Recommended — Always Free Tier)

This is the fastest, zero-cost method using GCP's **Always Free `e2-micro`** instance in `us-central1` or any standard micro VM.

### Step 1: Create VM on GCP
1. Go to **[GCP Console](https://console.cloud.google.com/)** $\rightarrow$ **Compute Engine** $\rightarrow$ **VM instances** $\rightarrow$ **Create Instance**.
2. Settings:
   * **Name**: `mas-standup-bot`
   * **Region**: `us-central1` (or `asia-south1` Mumbai)
   * **Machine configuration**: `E2` $\rightarrow$ `e2-micro` (2 vCPU, 1 GB memory)
   * **Boot disk**: Ubuntu 22.04 LTS or 24.04 LTS (10 GB Standard Disk)
3. Click **Create**.

---

### Step 2: SSH into VM & Clone Repo
Click **SSH** next to your VM and run:

```bash
# 1. Update packages and install Python & Git
sudo apt-get update && sudo apt-get install -y python3-pip python3-venv git

# 2. Clone repository
git clone https://github.com/yb0203/MAS-yashvi.git
cd MAS-yashvi

# 3. Create virtual environment & install dependencies
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r sprint_execution/slack_automation/requirements.txt
```

---

### Step 3: Configure Environment Variables
Copy `.env.example` to `.env` and configure your tokens:

```bash
cp sprint_execution/slack_automation/.env.example sprint_execution/slack_automation/.env
nano sprint_execution/slack_automation/.env
```

Ensure the following are set:
```bash
SLACK_BOT_TOKEN="xoxb-YOUR-SLACK-BOT-TOKEN"
SLACK_APP_TOKEN="xapp-YOUR-SLACK-APP-TOKEN"
SLACK_STANDUP_CHANNEL="C0B2NHS5ZH6"
GOOGLE_MEET_URL="https://meet.google.com/iek-smrh-zgg?authuser=0&hl=en_GB"

# Teammates Slack IDs
SLACK_ID_YASHVI="U0BRJ6L8ASJ"
SLACK_ID_PRAKHAR="U0BFMKFTWTH"
SLACK_ID_SHUBHAM="U0BD1GVPEDD"
SLACK_ID_GAURAV="U0B276EJLUR"
SLACK_ID_ROHAN="U0BD10ZGWD6"
```

---

### Step 4: Enable Systemd Service (24/7 Background Daemon)
Copy the service unit file and start it:

```bash
sudo cp sprint_execution/slack_automation/mas-standup.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now mas-standup.service
```

Check status and live logs:
```bash
sudo systemctl status mas-standup.service
journalctl -u mas-standup.service -f
```

---

## 🐳 Option 2: GCP Container / Docker VM

If you run Docker on GCP:

```bash
# Build Docker image
docker build -t mas-standup-bot:v1 -f sprint_execution/slack_automation/Dockerfile .

# Run container with restart policy
docker run -d \
  --name mas-standup \
  --restart unless-stopped \
  --env-file sprint_execution/slack_automation/.env \
  mas-standup-bot:v1
```

---

## 🛡️ Health Check & Maintenance

* **Check Bot Connection**: In Slack, type `/standup` or send a DM to `MAS Standup`.
* **Restart Daemon**: `sudo systemctl restart mas-standup.service`
* **Stop Daemon**: `sudo systemctl stop mas-standup.service`
* **Auto-Restart on Reboot**: Enabled by default via `systemctl enable`.
