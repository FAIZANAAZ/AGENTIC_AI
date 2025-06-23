from dotenv import load_dotenv
from agents import Agent,Runner,set_tracing_disabled
import rich
import litellm
from agents.extensions.models.litellm_model import LitellmModel

import os
# *************************
set_tracing_disabled(disabled=True)
litellm.disabled_aiohttp_transport = True
load_dotenv()
GEMINI_KEY=os.getenv("GEMINI_KEY")

agent=Agent(
    name="my_agent",
    instructions="you are a helpful assistant",
    model=LitellmModel(model="gemini/gemini-2.0-flash",api_key="your api key"),
)

ans=Runner.run_sync(agent,"")
rich.print(ans.final_output)