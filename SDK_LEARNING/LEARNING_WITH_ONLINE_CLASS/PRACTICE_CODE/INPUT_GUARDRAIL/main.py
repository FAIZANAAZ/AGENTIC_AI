from dotenv import load_dotenv
from agents import Agent, Runner, input_guardrail,RunContextWrapper,TResponseInputItem,GuardrailFunctionOutput,InputGuardrailTripwireTriggered
from pydantic import BaseModel
import asyncio



load_dotenv()

# guardrail mean restruction lgana ke is swal ka ans nhi krna galio ka as mt krna is trha hm input gruardrail sbsy phly lgaty hen taky sawal ay to chack kry or ak end me output guardrail lgaty hen taki output ay to check kry or agar output me kuch galat ay to usay change kr de ouput jany sy phly 

class Slang_Check_Output(BaseModel):
    is_slang: bool
    reasoning:str

guardrail_agent = Agent(
    model="gpt-4.1-nano",
    name="guardrail-agent",
    instructions="Check if the user is using slang in any language",output_type=Slang_Check_Output,
    
)

# ye hmara agent nhi he ye wo agent he jo gruadrail ka he jo wo checking ke liye use kryga 
@input_guardrail
async def slangs_guardrail(ctx: RunContextWrapper[None],agent: Agent, input: str|list[TResponseInputItem])->GuardrailFunctionOutput:
    # ye perameters wagera agent khod handle kryga
  result=await Runner.run(guardrail_agent, input,context=ctx.context)
  return GuardrailFunctionOutput(
      output_info=result.final_output,
      tripwire_triggered=result.final_output.is_slang, 
      # ye check krta he agar slang use hua to tripwire trigger ho jata he
    #   ye input ko samj kr trip krdyga ye asal me important he isko hm ans dety hen yes or no me no pr wo trip yani skip krdega 
  )


async def main():
    
    agent = Agent(
        model="gpt-4.1-nano",
        name="my-agent",
        instructions="you are a helpful assistant",
        input_guardrails=[slangs_guardrail]
    
    )
    # ye hmara agent he 

    try:
     result=await Runner.run(agent, "bastard")
     print(result.final_output)
    except InputGuardrailTripwireTriggered as e:
        print("user is using language slang",e)





if __name__ == "__main__":
   
    asyncio.run(main())