from dotenv import load_dotenv

load_dotenv()

import os
import sys

from shared_playground_crewai.llm_client import create_llm_client

llm = create_llm_client(api_key=os.getenv("GOOGLE_API_KEY"), model="gemini-pro")

print("########## SETUPING ##########")
from crewai import Agent, Crew, Process, Task

print("########## STARTING ##########")
random_quote_writer = Agent(
    role="Author of philosophy and self-help",
    goal="To create phrases, catch-phrase or motivational texts to help unmotivated people",
    backstory="""You are a visionary in the realm of self-development, with a deep understanding of both current and emerging mental issues and neurology. Your expertise lies not just in knowing the psychology but in foreseeing how it can be leveraged to solve real-world problems and drive self-development. You want to instigate people to learn about themselves and be responsible for themselves.""",
    verbose=True,  # enable more detailed or extensive output
    allow_delegation=True,  # enable collaboration between agent
    llm=llm,  # to load gemini
)


task1 = Task(
    agent=random_quote_writer,
    description="""Write motivational quote to instagram post.""",
    expected_output="A list of 10 inspiring motivational texts/quotes to be used in an Instagram post.",
)


crew = Crew(
    agents=[
        random_quote_writer,
    ],
    tasks=[
        task1,
    ],
    verbose=2,
    # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.
    process=Process.sequential,
)

result = crew.kickoff()

print("############ RESULT ###########")
print(result)
