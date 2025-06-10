from dotenv import load_dotenv
from agents import Agent, Runner, function_tool ,RunContextWrapper
from dataclasses import dataclass 



load_dotenv()

# context mean ak alag sy data dena agent ko jiska wo use krky ans de sky jey mera data me de skti ho as a tool kioky internat pr mera dta to nahi hai
# **********************
@dataclass
class User_Info():
    name: str
    age: int
    location: str  
    
#  hm context me user ka schema bnaygy dataclass ki madad sy lekin agent data class ko nhi phchanta to wo phchanta he tools ka 
# to hm isko as a data type use krengy or retyun krwa dengy  or 
# agent ko  wo function as a tool pas krdengy ke data is trha ka hoga 
# **********************
@function_tool
async def fetch_user_info(wrapper: RunContextWrapper[User_Info])->str :   
    return f"user_name is {wrapper.context.name} and age is {wrapper.context.age} and location is {wrapper.context.location}"


user_info_instance=User_Info("faiza naaz", 30, "Karachi")  
# ye hmny data diya he or isko hm as a context pas krengy runner me

agent=Agent[User_Info](
model="gpt-4.1-nano",
name="my_agent",
instructions="You are a helpful assistant .",
tools=[fetch_user_info]
)

result=Runner.run_sync(agent, "what is name of user",context=user_info_instance)
# 
print(result.final_output)






