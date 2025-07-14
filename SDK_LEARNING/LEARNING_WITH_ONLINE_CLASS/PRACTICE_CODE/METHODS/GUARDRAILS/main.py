import json
from typing import Any
from dotenv import load_dotenv
from agents import Agent, FunctionTool, RunContextWrapper,Runner, enable_verbose_stdout_logging
from openai import BaseModel
import rich




# ***********************************************************


# enable_verbose_stdout_logging()

class weatherArg(BaseModel):
    city: str
# ye class he types ki pydantic ki 
load_dotenv()  # Load environment variables from .env file

def weather_tool(city:str):
    return f"{city} weather is good"

# ********************************

async def run_weather_tool(ctx:RunContextWrapper[Any],arg:str):
    parsed=weatherArg.model_validate_json(arg)
    # ismy json string nikal kr bhejyga arg me agent osko hm pydaanki ka model prameter me convert krky add kry hen 
    return weather_tool(parsed.city)
    # 

# ********************************

weather_shema=weatherArg.model_json_schema()
# isko hmny chnge kiya json ke schema me or isko alag sy isi liye likhty hen kioky hmy additional property ko false krna hota he
# weather_schema ak trha sy weatherArg ki class ka instance bn gya he 
weather_shema["additionalProperties"] = False

# ********************************


agent =Agent(
    model="gpt-4.1-mini",
    name="triage agent",
    instructions="you are a helpful agents.",
    tools=[FunctionTool(
        name="weather_tool",
        # ye ak tool he bs jis pr hm kam kry hen
        description="get the weather of a city",
        # ye tool ki description he 
        on_invoke_tool=run_weather_tool,
        # ye jb run hoga jb tool call hoga 
        params_json_schema=weather_shema,
        # ye schema bna rha he 
        strict_json_schema=True,
        # ye strickly dekehyga ke schema ke mutabik result hona chiye ye bhi by dafault true hota he
        is_enabled=True
        # isko false krny sy tool nhi chalyga by default ye true hota he
    )]
)
# ye function tool class he jismy hmy params_jeson_shema or invote dena lazmi he positional parameter hen 
# 
        
        

# ***********************************************************

ans=Runner.run_sync(agent,"i need customer support?")
rich.print(ans.final_output)
  

# ***********************************************************
# ///////////////////////////////////////////////////////////
