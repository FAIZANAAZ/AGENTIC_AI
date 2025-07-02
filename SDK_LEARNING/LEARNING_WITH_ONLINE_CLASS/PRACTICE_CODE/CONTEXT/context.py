import os 
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool ,RunContextWrapper,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled
import rich
from pydantic import BaseModel

load_dotenv()
set_tracing_disabled(disabled=True)
Gemini_API_KEY= os.getenv("Gemini_API_KEY")
# ***********`  ******`********`***************`********`********`********`********`********`********`********`********
class User_Info(BaseModel):
    name: str
    age: int 
    alive: bool
    roll_no: str
# ***********`  ******`********`***************`********`********`********`********`********`********`********`********
my_info=User_Info(
    name="Faiza Naaz",
    age=19,
    alive=True,
    roll_no="12345"
)
# ***********`  ******`********`***************`********`********`********`********`********`********`********`********
# llm context
@function_tool
def get_user_info( wrapper: RunContextWrapper[User_Info]) -> str:
    """
    This function returns the user information.
    """
    return f"user roll no is {wrapper.context.roll_no}  user is alive {wrapper.context.alive}"
# ***********`  ******`********`***************`********`********`********`********`********`********`********`********
def dynamic_instruction(wrapper: RunContextWrapper[User_Info], agent: Agent[User_Info]) -> str:
    wrapper.context.name = "aLIZA NAaz"
    # SY OVER RIDE HO JAYGA NAME HM SARY PERMETER KO CHNAGE KR SKTY HEN
    return f"user name is {wrapper.context.name} user age is {wrapper.context.age} whenever user ask roll number you use given toll get_user_info and user roll no is {wrapper.context.roll_no} and user is alive {wrapper.context.alive}"
# ***********`  ******`********`***************`********`********`********`********`********`********`********`********

client = AsyncOpenAI(
    api_key=Gemini_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
    

agent= Agent[User_Info](
    name="my_agent",
    instructions=dynamic_instruction,
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash-lite",openai_client=client),
    tools=[get_user_info]
)

# ***********`  ******`********`***************`********`********`********`********`********`********`********`********


llm_result=Runner.run_sync(agent, "what is the roll no of user",context=my_info)

rich.print(llm_result.final_output)

