import os
from dotenv import load_dotenv
from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled
load_dotenv()

set_tracing_disabled(disabled=True)
OPEN_AI_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")

if not OPEN_AI_API_KEY :
    raise Exception("OPEN_ROUTER_API_KEY is not set in the environment variables.")

# ye agent ko bnaya he
client = AsyncOpenAI(
     api_key=OPEN_AI_API_KEY,
     base_url="https://openrouter.ai/api/v1",
)

agent = Agent(
    model=OpenAIChatCompletionsModel(
       
        openai_client=client,
        model="deepseek/deepseek-chat-v3-0324:free",
        
    ),
    name="my agent",
    instructions="you are helpful assistant",
)

# **************ye agent ko chalaya he
res=Runner.run_sync(agent, "hello chat ")
print(res.final_output)







# ******** run uv add openai-agents[litellm]