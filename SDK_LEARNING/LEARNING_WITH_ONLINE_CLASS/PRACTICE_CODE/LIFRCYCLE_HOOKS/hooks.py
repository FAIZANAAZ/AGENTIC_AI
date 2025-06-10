import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool ,RunContextWrapper,RunHooks,AgentHooks
from dataclasses import dataclass
from typing import Any
import rich



load_dotenv()


@dataclass
class User_Info():
    name: str
    age: int
    location: str  




user_info_instance=User_Info("faiza naaz", 30, "Karachi")  
# Runner hook
class CustomRunnerHook(RunHooks):
    async def on_agent_start(self,ctx: RunContextWrapper[User_Info], agent=Agent) -> None:
        rich.print("Runner  is starting...")
        rich.print(f"agent name: {agent.name},Usage:{ctx.usage},username:{ctx.context.name}")
        rich.print("\n\n")
        
        # end runner_agent
    async def on_agent_end(self,ctx: RunContextWrapper[User_Info], agent=Agent,output=Any) -> None:
        rich.print("Runner  is ending...")
        rich.print(f"agent name: {agent.name},Usage:{ctx.usage},username:{ctx.context.name}")
        rich.print("\n\n")
        
        
runner_hook=CustomRunnerHook()        
        
# ye hmny agent hook bnaya hai jo run start or end pr call hoga ye runner sy phly chlyga or end wla runner ke bad end hoga ismy self dena lazmi he ismy koch nhi krna bs agr hm chahty hen ke runner sy phly koch chly to hm ismy likh skty hen osko ak class bna kr on_agent_start or on_agent_end method use krky osmy koch bhi likh skty hen abhi hmny ismy ak context ko add kr diya wesy hm koch bhi kr skty hen ismy   or ye runner me hi pass hoga

# Agent hook************
class CustomAgentHook(AgentHooks):
    async def on_start(self,ctx: RunContextWrapper[User_Info], agent=Agent) -> None:
        rich.print("Agent  is starting...")
        rich.print(f"agent name: {agent.name},Usage:{ctx.usage},username:{ctx.context.name}")
        rich.print("\n\n")
        
        
        # end runner_agent
    async def on_end(self,ctx: RunContextWrapper[User_Info], agent=Agent,output=Any) -> None:
        rich.print("Agent  is ending...")
        rich.print(f"agent name: {agent.name},Usage:{ctx.usage},username:{ctx.context.name}")  
        rich.print("\n\n")
            
  
agent_hook=CustomAgentHook()
  
# ye bhi   same wesy hi he bs ye agent ke start sy phly stat hoga or agent ke end ke bad end hoga   or ye Agent me pass hoga 

# in dono me phly Runner wlaa satrt hota he phir agent wala or end bhi isi trha phly runner wala phir agent wla    
        
        
agent=Agent[User_Info](
model="gpt-4.1-nano",
name="my_agent",
instructions="You are a helpful assistant .",
hooks=CustomAgentHook(),

)

async def main():
    result=await Runner.run(agent, "what is name of user",context=user_info_instance,hooks=CustomRunnerHook())
    # 
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())





