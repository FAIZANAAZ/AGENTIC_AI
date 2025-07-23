
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
def is_business_hours():
  now = datetime.now().time()
  business_start=time(9,0)
  business_end=time(21,0)
  # time 24 ke hisab sy time samjhta he 
  return (business_start <= now) and  (now<= business_end)
# ***********************************************************

def burger_tool_switch(ctx: RunContextWrapper,agent:Agent,) -> bool:
  if ctx.context == "burger":
    return True
  return False

def pizza_tool_switch(ctx: RunContextWrapper,agent:Agent,) -> bool:
  if ctx.context == "pizza":
    return True
  return True

def close_shop_switch(ctx: RunContextWrapper,agent:Agent,) -> bool:
  """enable shop_close tool only when shop is closed """
  return not is_business_hours()
  
# ***********************************************************

# Create the Agent with the improved instructions and output type

@function_tool(is_enabled=burger_tool_switch)
def burger_order(input: str) -> str:
  """ provide an update for the status of the user burger order"""
  return f"your burger is cooking please w8 for 10 minutes "

@function_tool(is_enabled=pizza_tool_switch)
def pizza_order(input: str) -> str:
  """ provide an update for the status of the user pizza order"""
  return f"your pizza is cooking please w8 for 15 minutes "

# ***********************************************************
@function_tool(is_enabled=close_shop_switch)
def shop_close()->str:
  """ return a standard shop closed notice"""
  return f"our shop is closed please comeback later shop is closed on 9pm"
# ***********************************************************
MY_order_agent = Agent(
   model="gpt-4.1-mini",
   name="order taker manager",
   instructions="you are a order taker manager for a food restaurant always first check time of shop_close tool always use available tools provided  to you if tha shop_tool is available use it immediately  never response with your  own text always use a tools ",
   tools=[burger_order, pizza_order, shop_close],
   model_settings=ModelSettings(temperature=0.3,tool_choice="required"),
)
