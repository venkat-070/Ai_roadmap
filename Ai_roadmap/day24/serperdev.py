import datetime
from crewai.tools import tool
from crewai import Agent,LLM,Task,Process,Crew
from crewai_tools import SerperDevTool
import os 
from dotenv import load_dotenv
load_dotenv()

@tool
def current_date_time()->str:
    """It doesnt take any input , but it returns the current date and time."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

gemini_llm = LLM(model="gemini/gemini-flash-lite-latest",
                 api_key=os.getenv("GEMINI_API_KEY"))

search_tool = SerperDevTool()
Researcher = Agent(
    role="Researcher",
    goal="Fetch accurate and most factual results, always stay on point and avoid hallucinating.",
    backstory="You are a researcher, who always return results after a thorough research and repetative verification",
    llm=gemini_llm,
    tools=[search_tool,current_date_time],
)
writer = Agent(
    role = "Writer",
    goal = "You write output in a best and efficient manner, easy to understand format.",
    backstory = "Your role defines the presentation in a effective manner by opting the best vocabulary words.",
    llm = gemini_llm
    
)
research_task = Task(
    description="First, determine today's exact date. Then, using that date, search for the current status of the India vs England ODI match, including score and match situation.",
    expected_output="A brief, accurate summary of the current match status, including score and key details.",
    agent=Researcher
)
writing_task = Task(
    description="Analyse the researcher's output and present the outcomes in a prominent way possible",
    expected_output="The output should contain the task, answer",
    agent=writer,
    context=[research_task]
)
crew = Crew(
    agents=[Researcher,writer],
    tasks = [research_task,writing_task],
    process = Process.sequential,
    verbose = True
)
results = crew.kickoff()
print(results)