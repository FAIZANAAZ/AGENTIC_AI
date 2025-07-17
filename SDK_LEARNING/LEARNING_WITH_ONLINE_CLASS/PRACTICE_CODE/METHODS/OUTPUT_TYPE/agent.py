
from typing import Any, Literal
from dotenv import load_dotenv
from agents import Agent, AgentHooks, RunContextWrapper, Runner, enable_verbose_stdout_logging, function_tool
from pydantic import BaseModel, Field
import rich
import datetime




# ***********************************************************

enable_verbose_stdout_logging()

load_dotenv()  


class MyName (BaseModel):
    is_order: bool


class AgentCustom_Hook(AgentHooks):
    # isy tamam methods a jaygy agentclass ke agenthook inherit krny sy 
    async def on_start(self, context: RunContextWrapper, agent:Agent):
        print("i am on start \n")
        # return await super().on_start(context, agent)
        
    async def on_end(self, context: RunContextWrapper, agent:Agent, output:Any):
        print("i am on end ")
        # return await super().on_end(context, agent)  
        
    async def on_handoff(self, context, agent, source):
      
        print("i am on handoff")                 
# handsoff lgany sy hmara end wala method nhi chlyga kioky wo man agent ke badchlta he lekin jb hands off howa to kam dosry agent ke pas 
# chlly gya

    async def on_tool_start(self, context, agent, tool):
       print("i am on tool start")
# ***********************************

@function_tool
def weather():
    return "sunny"
# ***********************************
hinglish_agent=Agent(
    name="hinglish agent",
    model="gpt-4.1-mini",
    instructions="you are a helpfull assistant. and always use weather tool",
    handoff_description="reply in hinglish",
    tools=[weather],
    hooks=AgentCustom_Hook()
)
# ***********************************

agent =Agent(
    model="gpt-4.1-mini",
    name="triage agent",
    instructions="you are a helpfull assistant.",
    hooks=AgentCustom_Hook(),
    handoffs=[hinglish_agent]
   
)
    
        

# ***********************************************************
time=datetime.datetime.now()
ans=Runner.run_sync(agent,input="hi please handoff to hinglish agent")
rich.print(time)
rich.print(ans.final_output)





# ***********************************************************
# ///////////////////////////////////////////////////////////
