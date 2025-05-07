import os
from dotenv import load_dotenv
from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled

load_dotenv()
set_tracing_disabled(disabled=True)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY :
    raise ValueError("OPENROUTER_API_KEY is not set in the environment variables. Please set it and try again.")

# ***********************************************************

client=AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)


agent =Agent(
    model=OpenAIChatCompletionsModel(model="deepseek/deepseek-r1:free",openai_client=client),
    name="practice agent",
    instructions="you are a helpful agents.",   
)

# ***********************************************************
def main():
    
  ans=Runner.run_sync(
        agent,
        "What is the capital of pakistan?"
    )
  print(ans.final_output)
main()  
# ***********************************************************
