#importing libraries
import os
from crewai import Agent, Task, Crew
# Importing crewAI tools
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)

# Set up API keys
os.environ["SERPER_API_KEY"] = "" # serper.dev API key
os.environ["OPENAI_API_KEY"] = ""

# Instantiate tools
docs_tool = DirectoryReadTool(directory='./blog-posts')
file_tool = FileReadTool()
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()


city = input("Enter the name of city you want weather for--> ").strip()
# Create agents
researcher = Agent(
    role='Weather analyst',
    goal='Provide Up to date Weather Information on {city}',
    backstory='An expert analyst for current weather for {city}',
    tools=[search_tool, web_rag_tool],
    verbose=True
)

# Define tasks
research = Task(
    description='Give the current Weather updates for a particular {city}',
    expected_output='summary of weather inforamtion in a particular {city}',
    agent=researcher
)


# Assemble a crew with planning enabled
crew = Crew(
    agents=[researcher, ],
    tasks=[research, ],
    verbose=True,
    planning=True,  # Enable planning feature
)

# Execute tasks
result = crew.kickoff(inputs={'city': city})
print(result)
