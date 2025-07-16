from typing import Any
from dotenv import load_dotenv
from agents import Agent, InputGuardrailTripwireTriggered, GuardrailFunctionOutput, RunContextWrapper, Runner, enable_verbose_stdout_logging, function_tool,  output_guardrail
from pydantic import BaseModel
import rich

enable_verbose_stdout_logging()

load_dotenv()

@function_tool
def weather_info(city: str):
    """this function is about to tell weather report"""
    return f"{city} weather is sunny"

class Weather_check(BaseModel):
    is_weather_check: bool

# ****************************************
output_guardrail_agent = Agent(
    name="output_guardrail_agent",
    instructions="always check user is asking about weather you always check if agent response has weather or any information related to weather",
    model="gpt-4.1-mini",
    output_type=Weather_check
)
# ****************************************

@output_guardrail
async def weather_check(wraper: RunContextWrapper, agent: Agent, output: Any) -> GuardrailFunctionOutput:
    # Use the provided agent and output as input for the guardrail check
    response = await Runner.run(starting_agent=output_guardrail_agent, input=output, context=wraper.context)
    
    # Check the guardrail output, ensuring `is_weather_check` is True or False
    tripwire_triggered = response.final_output.is_weather_check
   
    return GuardrailFunctionOutput(
        output_info="Weather check completed.",
        tripwire_triggered=tripwire_triggered
    )

# ****************************************
agent = Agent(
    model="gpt-4.1-mini",
    name="triage agent",
    instructions="you are a helpful agent. whenever user asks for weather, use the weather_info function to get the weather report",
    tools=[weather_info],
    output_guardrails=[weather_check]
)

# ***********************************************************
ans = Runner.run_sync(agent, input="who are U ")

# Output the final result of the agent's response
rich.print(ans.final_output)
