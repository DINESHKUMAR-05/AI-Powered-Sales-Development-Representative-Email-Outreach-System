import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

"""Function to send email using SMTP protocol"""

def send_email(sender_email: str, receiver_email: str, subject: str, body: str, login: str, password: str):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        return "Email sent successfully!"
    except Exception as e:
        return f"Failed to send email. Error: {e}"


