from typing import Any
from dotenv import load_dotenv
from agents import Agent,InputGuardrailTripwireTriggered, GuardrailFunctionOutput, RunContextWrapper,Runner, TResponseInputItem, enable_verbose_stdout_logging, input_guardrail
from openai import BaseModel
import rich




# ***********************************************************
class Prime_minister_Check(BaseModel):
    is_prime_minister:bool
# ***********************************************************



enable_verbose_stdout_logging()


load_dotenv()  

guardrail_agent=Agent(
    model="gpt-4.1-mini",
    name="guadrrail_agent",
    instructions="always check user is aasking about prime minister",
    output_type=Prime_minister_Check
)
# ********************************
@input_guardrail
async def prime_minister(wraper:RunContextWrapper[None],agent:Agent , input:str |list[TResponseInputItem])->GuardrailFunctionOutput:
     response=await Runner.run(guardrail_agent,input,context=wraper.context)
     return GuardrailFunctionOutput(
         output_info=response.final_output,
         tripwire_triggered=response.final_output.is_prime_minister
     )

# *******************************
second_agent=Agent(
    model="gpt-4.1-mini",
    name="second agent",
    instructions="you are a helpful agents. wehenever user ask about president you also add information about primenister for example xyz is the prime meninster ",
    input_guardrails=[prime_minister]
)

agent =Agent(
    model="gpt-4.1-mini",
    name="triage agent",
    instructions="you are a helpful agents.",
    input_guardrails=[prime_minister],
    handoffs=[second_agent]
    
)
      
        

# ***********************************************************

try:
    ans=Runner.run_sync(agent,input="who i sthe prime miniter of pakistan and handsoff sencod agent")
    rich.print(ans.final_output)
    second_ans=Runner.run_sync(agent,input=ans.to_input_list())
    rich.print(second_ans.final_output)
   
    
except InputGuardrailTripwireTriggered as e:
    print(e,"🙄")    
  

# ***********************************************************
# ///////////////////////////////////////////////////////////
