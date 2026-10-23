
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Read-only permission for Gmail
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def main():
    creds = None

    # Load previously saved login token
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file(
            "token.json", SCOPES
        )

    # Sign in or refresh authorization
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    # Connect to Gmail API
    service = build("gmail", "v1", credentials=creds)

    # Display connected Gmail account
    profile = service.users().getProfile(
        userId="me"
    ).execute()

    print("Gmail connected successfully!")
    print("Account:", profile["emailAddress"])

    # Get the latest 10 emails
    results = service.users().messages().list(
        userId="me",
        maxResults=10
    ).execute()

    messages = results.get("messages", [])

    print("\nLatest emails:\n")

    if not messages:
        print("No emails found.")
        return

    # Display sender and subject
    for message in messages:
        email_data = service.users().messages().get(
            userId="me",
            id=message["id"],
            format="metadata",
            metadataHeaders=["Subject", "From"]
        ).execute()

        headers = email_data.get("payload", {}).get(
            "headers", []
        )

        header_dict = {
            h["name"]: h["value"] for h in headers
        }

        print("From:", header_dict.get("From", "Unknown"))
        print("Subject:", header_dict.get("Subject", "No subject"))
        print("-" * 40)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("Error:", error)
