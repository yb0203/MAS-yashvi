/**
 * Google Apps Script — Automated Google Meet Gemini Notes to Slack Sync
 * Trigger: Runs daily at 10:00 PM IST (or on-demand)
 * Target Slack Channel: #all-mas-ai-labs (C0B2NHS5ZH6)
 */

// Configuration
const SLACK_BOT_TOKEN = "xoxb-YOUR_SLACK_BOT_TOKEN_HERE"; // Or use Slack Webhook URL
const SLACK_CHANNEL_ID = "C0B2NHS5ZH6"; // #all-mas-ai-labs
const SLACK_WEBHOOK_URL = ""; // Optional: if using Incoming Webhook instead of Token

function syncGoogleMeetNotesToSlack() {
  const today = new Date();
  const dateQuery = Utilities.formatDate(today, "Asia/Kolkata", "yyyy/MM/dd");
  
  // Search Gmail for today's Google Meet Gemini summary email
  const searchQuery = `subject:"Notes: 'MAS AI Labs Daily Scrum'" after:${dateQuery}`;
  const threads = GmailApp.search(searchQuery, 0, 1);

  if (threads.length === 0) {
    Logger.log("No Google Meet Gemini notes email found for today.");
    return;
  }

  const messages = threads[0].getMessages();
  const latestMessage = messages[messages.length - 1];
  const emailSubject = latestMessage.getSubject();
  const emailBody = latestMessage.getPlainBody();

  Logger.log("Found Email: " + emailSubject);

  // Send to Slack via Web API or Webhook
  if (SLACK_BOT_TOKEN && SLACK_BOT_TOKEN.startsWith("xoxb-")) {
    postToSlackViaBotToken(emailSubject, emailBody);
  } else if (SLACK_WEBHOOK_URL) {
    postToSlackViaWebhook(emailSubject, emailBody);
  } else {
    Logger.log("Error: Neither SLACK_BOT_TOKEN nor SLACK_WEBHOOK_URL configured.");
  }
}

function postToSlackViaBotToken(subject, body) {
  const url = "https://slack.com/api/chat.postMessage";
  const payload = {
    channel: SLACK_CHANNEL_ID,
    text: `📝 *${subject}*\n\n` + cleanEmailBody(body)
  };

  const options = {
    method: "post",
    contentType: "application/json; charset=utf-8",
    headers: {
      "Authorization": "Bearer " + SLACK_BOT_TOKEN
    },
    payload: JSON.stringify(payload),
    muteHttpExceptions: true
  };

  const response = UrlFetchApp.fetch(url, options);
  Logger.log("Slack API Response: " + response.getContentText());
}

function postToSlackViaWebhook(subject, body) {
  const payload = {
    text: `📝 *${subject}*\n\n` + cleanEmailBody(body)
  };

  const options = {
    method: "post",
    contentType: "application/json; charset=utf-8",
    payload: JSON.stringify(payload),
    muteHttpExceptions: true
  };

  const response = UrlFetchApp.fetch(SLACK_WEBHOOK_URL, options);
  Logger.log("Slack Webhook Response: " + response.getContentText());
}

function cleanEmailBody(rawBody) {
  // Strip Google Workspace footer metadata
  const lines = rawBody.split("\n");
  const filtered = lines.filter(line => {
    const l = line.toLowerCase();
    return !l.includes("attachments [") && 
           !l.includes("meeting records [") && 
           !l.includes("invited [") && 
           !l.includes("how is the quality");
  });
  return filtered.join("\n").trim();
}
