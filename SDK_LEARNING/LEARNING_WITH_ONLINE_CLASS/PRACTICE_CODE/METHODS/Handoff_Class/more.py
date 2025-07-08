import json
from dotenv import load_dotenv
from agents import Agent, Handoff, RunContextWrapper,Runner, function_tool, enable_verbose_stdout_logging
from pydantic import BaseModel
import rich
from agents.extensions import handoff_filters 



# ***********************************************************


load_dotenv()  # Load environment variables from .env file
enable_verbose_stdout_logging()



@function_tool
def greeting():
    return "Hello, how can I assist you today?"

customer_agent=Agent(
    model="gpt-4.1-mini",
    name="customer_agent",
    instructions="you are a customer support agent.",
    handoff_description="if you are unable to answer the question, please handoff to the hanoff agent.",
    tools=[greeting],  # ye tools optional hen   
)
# ***********************************************************

# ***********************************************************

class User_Info(BaseModel):
    name: str
    
    # ismy hm jo bhi dengy wo agennt khod samj kr osko ak sturcture me set krdega jesy {name: "Ali"}
 
schema = User_Info.model_json_schema()
# yha wo object ko jeson bnara he 
schema["additionalProperties"] = False  
# HM IS TRHA SY  schema bnaty hen or osko jeson me change krty hen or additional Properties False krty hen phit schema dety hen hm 


# ***********************************************************
async def my_invoke  (wrapper: RunContextWrapper, argument:str)->Agent:
    user_data=json.loads(argument)
    # ye string ko jeson me convert krty ha or osky bd pydantic model me addd krta he 
    user_info= User_Info(**user_data)
    rich.print(f"User Info: {user_info.name}")
    rich.print(f"User data: {user_data}")
    rich.print(f"User Info: {user_info}")
    
    rich.print(f"Argument passed to the handoff: {argument}")
    
    customer_agent.instructions = f"you are a customer support agent. User name is {user_info.name}."
    # print sy oper wali line bs samjhny ke liye he 
    
    return customer_agent

# KIoky ye function awaitable hota he hm isko async me rakhety hen or phir dety hen  ismy osy function ko return krygy jispr handsoff ki class he or 

# ***********************************************************

modify_agent = Handoff(
    agent_name="customer_agent",  # required property or isy string me dena lazmi he 
    tool_name="customer_support_agent",
    tool_description="this tool is used to handoff the conversation to the customer support agent.",
    input_filter=handoff_filters.remove_all_tools,
    input_json_schema=schema,
    on_invoke_handoff=my_invoke,  # optional; if set, this function will be called when the handoff is invoked
    is_enabled=False  # optional; if set to False, the agent will not handoff
)
# ismy hm agent ki properties ko override krty hen

print("hands of hogya ",modify_agent.get_transfer_message(customer_agent))
# ismy hm ye krty hen ke agr hm chahty hen ke koi mesaage print ho hands off ke doran jisy llm or confirm ho jay to wo sms hm imy de dengy print ke sath concatinate krwa kr
# 
# ***********************************************************


agent =Agent(
    model="gpt-4.1-mini",
    name="triage agent",
    instructions="you are a helpful agents.",
    handoffs=[customer_agent],
    tools=[greeting]
    
)

# ***********************************************************

ans=Runner.run_sync(agent,"i need customer support?")
rich.print(ans.final_output)
  

# ***********************************************************
# ///////////////////////////////////////////////////////////
