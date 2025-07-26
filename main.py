import base64
from email.message import EmailMessage
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
# run it on 3.12.4 py ver

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def gmail_authenticate():
    creds = None
    if os.path.exists('token.json'):
        from google.oauth2.credentials import Credentials
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            from google.auth.transport.requests import Request
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token_file:
            token_file.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def send_email(service, sender, to, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['To'] = to
    msg['From'] = sender
    msg['Subject'] = subject

    encoded_msg = base64.urlsafe_b64encode(msg.as_bytes()).decode()

    send_message = service.users().messages().send(
        userId='me',
        body={'raw': encoded_msg}
    ).execute()
    print(f"✅ Email sent to {to} with Message ID: {send_message['id']}")

def main():
    service = gmail_authenticate()

    with open("./Input/Names/invited_names.txt") as names_file:
        lines = names_file.readlines()

    with open("./Input/Letters/starting_letter.txt") as letter_file:
        letter_contents = letter_file.read()

    your_email = "catsadogga@gmail.com"  # Replace with your Gmail address

    for line in lines:
        name, email = line.strip().split(",")  # Split line by comma
        personalized_letter = letter_contents.replace("[name]", name)

        send_email(
            service=service,
            sender=your_email,
            to=email,
            subject="You're Invited! To My Party.",
            body=personalized_letter
        )

if __name__ == "__main__":
    main()


# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


# 1. credentials.json (OAuth 2.0 Client Credentials)
# This file is downloaded from the Google Cloud Console and 
# contains your app's OAuth 2.0 client ID and client secret. 
# It is required for the first-time authentication process.


# 2. token.json (OAuth 2.0 User Token)
# This file is generated automatically after the first successful 
# OAuth authorization. It stores the user's access and refresh tokens, 
# so they don’t have to log in again.

# 3.
# OAuth lets your app securely access a user's account 
# on another service (like Gmail) without asking for their password.