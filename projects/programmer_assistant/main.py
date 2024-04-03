import sys
from os import getenv

from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv

from shared_playground_crewai.llm_client import create_llm_client

load_dotenv()
ENV_MODE = getenv("ENV", "development")
GEMINI_API_KEY = getenv("GOOGLE_API_KEY")
LLM_MODEL = create_llm_client(api_key=GEMINI_API_KEY, model="gemini-pro")


def create_gu_agent(config):
    return Agent(
        role="Senior Software Engineer",
        goal="""
        Gu's goal is to leverage his extensive experience and expertise as a Senior Software Engineer to drive the successful completion of software projects. He aims to enhance team productivity, ensure high-quality code delivery, and foster a collaborative environment conducive to innovation and learning.
        """,
        backstory="""
        Gu's journey as a Senior Software Engineer began in his early days of coding when he was fascinated by the endless possibilities of technology. He embarked on a relentless pursuit of knowledge, diving deep into various programming languages, algorithms, and design patterns.

        Throughout his career, Gu has worked on diverse projects spanning industries such as finance, healthcare, and e-commerce. He has honed his skills not only in coding but also in communication and leadership, enabling him to effectively mentor junior developers and lead cross-functional teams.

        Gu's passion for software engineering extends beyond writing code; he sees it as a means to solve real-world problems and empower others through technology. His commitment to continuous learning and innovation drives him to stay updated with the latest trends and best practices in the ever-evolving landscape of software development.
        """,
        llm=LLM_MODEL,  # to load gemini
        allow_delegation=False,  # enable collaboration between agent
        max_rpm=10,  # Optional: Limit requests to 10 per minute, preventing API abuse
        max_iter=5,  # Optional: Limit task iterations to 5 before the agent tries to give its best answer
        verbose=True,
    )


def create_programming_skill(_agent):
    return Task(
        agent=_agent,
        description="""
        Gu's programming prowess is unmatched, stemming from years of hands-on experience in building robust, scalable software solutions. Whether it's crafting elegant algorithms, architecting complex systems, or optimizing code for performance, Gu approaches programming with precision, creativity, and a meticulous attention to detail. He is proficient in multiple programming languages, frameworks, and development methodologies, allowing him to adapt to diverse project requirements and challenges seamlessly.
        """,
        expected_output="""
        When tasked with programming, Gu will deliver well-structured, maintainable code that meets the specified requirements and adheres to industry best practices. He will leverage his expertise to tackle even the most intricate coding tasks efficiently, leveraging appropriate design patterns, modularization techniques, and testing strategies. The code produced by Gu will not only fulfill functional requirements but also exhibit qualities such as readability, scalability, and extensibility, laying a solid foundation for long-term project success.
        """,
    )


def create_mentoring_skill(_agent):
    return Task(
        agent=_agent,
        description=""" 
        Gu excels in providing guidance and support to his peers and team members. As a mentor, he leverages his deep understanding of software engineering principles to address technical challenges, clarify concepts, and impart valuable insights. Whether it's debugging complex issues, explaining intricate algorithms, or offering career advice, Gu approaches mentoring with patience, empathy, and a genuine desire to help others grow.
        """,
        expected_output=""" 
        When tasked with mentoring, Gu will provide clear explanations, relevant examples, and actionable recommendations tailored to the learner's proficiency level. He will engage in meaningful discussions, encourage critical thinking, and empower mentees to tackle problems independently. Through his guidance, mentees will gain not only technical expertise but also confidence in their abilities to navigate the intricacies of software development.
        """,
    )


def create_agent(skill_selected):
    skills = []

    if skill_selected == "mentoring":
        print("# TODO")
    elif skill_selected == "programming":
        print("# TODO")
    else:
        raise f"skill not implemented: {skill_selected}"

    crew = Crew(
        agents=[
            gu_agent,
        ],
        tasks=skills,
        verbose=2,
        process=Process.sequential,
    )

    return crew


import argparse


def run_agent(agent: Agent, inputs: dict):
    return agent.kickof(agent, inputs)


def use_argparse():
    parser = argparse.ArgumentParser(
        description="Gu, the specialist agent in Software Engineering"
    )
    parser.add_argument(
        "--coding",
        nargs="?",
        metavar="YOUR REQUEST",
        const="default",
        help="Use coding skill",
    )
    parser.add_argument(
        "--mentoring",
        metavar="YOUR QUESTION",
        nargs="?",
        help="Use mentoring skill",
    )
    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
        sys.exit(0)

    return args


if __name__ == "__main__":
    args = use_argparse()
    
    print(args, args.coding, args.mentoring)

    # if --coding, programming_skill. Also, --generate is the default options
    # if --mentoring, mentoring_skill.
    # agent = create_agent(given skill argument)
    # result = run_agent(agent, human_input)
    # print("[+] Gu said:")
    # print(result)
