from crewai import Crew,Process, Task , Agent,LLM
import os 
from dotenv import load_dotenv

load_dotenv()
gemini_llm = LLM(
    model = "gemini/gemini-2.5-flash",
    api_key= os.getenv("GEMINI_API_KEY"),
)


Researcher = Agent(
    role = "Researcher",
    goal = "To find factual answer with high accuracy.",
    backstory = "You are an experienced researcher,you answer in short and accurate format with all valid and on point answers.",
    llm = gemini_llm
)

writer = Agent(
    role = "Writer",
    goal = "You write output in a best and efficient manner, easy to understand format.",
    backstory = "Your role defines the presentation in a effective manner by opting the best vocabulary words.",
    llm = gemini_llm
)
research_task = Task(
    description="Make a 5 point summary on how modren software engineering different from the software engineering which is decade old",
    expected_output="I expect u to answer the question in accurate and on point answer rather than irrelavent content, all in 5-points ",
    agent=Researcher
)

writing_task = Task(
    description="Analyse the researcher's output and present the outcomes in a prominent way possible , by explaining each and every line in a concise summary",
    expected_output="The output should contain the task, answer, explanation , justification all in short paragraph format",
    agent=writer,
    context=[research_task]
)
crew = Crew(
    agents=[Researcher,writer],
    tasks=[research_task,writing_task],
    process = Process.sequential
)
results = crew.kickoff()
print(results)