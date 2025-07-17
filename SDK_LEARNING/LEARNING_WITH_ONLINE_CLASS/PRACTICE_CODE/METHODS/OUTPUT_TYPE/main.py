
from typing import Literal
from dotenv import load_dotenv
from agents import Agent, Runner
from pydantic import BaseModel, Field
import rich




# ***********************************************************



load_dotenv()  


class MyName (BaseModel):
    is_order: bool
    type:Literal["pizza","burger","pasta"]
    # taky wo ak chiz othay dono nhi othay literal ak hi value rkhta he 
    ingredients: list[str]=Field(default_factory=list)


agent =Agent(
    model="gpt-4.1-mini",
    name="triage agent",
    instructions="always check if use tell his pizza and burger so your output should be only pizza or burger.",
    output_type=MyName


   
)
    
        

# ***********************************************************

ans=Runner.run_sync(agent,input="hi i want to pizza and burger")
rich.print(ans.final_output)
  

name_check=ans.final_output



# ***********************************************************
# ///////////////////////////////////////////////////////////
