
from typing import Literal
from dotenv import load_dotenv
from agents import Agent, FunctionToolResult, ModelSettings, RunContextWrapper, Runner, ToolsToFinalOutputResult, enable_verbose_stdout_logging, function_tool
from pydantic import BaseModel, Field
import rich




# ***********************************************************
enable_verbose_stdout_logging()


load_dotenv()  

# ***********************************************************


def custom_error_function( ctx:RunContextWrapper,EXP:Exception):
    return f"Error in weather tool {str(EXP)}"
# koi bhi   error ayga functiontool to osmy ye error a jayga or exp me wo error print hoga jis wja he error any ki
    
@function_tool(
    name_override="weather_tool_karachi",
    # jis function ke ope ye decorater lga hoga iska name override krdega
    description_override="this is weather tool for karachi",
    # jis function ke ope ye decorater lga hoga iska description override krdega
    
    docstring_style="google",
    # ye function ke docstring style ko google style pr set krdega
    
    use_docstring_info=True,
    # ye function ke docstring gaib krdega 
    
    failure_error_function=custom_error_function,
    # ismy jo function pass kiya he koi error aya oto ye print hoga agr hm khod ka nhibnaty to eo by default default_tool_error_function ko run krta he 
    
    is_enabled=True,
    # agr isko false krdengy to wo tool agen ko dikhyga hi nhi
    
    strict_mode= True,
# isy ye tool ko use krny k liye strict mode krdeta he yani type schema check kryga
     
    
    
    
    
    
    
    )
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

ans=Runner.run_sync(agent,input="hi what is weather of karachi")
rich.print(ans.final_output)
  




# ***********************************************************
# ///////////////////////////////////////////////////////////
