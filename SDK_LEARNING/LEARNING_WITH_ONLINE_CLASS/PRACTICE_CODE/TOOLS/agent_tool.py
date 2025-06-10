
from dotenv import load_dotenv
from agents import Agent , Runner, function_tool 


load_dotenv()



english_agent=Agent(
    name="English Agent",
    model="gpt-4.1-mini",
    instructions="You are a helpful assistant that translates English to urdu."
)

triage_agent=Agent(
    model="gpt-4.1-mini",
    name="my_assistant",
    instructions="your rout user queries to the appropriate agent",
    tools=[english_agent.as_tool(
        tool_name="english_agent",
        tool_description="Translates English text to Urdu."
    )]
   
)

# ***********************************************************


    
result = Runner.run_sync(triage_agent,"what is the meaning ok country")

print(result.final_output)