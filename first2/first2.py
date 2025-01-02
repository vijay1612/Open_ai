import os
import os

# Fetch API key from environment variable
api_key = os.environ.get("OPENAI_API_KEY")

# If the key is missing, raise an error
if not api_key:
    raise ValueError(
        "API key is missing. Please set the OPENAI_API_KEY environment variable."
    )
from crewai import Agent, Task, Process, Crew
import openai

# Fetch API key from environment variables
api = os.environ.get("OPEN_API_KEY")

# Market Research Analyst Agent
marketer = Agent(
    role="Market Research Analyst",
    goal="To provide the best market research analysis",
    backstory="""You are an expert at understanding the market demand, target audience, and competition. 
    This is crucial for validating whether an idea fulfills a market need and has the potential to attract a wide audience. 
    You are good at coming up with ideas on how to appeal to the widest possible audience.""",
    verbose=True,  # Enable more detailed or extensive output
    allow_delegation=False,  # Disable collaboration between agent
)

# Technology Expert Agent
technologist = Agent(
    role="Technology Expert",
    goal="Make assessments on how technologically feasible the company is and what type of technologies the company needs to adopt in order to succeed",
    backstory="""You are a visionary in the realm of technology, with a deep understanding of both current and emerging technological trends. 
    Your expertise lies not just in knowing the technology but in foreseeing how it can be leveraged to solve real-world problems and drive business innovation. 
    You have a knack for identifying which technological solutions best fit different business models and needs, ensuring that companies stay ahead of the curve. 
    Your insights are crucial in aligning technology with business strategies, ensuring that the technological adoption not only enhances operational efficiency but also provides a competitive edge in the market.""",
    verbose=True,  # Enable more detailed or extensive output
    allow_delegation=False,  # Disable collaboration between agent
)

# Business Development Consultant Agent
business_consultant = Agent(
    role="Business Development Consultant",
    goal="Evaluate and advise on the business model, scalability, and potential revenue streams to ensure long-term sustainability and profitability",
    backstory="""You are a seasoned professional with expertise in shaping business strategies. Your insight is essential for turning innovative ideas 
    into viable business models. You have a keen understanding of various industries and are adept at identifying and developing potential revenue streams. 
    Your expertise in business development is crucial for ensuring the long-term sustainability and profitability of the company.""",
    allow_delegation=True,  # Enable collaboration between agents
)

# Task 1: Market Research Analysis
task1 = Task(
    description="""Analyze what the market demand for plugs for holes in crocs (shoes) is, so that this iconic footwear looks less like Swiss cheese. 
    Write a detailed report with a description of what the ideal customer might look like, and how to reach the widest possible audience. 
    The report has to be concise with at least 10 bullet points and it has to address the most important areas when it comes to marketing this type of business.""",
    agent=marketer,  # Specify the agent responsible for this task (Marketer Agent)
    expected_output="A detailed report with marketing strategies, target audience, and key takeaways.",
)

# Task 2: Technology Assessment
task2 = Task(
    description="""Analyze how to produce plugs for crocs (shoes) so that this iconic footwear looks less like Swiss cheese. 
    Write a detailed report with a description of which technologies the business needs to use in order to make High-Quality T-shirts. 
    The report has to be concise with at least 10 bullet points and it has to address the most important areas when it comes to manufacturing this type of business.""",
    agent=technologist,  # Specify the agent responsible for this task (Technologist Agent)
    expected_output="A detailed report with the list of required technologies for T-shirt production.",
)

# Task 3: Business Plan Creation
task3 = Task(
    description="""Analyze and summarize marketing and technological reports and write a detailed business plan with a description of how to make a sustainable and profitable 'plugs for crocs (shoes)' business so that this iconic footwear looks less like Swiss cheese. 
    The business plan has to be concise with at least 10 bullet points, 5 goals, and it has to contain a time schedule for which goal should be achieved and when.""",
    agent=business_consultant,  # Specify the agent responsible for this task (Business Consultant Agent)
    expected_output="A comprehensive business plan with timelines, goals, and strategies for sustainable growth.",
)

# Crew initialization
crew = Crew(
    agents=[marketer, technologist, business_consultant],
    tasks=[task1, task2, task3],
    verbose=True,  # Set verbose to True or False, not 2
    process=Process.sequential,  # Ensure this is the correct syntax for Process
)

result = crew.kickoff()  # Run the crew
print(result)  # Print the result
