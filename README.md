# 📧 Gmail Bulk Invitation Sender

A Python script to automatically send personalized invitation emails using the Gmail API. This tool reads recipient names and emails from a file and personalizes each message using a letter template.

## ✨ Features

- Sends customized emails using the Gmail API
- Reads recipient list from a `.txt` file (CSV-style)
- Inserts personalized names into a letter template
- Authenticates securely via OAuth2
- Designed for Python 3.12.4

## 🛠 Requirements

- Python 3.12.4
- Google Gmail API credentials (`credentials.json`)
- `token.json` (auto-generated after first authentication)
