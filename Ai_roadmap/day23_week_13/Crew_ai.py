from crewai import Agent,Task ,Crew,Process,LLM
import os
from dotenv import load_dotenv
load_dotenv()
gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

fact_finder = Agent(
    role = "Fact Finder",
    goal = "Answer factual question with high accuracy",
    backstory = "you are a prominent research assistant who answer questions in a well manner with most accurate answer.",
    llm = gemini_llm
)
find_capital_task = Task(
    description = "What is the main reason in the long term stability of old monuments. where modern engineering fails",
    expected_output= "The output should consists of three things , 1.reason , 2. comparision , 3.suggestions",
    agent=fact_finder
)
crew = Crew(
    agents = [fact_finder],
    tasks= [find_capital_task],
    process=Process.sequential
)
result = crew.kickoff()
print(result)