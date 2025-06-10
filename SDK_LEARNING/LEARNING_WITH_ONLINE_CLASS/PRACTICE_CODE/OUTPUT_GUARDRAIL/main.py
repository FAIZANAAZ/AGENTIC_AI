import asyncio
from dotenv import load_dotenv
from agents import Agent, OutputGuardrailTripwireTriggered ,Runner,output_guardrail,RunContextWrapper,GuardrailFunctionOutput
from pydantic import BaseModel

load_dotenv()


class MessageOutput(BaseModel):
    response: str
    
   
class GuardrailOutput(BaseModel):
    is_prime_minister: bool
    Reason: str
    
# /ye agent ke liye he gruadrail waly ismy ye ayga ke priminiter ke barey mein koi bhi sawal he or kiya he check kryga     
      
guardrail_agent = Agent(
    name="Prime Minister Guardrail Agent",
    model="gpt-4.1-mini",
    instructions="You are a guardrail agent that prevents the main agent from answering questions about the Prime Minister of Pakistan.",
    output_type=GuardrailOutput
)    
    
@output_guardrail
async def prime_minister_guardrail(ctx:RunContextWrapper,agent:Agent,output:MessageOutput)->GuardrailFunctionOutput:
    # ctx me input ata he 
    
    result = await Runner.run(guardrail_agent, output.response, context=ctx.context)
    """ye prime miniter ke hawaly ke koi ans nhi dega hm rok rhy hen ans ko agent ke"""
    return GuardrailFunctionOutput(
         output_info=result.final_output,
         tripwire_triggered=result.final_output.is_prime_minister
    )


agent=Agent(
    name="Test Agent",
    model="gpt-4.1-mini",
    instructions="you are a helpful assistant",
    output_type=MessageOutput,
    output_guardrails=[prime_minister_guardrail]
    
)
    # isko bhi hmny wahi de diya  taky structure out ho same 
# ////////////////

async def main():
   try:
        result = await Runner.run(agent, "Who is the Prime Minister of Pakistan?")
        print(result.final_output.response)
   except OutputGuardrailTripwireTriggered as e:
        print("Guardrail tripwire triggered:", e)
        
       
    
    
if __name__ == "__main__":
    asyncio.run(main())    