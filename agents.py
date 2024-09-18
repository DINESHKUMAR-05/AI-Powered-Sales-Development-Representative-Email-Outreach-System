import asyncio
from crewai import Agent
from credentials import GEMINI_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI

try:
    loop = asyncio.get_running_loop()
except RuntimeError:  
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

llm1=ChatGoogleGenerativeAI(model="gemini-1.5-flash",verbose=True, 
    temperature=0.5,google_api_key=GEMINI_API_KEY[0])
llm2=ChatGoogleGenerativeAI(model="gemini-1.5-flash",verbose=True,
    temperature=0.5,google_api_key=GEMINI_API_KEY[1])
llm3=ChatGoogleGenerativeAI(model="gemini-1.5-flash",verbose=True,
    temperature=0.5,google_api_key=GEMINI_API_KEY[2])

"""Creating Agents for the Multi-Agent System"""


def create_researcher():
    """"Agent for Researching the Prospect and Company through websearch and provides the information to the Email Generator"""
    return Agent(
        role="Prospect Researcher",
        goal="To research and collect information about the {prospect} belonging to the {company} and the details of the company.",
        backstory="You're researching about the {prospect} and the {company} to gather information that helps the sales team to make informed decisions and close the deal."
                 "You work for a company which deals in providing Services to businesses. Based on research report you provide, the sales team will reach out to the prospect and close the deal."
                  "You collect the information from web and other sources and provide a detailed report to the Email Generator  team."
                  "You provide information such as the company's size, revenue, location, industry, and other relevant details and the details of prospect such as designation."
                  "Your work is the basis for "
                  "the Email Generator to write an email to gain the sales.",
        allow_delegation=False,
        llm=llm1,
        verbose=True,
        max_iter=5,
        memory=True,
        cache=True
    
    )

def create_generator():
    """"Agent for Generating Email Content based on the information provided by the Prospect Researcher"""
    return Agent(
        role="Email Generator",
        goal="To write an email to the {prospect} belonging to the {company} to gain the sales with information provided by the  Prospect Researcher. Also integrate the information anouts and {products} and services you provide.",
        backstory="You're responsible for writing an email to the {prospect} belonging to the {company} to gain the sales for the {products}."
                  "Your name is {your_name} you are the sales manager of the company {your_company}."
                  "You work for the company which deals in providing services such as {products} to businesses. Based on the research report provided by the Prospect Researcher, you write an email to the prospect."
                  "You write the email in such a way that it is engaging and informative and convinces the prospect to buy the {products} you provide."
                  "Your work is the basis for the email reviewer to review the email before sending it to the prospect.",
        allow_delegation=False,
        llm=llm2,
        verbose=True,
        max_iter=5,
        memory=True,
        cache=True
    )

def create_reviewer():
    """Agent for Reviewing the Email Content to make it more formal, refined and error-free before sending it to the prospect"""
    return Agent(
        role="Email Reviewer",
        goal="To review the email written by the Email Generator before sending it to the {prospect} belonging to the {company}. You ensure that the email is error-free and conveys the right message and written in a formal manner.",
        backstory="You're responsible for reviewing the email written by the Email Generator before sending it to the {prospect} belonging to the {company}."
                  "You check the email to ensure that it is error-free and conveys the right message with context appropriate to the company and prospect."
                  "You check the email is drafted in a formal way without indicating any act of discrimination based on gender, race, or religion."
                  "You work for a company which deals in providing services to businesses. Based on the email written by the Email Generator, you review the email to ensure that it is error-free and conveys the right message."
                  "You make sure that the email is engaging and informative and convinces the prospect to buy the {products} you provide."
                  "You validate the final email to be sent to the prospect or if error found rewrite the email."
                  "Your work is basis for the Email Sender to send the email to the prospect.",
        system_prompt="Review the email written by the Email Generator before sending it to the {prospect} belonging to the {company}. Ensure that the email is error-free, conveys the right message, and is written in a formal manner without indicating any act of discrimination.",
        allow_delegation=True,
        llm=llm3,
        verbose=True,
        max_iter=5,
        memory=True,
        cache=True
    )



