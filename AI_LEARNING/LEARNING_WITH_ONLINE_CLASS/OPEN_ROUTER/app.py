import os
from dotenv import load_dotenv
from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled 

from agents.extensions.models.litellm_model import LitellmModel
load_dotenv()
set_tracing_disabled(disabled=True)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY :
    raise Exception("OPEN_ROUTER_API_KEY is not set in the environment variables.")

# ye agent ko bnaya he

agent = Agent(
    model=LitellmModel(
        model="gemini/gemini-2.0-flash",
       api_key=GEMINI_API_KEY
        
        ),
    name="my agent",
    instructions="you are helpful assistant",
)

# **************ye agent ko chalaya he
res=Runner.run_sync(agent, "hello chat ")
print(res.final_output)







# ******** run uv add openai-agents
# agr error ayga to ye line chalayenge
# $Env:PYTHONUTF8 ='1'  
# python -X utf8 app.py