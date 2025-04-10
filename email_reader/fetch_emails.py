import requests
from google.oauth2.credentials import Credentials

def get_unread_emails(access_token):
    creds = Credentials(token=access_token)

    headers = {
        "Authorization": f"Bearer {creds.token}",
        "Accept": "application/json"
    }

    # Gmail API to list unread messages
    response = requests.get(
        "https://gmail.googleapis.com/gmail/v1/users/me/messages?q=is:unread",
        headers=headers
    )

    if response.status_code == 200:
        messages = response.json().get("messages", [])
        return messages
    else:
        return {"error": "Failed to fetch emails", "details": response.text}

