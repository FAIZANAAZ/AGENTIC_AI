
import random
from dotenv import load_dotenv
from agents import Agent, Handoff, ModelSettings, RunContextWrapper, Runner, function_tool, enable_verbose_stdout_logging
from pydantic import BaseModel, Field
import rich
from agents.extensions import handoff_filters
from datetime import datetime, time
# ***********************************************************
# Load environment variables and enable logging
load_dotenv()  
# enable_verbose_stdout_logging()
# ***********************************************************

# ***********************************************************
class ToolInfo(BaseModel):
  token_number: str=Field(description="this take token number")
  wait_time: str=Field(description="this take wait time")
  message: str=f"please take token {token_number} and wait for {wait_time}and have a seat , we will call you"
# ***********************************************************

@function_tool
def generate_customer_token(service_type: str="general") -> ToolInfo:
  """
  generate a general token number for customer queue"""
  
  if service_type == "acount_service":
    wait_time="5-10 minutes"
    prefix="A"
    
  elif service_type == "transfer_service":
    wait_time="2-5 minutes"
    prefix="T"
  elif service_type == "loan_service":
    wait_time="15-20 minutes"
    prefix="L"
  else:
    prefix="G"
    wait_time="8-10 minutes"
   
  token_number=f"{prefix}{random.randint(100,999)} " 
  return service_type


# ***********************************************************
account_agent=Agent(
  model="gpt-4.1-mini",
  name="Account Service Agent",
  instructions="""you help users in their query of account balance ,statements ,and account information,always generate a general token . 
  
  """,
)

transfer_agent=Agent(
  model="gpt-4.1-mini",
  name="Transfer Agent",
  instructions="""you help users  with money transfer  ,generate a general token .
  """,
)

loan_agent=Agent(
  model="gpt-4.1-mini",
  name="Loan Agent",
  instructions="""you help user with loans and mortgages ,always generate a general token .  . 
  
  """,
)
# ***********************************************************
agents = Agent(
   model="gpt-4.1-mini",
   name="Bank Greeting Agent",
   instructions="""you are a friendly bank greeting agent.
   1.welcome  customer nicely
   2.use identify_banking_purpose to understand user need .
   3.confidence>0.8 ,send user to the right specialist 
   4.otherwise generate a general token .
   always be help_full
   """,
   handoffs=[account_agent , transfer_agent, loan_agent],
   tools=[generate_customer_token]
  )

# ***********************************************************
result=Runner.run_sync(agents, "hi")
rich.print(result.final_output)