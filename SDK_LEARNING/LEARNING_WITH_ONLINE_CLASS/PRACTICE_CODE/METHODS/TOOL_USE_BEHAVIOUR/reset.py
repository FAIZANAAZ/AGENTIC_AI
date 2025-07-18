
from typing import Literal
from dotenv import load_dotenv
from agents import Agent, FunctionToolResult, ModelSettings, RunContextWrapper, Runner, ToolsToFinalOutputResult, enable_verbose_stdout_logging, function_tool
from pydantic import BaseModel, Field
import rich




# ***********************************************************
enable_verbose_stdout_logging()


load_dotenv()  

# ***********************************************************


@function_tool
def weather_tool():
    return f"karachi weather is karachi"



agent =Agent(
    model="gpt-4.1-mini",
    name="triage agent",
    instructions="you ara a helpfull agent.",
    tools=[weather_tool],
    model_settings=ModelSettings(tool_choice="required"),
    reset_tool_choice=True
    # iski best practice ye he or recomeneded bhi ye he ke isko true rkha jay 
    # ye tool ko call  krny ke bas osko reset krdeta he 
    # agr isko false kiya to wo bar bar tool ko call krdega infinit loop me
)

# ***********************************************************

ans=Runner.run_sync(agent,input="hi what is weather of karachi")
rich.print(ans.final_output)
  




# ***********************************************************
# ///////////////////////////////////////////////////////////
