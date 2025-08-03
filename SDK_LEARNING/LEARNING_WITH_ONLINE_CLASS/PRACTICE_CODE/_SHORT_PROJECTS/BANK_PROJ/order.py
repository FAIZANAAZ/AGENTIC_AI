
import random
from typing import Any
from dotenv import load_dotenv

from agents import Agent, Handoff, ModelSettings, RunContextWrapper, Runner, function_tool, enable_verbose_stdout_logging,input_guardrail,TResponseInputItem,GuardrailFunctionOutput,InputGuardrailTripwireTriggered,output_guardrail,OutputGuardrailTripwireTriggered
from pydantic import BaseModel, Field
import rich
from agents.extensions import handoff_filters
from datetime import datetime, time
# ***********************************************************
# Load environment variables and enable logging
load_dotenv()  
# enable_verbose_stdout_logging()
# ***********************************************************
class check_slangs_class(BaseModel):
  is_abusive:bool=Field(description="value will be True if user query has some slang or abusive words")
  reasoning:str=Field(description="what is the reason behind it ")

i_guardrail_agent=Agent(
  model="gpt-4.1-mini",
  name="Input Guardrail Agent",
  instructions="always check if the user query has any abusive and slang words .",
  output_type=check_slangs_class)

@input_guardrail
async def check_slangs(ctx: RunContextWrapper,agent: Agent, input: str |list[TResponseInputItem]) -> GuardrailFunctionOutput:
  result =await Runner.run(i_guardrail_agent, input,context=ctx)
 
  return GuardrailFunctionOutput(
    output_info=result.final_output,
    tripwire_triggered=result.final_output.is_abusive
  )

# ***********************************************************

class check_response_class(BaseModel):
  is_not_banking_related:bool=Field(description="if the llm response is not related to banking related topic set the value True in this field")
  reasoning:str=Field(description="what is the reason behind it ")

o_guardrail_agent=Agent(
  model="gpt-4.1-mini",
  name=" Output Guardrail Agent",
  instructions="always check if the llm response should be only related to banking response .",
  output_type=check_response_class
)
@output_guardrail
async def response_guardrail(ctx: RunContextWrapper,agent: Agent,output: Any) -> GuardrailFunctionOutput:
  
  result =await Runner.run(o_guardrail_agent, output,context=ctx)
  return GuardrailFunctionOutput(
    output_info=result.final_output,
    tripwire_triggered=result.final_output.is_not_banking_related
  )

# ***********************************************************

class ToolInfo(BaseModel):
  token_number: str
  wait_time: str
  message: str
  service_type: str
  
  
class serviceType(BaseModel):
  confidence: float
  service: str
  keywords_detected: list[str]
  reason: str
  
# ***********************************************************

@function_tool
def generate_customer_token(service_type: str="general") -> ToolInfo:
  """
  generate a general token number for customer queue the value of the service_type arguments can be only these as mentio below
  
  Args:
      service_type == "acount_service".
      service_type == "general".
      service_type == "transfer_service".
      service_type == "loan_service".
  """
  
  # llm arguments ko isi name sy fil kryga 
  
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
  
  return ToolInfo(
    token_number=token_number,
    wait_time=wait_time,
    message=f"please take token {token_number} and wait for {wait_time}and have a seat , we will call you",
    service_type=service_type
  )
  



@function_tool
def identify_banking_purpose(customer_request: str) -> str:
  """ it is a simple function to figure out what banking service customer need"""
  
  corrected_request=customer_request.lower()
  
  if ("balance" in corrected_request) or ("account" in corrected_request) or ("statement" in corrected_request):
    return serviceType(
       confidence=0.9,
       service="account_service",
       keywords_detected=["balance","account","statement"],
       reason="Customer want to check account balance"
    )
    
  elif ("transfer" in corrected_request) or ("send" in corrected_request) or ("payment" in corrected_request):
    return serviceType(
       confidence=0.9,
       service="transfer_service",
       keywords_detected=["transfer","send","payment"],
       reason="Customer want to transfer money"
    )  
    
  elif ("loan" in corrected_request) or ("mortgage" in corrected_request) or ("borrow" in corrected_request):
    return serviceType(
       confidence=0.9,
       service="loan_service",
       keywords_detected=["loan","mortgage","borrow"],
       reason="Customer want to get a loan"
    )  
  else:
    return serviceType(
       confidence=0.5,
       service="general_banking",
       keywords_detected=["general"],
       reason="Customer need general banking service"
    )
    
    

# ***********************************************************
account_agent=Agent(
  model="gpt-4.1-mini",
  name="Account Service Agent",
  instructions="""you help users in their query of account balance ,statements ,and account information,always generate a general token . 
  
  """,
  output_guardrails=[response_guardrail]
)

transfer_agent=Agent(
  model="gpt-4.1-mini",
  name="Transfer Agent",
  instructions="""you help users  with money transfer  ,generate a general token .
  """,
  output_guardrails=[response_guardrail]
)

loan_agent=Agent(
  model="gpt-4.1-mini",
  name="Loan Agent",
  instructions="""you help user with loans and mortgages ,always generate a general token .  . 
  
  """,
  output_guardrails=[response_guardrail]
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
   5.always use generate_customer_token to generate token for the customer .
   
   # EXAMPLE:argument for the generate_customer_token can only be  Args:
   (  service_type == "acount_service".
      service_type == "general".
      service_type == "transfer_service".
      service_type == "loan_service".)
      
      
   always be help_full
   
   """,
   handoffs=[account_agent , transfer_agent, loan_agent],
   tools=[generate_customer_token,identify_banking_purpose],
   input_guardrails=[ check_slangs ],
   output_guardrails=[response_guardrail],
  )

# ***********************************************************

while True:
  try:
    user_input = input("\nEnter your query: ")
    if user_input.lower() in ["quit", "exit"]:
      break
    result=Runner.run_sync(agents, user_input)
    rich.print(result.final_output)
    
  except InputGuardrailTripwireTriggered as e:
    print(f"Input Guardrail Tripwire Triggered: {e}")
  except OutputGuardrailTripwireTriggered as e:
    print(f"Output Guardrail Tripwire Triggered: {e}")
  # isy  token km zaya hongy 
# ***********************************************************
  