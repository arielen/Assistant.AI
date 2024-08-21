from datetime import datetime
from textwrap import dedent

from crewai import Agent, Task, Crew
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from crewai_tools.tools.docx_search_tool.docx_search_tool import DOCXSearchTool
from crewai_tools.tools.pdf_search_tool.pdf_search_tool import PDFSearchTool
from crewai_tools.tools.scrape_element_from_website.scrape_element_from_website import ScrapeElementFromWebsiteTool
from crewai_tools.tools.website_search.website_search_tool import WebsiteSearchTool


def get_tools():
    return [
        SerperDevTool(),
        ScrapeElementFromWebsiteTool(),
        PDFSearchTool(),
        DOCXSearchTool(),
        WebsiteSearchTool(),
        ScrapeWebsiteTool()
    ]


def get_tip_section():
    return dedent(
        f"""
        Assistant.AI

        Make sure your answer is written in a formal or informal style depending on the context of the question.

        This task requires exceptionally precise and comprehensive execution, considering all observable universes and parallels.

        Consider today's date: {datetime.now().strftime('%d/%m/%Y')} and the urgency implicit in the demand when planning your response.

        Please take a deep breath before you start and use all your available tools to ensure the highest quality and relevance of the information.

        """
    )


def get_knowledge_agent():
    return Agent(
        role='Dynamic Knowledge Explorer',
        goal='Respond to the demand "{question}" using appropriate resources',
        memory=True,
        backstory=dedent("""
            As a Dynamic Knowledge Explorer, you adapt your strategies and tools 
            based on the nature of the query, ensuring that the answer is always accurate and relevant.
            """),
        tools=get_tools(),  # Starting with the default tools
        allow_delegation=False
    )


def get_answer_question_task(knowledge_agent):
    return Task(
        description=dedent(f"""
            {get_tip_section()}
            Aim to best meet the user's demand by combining internal data and up-to-date information from the internet.

            Demand:{{question}}

            """
        ),
        expected_output='An accurate and relevant answer based on the question asked.',
        agent=knowledge_agent,
        memory=True,
    )


def get_knowledge_crew(knowledge_agent, answer_question_task):
    return Crew(
        agents=[knowledge_agent],
        tasks=[answer_question_task],
        memory=True,
        cache=True,
        full_output=False
    )


def ask_question(question_):
    knowledge_agent = get_knowledge_agent()
    answer_question_task = get_answer_question_task(knowledge_agent)
    knowledge_crew = get_knowledge_crew(knowledge_agent, answer_question_task)

    result = knowledge_crew.kickoff(inputs={'question': question_})
    return result


if __name__ == "__main__":
    while True:
        question = input("What do you want? ")
        if question.lower() == "exit":
            break
        print("Assistant.AI: Let me do some research...")
        print(f"Assistant.AI:\n\n {ask_question(question)}\n\n\n")
