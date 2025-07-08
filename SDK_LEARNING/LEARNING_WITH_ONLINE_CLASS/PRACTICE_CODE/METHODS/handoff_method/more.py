import os
from dotenv import load_dotenv
from agents import Agent, RunConfig,Runner,OpenAIChatCompletionsModel,AsyncOpenAI, function_tool, handoff,set_tracing_disabled,enable_verbose_stdout_logging
import rich
from agents.extensions import handoff_filters 


enable_verbose_stdout_logging()
# ***********************************************************
load_dotenv()
set_tracing_disabled(disabled=True)

Gemini_API_KEY = os.getenv("Gemini_API_KEY")

if not Gemini_API_KEY :
    raise ValueError("Gemini_API_KEY is not set in the environment variables. Please set it and try again.")

# ***********************************************************

client=AsyncOpenAI(
    api_key=Gemini_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
# ***********************************************************

@function_tool
def greeting():
    return "Hello, how can I assist you today?"

customer_agent=Agent(
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash-lite",openai_client=client),
    name="customer agent",
    instructions="you are a customer support agent.",
    handoff_description="if you are unable to answer the question, please handoff to the hanoff agent.",
    tools=[greeting],  # ye tools optional hen   
)
# ***********************************************************

modify_agent = handoff(
    agent=customer_agent,  # required property
    tool_name_override="customer_support_agent",
    input_filter=handoff_filters.remove_all_tools,
    is_enabled=False  # optional; if set to False, the agent will not handoff
)

# ismy hm agent ki properties ko override krty hen
# ***********************************************************


agent =Agent(
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash-lite",openai_client=client),
    name="practice agent",
    instructions="you are a helpful agents.",
    handoffs=[customer_agent],
    tools=[greeting]
    
)

# ***********************************************************

ans=Runner.run_sync(agent,"i need customer support?")
rich.print(ans.final_output)
  

# ***********************************************************
# ///////////////////////////////////////////////////////////
