from crewai import Task
from agents import create_researcher, create_generator, create_reviewer
from tools import search_duckduckgo_cached

"""Creating Tasks for the Multi-Agent System"""

def research_task():
    """Task for Researching the Prospect and Company through websearch (DuckDuckGo)"""
    return Task(
        description=("Research about the {company} and the {prospect} to gather information to help the sales team to make informed decisions and close the deal."
                     "collect the information such as the company's size, revenue, location, industry, and other relevant details and the details of prospect such as designation."),
        expected_output="A detailed report about the company",
        agent=create_researcher(),
        tools =[search_duckduckgo_cached]
    )

def email_generation_task():
    """Task for Generating Email Content"""
    return Task(
        description=("Write an email to the prospect to gain the sales with information provided by the Prospect Researcher or to edit the mail based on suggestions from the Email Reviewer. The email should include elements that are engaging and informative and convinces the prospect to buy the {products}."),
        expected_output="An email that is engaging and informative and convinces the prospect to buy the {products}.",          
        agent=create_generator(),
    )

def email_review_task():
    """Task for Reviewing the Email Content"""
    return Task(
        description=("Review the email written by the Email Generator before sending it to the prospect. Ensure that the email is error-free, conveys the right message, and is written in a formal manner without indicating any act of discrimination based on race, gender, or religion."),
        expected_output="A reviewed email that is error-free, conveys the right message, and is written in a formal manner in the following format:"
                        "From: sales@{your_company}.com (in lowercase small letters)\n"
                        "To: [Prospect mail id] eg: {prospect}@{company}.com\n (in lowercase small letters)"
                        "Subject: [Subject of the mail]\n"
                        "Dear [Prospect Name],"
                        "[Mail Content]"
                        "\nSincerely,"
                        "\nAItoall Team"
                        "\nDate : {date}",
        agent=create_reviewer(),
    )

