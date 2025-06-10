import os
from dotenv import load_dotenv
from agents import Agent , Runner, WebSearchTool 


load_dotenv()
OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")


# ***********************************************************


agent=Agent(
    model="gpt-4.1-mini",
    name="my_assistant",
    instructions="your are help_full assistant,always use webserch tool for information,answer question as concisely as possible",
    tools=[WebSearchTool()],
)

# ***********************************************************


    
result = Runner.run_sync(agent, "who is the best football player in the world")

print(result.final_output)
    


