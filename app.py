import streamlit as st
import io
import sys
import threading
from crewai import Crew, Process
from credentials import SENDERS_EMAIL, RECIEVERS_EMAIL, APP_PASSWORD
from datetime import datetime
from agents import create_researcher, create_generator, create_reviewer
from tasks import research_task, email_generation_task, email_review_task
from monitor import fetch_latest_emails
from sendmail import send_email

"""Streamlit Web Application for Automated Email Workflow with AI and Email Sending and Monitoring"""

st.title("Automated Email Workflow with AI and Email Sending and Monitoring")

# Initialize session state to store generated email body, log output, and email replies
if "generated_email_body" not in st.session_state:
    st.session_state["generated_email_body"] = ""
if "log_output" not in st.session_state:
    st.session_state["log_output"] = ""
if "email_replies" not in st.session_state:
    st.session_state["email_replies"] = []

prospect = st.text_input("Enter Prospect Name")
company = st.text_input("Enter Company Name")
products = st.text_input("Products Information")
your_name = st.text_input("Your Name")
your_company = st.text_input("Your Company")
date = str(datetime.now().date())

"""Capturing Multi-Agent System Logs on how each agent is performing the task"""
log_capture_string = io.StringIO()
sys.stdout = log_capture_string  
api_key=True

#"""Module to generate Email Content using Multi-Agent System using CrewAI and kick-off the process of executing crews """
if st.button("Generate Email"):
    if api_key:
        crew = Crew(
            agents=[create_researcher(), create_generator(), create_reviewer()],
            tasks=[research_task(), email_generation_task(), email_review_task()],
            process=Process.sequential
        )
        result = crew.kickoff(inputs={"prospect": prospect, "company": company, "date": date, "products": products, "your_name":your_name, "your_company": your_company })
        
        st.session_state["generated_email_body"] = result  # Store the generated email body in session state
        st.success("Email content generated:")
        st.write(st.session_state["generated_email_body"])
        
        st.session_state["log_output"] = log_capture_string.getvalue()
    else:
        st.error("API Key is required to generate email content.")

st.subheader("Multi Agent System Logs")
st.text_area("Logs", value=st.session_state["log_output"], height=300)

"""Module to Send Email using the generated email content"""
st.subheader("Send Email")
sender_email = st.text_input("Sender Email", value=SENDERS_EMAIL)
receiver_email = st.text_input("Recipient Email", value=RECIEVERS_EMAIL)
subject = st.text_input("Email Subject", value="Regarding Sales")  
body = st.text_area("Email Body", value=st.session_state["generated_email_body"], height=200)  
password = st.text_input("Sender Email Password", value=APP_PASSWORD, type="password")

if st.button("Send Email"):
    # Use the generated email body stored in session state
    if st.session_state["generated_email_body"] or body:
        # Call the email sending function
        status = send_email(
            sender_email=sender_email,
            receiver_email=receiver_email,
            subject=subject,
            body=body,
            login=sender_email,
            password=password
        )
        st.write(status)
    else:
        st.error("No email body to send. Please generate the email first.")
replies =[]

if st.button("Check for New Emails"):
    replies = fetch_latest_emails(sender_email, password, receiver_email)


sys.stdout = sys.__stdout__

check_thread = threading.Thread(target=fetch_latest_emails, args=(sender_email, password,receiver_email), daemon=True)
check_thread.start()
