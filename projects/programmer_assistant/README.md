# projects/programmer_assistant




![](demo.png)


---

We are creating an AI Agent in Python using a library. Our goal is to create an Agent that acts as a Senior Software Engineer and helps me with my projects and questions.

I will briefly explain to you about the customization of our agent:
```
Key Attributes for Customization
- Role: Specifies the agent's job within the crew, such as 'Analyst' or 'Customer Service Rep'.
- Goal: Defines what the agent aims to achieve, in alignment with its role and the overarching objectives of the crew.
- Backstory: Provides depth to the agent's persona, enriching its motivations and engagements within the crew.
- Tools: Represents the capabilities or methods the agent uses to perform tasks, from simple functions to intricate integrations.
```

To create our Senior Software Engineer Agent (let's call him Gu) we need:
- [X] Define agent role: Senior Software Engineer
- [ ] Define agent goal
- [ ] Define agent backstory

We also need to define what types of skills the agent will have.Initially we will create two: program and mentor.

"Programming" ability is to generate code as a final output based on requirements and other specifications and other pre-configured specifications.

The "mentoring" ability is to answer technical questions and teach the topic asking as a final output based on requirements and other pre-configured specifications.

Below is a piece of code that we will use to create our agent.
```python
gu_agent = Agent(
    role="TBD",
    goal="TBD",
    backstory="""TBD""",
    llm=llm, 
    allow_delegation=False, 
    max_rpm=10, 
    max_iter=5, 
    verbose=(
        True
        if config.env == "development"
        else False
    ),
)

programming_skill = Task(
    agent=gu_agent,
    description="TBD",
    expected_output="TBD",
)

mentoring_skill = Task(
    agent=gu_agent,
    description="TBD",
    expected_output="TBD",
)
```


So, in short, your mission is:
- [ ] Define agent goal
- [ ] Define agent backstory
- [ ] Define the "mentoring" ability
  - [ ] define its description
  - [ ] define its expected output
- [ ] Define the "programming" ability
  - [ ] define its description
  - [ ] define its expected output