# AI-Driven Email Outreach Automation System

## Project Overview
This project aims to develop an AI-driven system that automates and enhances the email outreach process for Sales Development Representatives (SDRs). The system focuses on researching prospects, generating personalized emails, and ensuring adherence to best practices.

The core functionalities include:
- **Prospect research** using web search tools.
- **Personalized email generation** based on researched data.
- **Automated email sending** and response monitoring.
- **Multi-agent system** to manage different tasks like research, email generation, and sending.
- **Adherence to email best practices** to maximize engagement.

We used **CrewAI framework** for building the multi-agent system and **Gemini Language Model (LLM)** for generating personalized emails.

---

## Folder Structure

The project files are structured as follows:

### 1. `requirements.txt`
Contains the necessary libraries to run the project. Install these dependencies by running:
```
pip install -r requirements.txt
```

### 2. `app.py`
This file contains the **Streamlit** code to run the system. It serves as the main entry point to kick off the multi-agent system and provides the interface for sending and monitoring emails. Run the app using the following command:
```
streamlit run app.py
```

### 3. `agents.py`
Defines the **agents** in the multi-agent system, their roles, and the specific prompts they use. Agents handle tasks such as prospect research, email generation, and ensuring best practices.

### 4. `tasks.py`
Defines the **tasks** that each agent performs. It contains the specific prompts and logic required for each agent to function efficiently in the email outreach process.

### 5. `tools.py`
Includes the tools used by the agents, such as **DuckDuckGo** for prospect research and web search functionality.

### 6. `sendmail.py`
This file contains the **SMTP** logic to automate the process of sending emails. It utilizes Gmail's SMTP server to send personalized emails generated by the system.

### 7. `monitor.py`
Monitors email replies from a specific mail ID using threads. It keeps track of responses and enables the system to act accordingly (e.g., sending follow-ups).

### 8. `credentials.py`
Contains sensitive credentials:
- **Gemini LLM API key**.
- **Gmail app password** for SMTP access.
- **Sender's and receiver's email IDs**.

To obtain the API key for **Gemini**, visit [Google AI Studios](https://aistudios.google.com), and for Gmail app passwords, visit [Google Account Settings](https://myaccount.google.com).

---

## Important Notes

### Gemini API Usage
We used **Gemini LLM** to generate personalized email content. As the free version of Gemini allows only a limited number of API requests (2 requests per minute), we generated API keys from three different accounts to handle multiple API calls simultaneously and improve the overall performance of the system.

### Multi-Agent System
The multi-agent system is built using the **CrewAI** framework. Each agent in the system is responsible for a different aspect of the email outreach process, from researching prospects to composing and sending emails.

---

## How to Run the Project

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Enter the credentials in credentials.py file for 
   - Gemini API Key
   - App Password for mail access
   - mail id for sender and reciever
     
3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
4. Use the web interface to interact with the system, assign tasks to agents, send emails, and monitor replies.

---

## Author
Developed by Dineshkumar S.
