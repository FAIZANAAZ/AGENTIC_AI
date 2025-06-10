import os
from dotenv import load_dotenv
from agents import Agent , Runner, WebSearchTool, function_tool 


load_dotenv()
OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")

@function_tool
def weather_karachi():
    print("weather in karachi is -0 degrees")
    
@function_tool    
def prime_minister():
    print("prime minister of pakistan is imran khan")    
    # 

# ***********************************************************


agent=Agent(
    model="gpt-4.1-mini",
    name="my_assistant",
    instructions="your are help_full assistant,always use webserch tool for information,answer question as concisely as possible",
    tools=[weather_karachi,prime_minister],
    # wo function yani  tool ka name dekh kr sawal sy match kryga or chala dega agr hm likhengy pakistan ke praiminister ki jga india
    # to bhi wo imran khan hi bolya kioky wo name match kryga tool ka 
)

# ***********************************************************


    
result = Runner.run_sync(agent,"who is the prime minister of pakistan")

print(result.final_output)