import imaplib
import email
from email.header import decode_header
import time
import streamlit as st

"""Module to Fetch Latest Emails from the Reciever Email Account using IMAP Protocol"""

def decode_header_value(value):
    decoded_bytes, encoding = decode_header(value)[0]
    if isinstance(decoded_bytes, bytes):
        return decoded_bytes.decode(encoding if encoding else 'utf-8')
    return decoded_bytes

"""Function to fetch the latest emails from the reciever email account only captures the replies from particular email address"""
def fetch_latest_emails(sender_email, app_password, recievers_email, num_emails=3):
    try:
        time.sleep(60)
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(sender_email, app_password)  # Use an App Password if 2FA is enabled
        mail.select('inbox')
        status, data = mail.search(None, f'FROM {recievers_email}')
        email_ids = data[0].split()
        latest_email_ids = email_ids[-num_emails:]  # Get the last `num_emails` IDs
        replies = []
        for email_id in latest_email_ids:
            status, data = mail.fetch(email_id, '(RFC822)')
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            subject = decode_header_value(msg.get("Subject", ""))
            sender = decode_header_value(msg.get("From", ""))
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                        replies.append(body)
                        break
            else:
                body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
        replies = [body.split('\r')[0] for body in replies]
        mail.logout()
        st.subheader("Latest Replies")
        if replies:
            for i,reply in enumerate(replies):
                st.code(f"Reply {i+1}: {reply}")

    except Exception as e:
        print(f"An error occurred: {e}")

