from crewai import Agent
from crewai_tools.tools import WebsiteSearchTool
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI

web_search_tool = WebsiteSearchTool()

class Agents():
    def researcher_agent(self):
        return Agent(
            role='Senior Research Analyst',
            goal='Uncover latest news in healthcare AI development',
            backstory="""You work at a leading tech think tank.
            Your expertise lies in identifying emerging trends.
            You have a knack for dissecting complex data and presenting actionable insights.""",
            verbose=True,
            allow_delegation=False,
            tools=[web_search_tool],
            llm=ChatOpenAI(model_name="gpt-4", temperature=0.7)
        )

    def writer_agent(self):
        return Agent(
            role='Healthcare AI Content Blog Writer',
            goal='Craft compelling content on healthcare AI development',
            backstory="""You are a renowned Content Blog Writer, known for your insightful and engaging articles.
            You make a wonderful story with given content.
            You transform complex concepts into compelling narratives.""",
            verbose=True,
            allow_delegation=True
        )
