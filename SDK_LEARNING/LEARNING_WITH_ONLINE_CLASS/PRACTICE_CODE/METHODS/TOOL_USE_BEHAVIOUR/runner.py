
from typing import Literal
from dotenv import load_dotenv
from agents import Agent, FunctionToolResult, ModelSettings, RunConfig, RunContextWrapper, Runner, ToolsToFinalOutputResult, enable_verbose_stdout_logging, function_tool
from pydantic import BaseModel, Field
import rich




# ***********************************************************
enable_verbose_stdout_logging()


load_dotenv()  

# ***********************************************************

# ***********************************************************


@function_tool
def weather_tool():
    """this is weather tool"""
    return f"karachi weather is karachi"



agent =Agent(
    model="gpt-4.1-mini",
    name="triage agent",
    instructions="you ara a helpfull agent.",
    tools=[weather_tool],
    
)



# ***********************************************************
config=RunConfig(
    model="gpt-4.1-mini",
    tracing_disabled=True,  
    workflow_name="faiza workflow", 
    # ye by default iska name agent workflow hota he agr hm de dengy to is name sy tracing show hogi hamri dashbord pr
    trace_include_sensitive_data=True
    # ye bhi tracing ko diable krdyga yani openai ke dashbord pr nhi show hoga data
    
    
)
ans=Runner.run_sync(agent,input="hi what is weather of karachi",run_config=config)
rich.print(ans.final_output)
  




# ***********************************************************
# ///////////////////////////////////////////////////////////
