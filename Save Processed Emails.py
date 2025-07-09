def save_emails(user_id, emails):
    db = SessionLocal()
    for email in emails:
        db_email = Email(
            user_id=user_id,
            gmail_message_id=email['id'],
            sender=email['from'],
            recipient=email['to'],
            subject=email['subject'],
            snippet=email['snippet'],
            body=email['body'],
            received_date=email['date']
        )
        db.add(db_email)
    db.commit()