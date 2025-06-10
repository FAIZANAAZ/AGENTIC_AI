import asyncio
import os
from dotenv import load_dotenv
from agents import Agent , Runner ,set_tracing_disabled,OpenAIChatCompletionsModel ,AsyncOpenAI
from openai.types.responses import ResponseTextDeltaEvent
import rich


load_dotenv()
set_tracing_disabled(disabled=True)

OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")

if not OPEN_ROUTER_API_KEY :
    raise ValueError("OPEN_ROUTER_API_KEY is not set in the environment variables. Please set it and try again.")

# ***********************************************************

client=AsyncOpenAI(
    api_key=OPEN_ROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)
agent=Agent(
    name="streaming_agent",
    instructions="your are help_full assistant",
    model=OpenAIChatCompletionsModel(model="deepseek/deepseek-chat-v3-0324:free", openai_client=client)
)

# ***********************************************************

async def main():
    
    result = Runner.run_streamed(starting_agent=agent, input="what is agent ai sdk")
    

    # run stramed ak oop he jo bar bar chalta he bar bar chalta he or sath sath answer bhi krta jaa he 
    async for item in result.stream_events():
     if item.type=="raw_response_event" and isinstance(item.data, ResponseTextDeltaEvent):   
         
        #  event.data,ResponseTextDeltaEvent ka matlb he jesy hm classs ka instance bnaty hen or osko ak variable me save kr dety hen
        # to hm osko is intance sy chek krty hen ke jis varible me save kiya he owo is  class ka instance he ya nhi
        # event.data variable he ResponseTextDeltaEvent class he or is class ko hmny event.data ke variable me save krwaya he or cheq kiyahe 
       rich.print(item.data.delta, end="", flush=True)
# for loop me async isi liye dala he ke wo await krta rhy or ans krta rhy or wrna wo ak dam sy sb  chalyga or sath chlyga 

if __name__ == "__main__":
    asyncio.run(main())
    
    
# @cl.on_message
# async def main(message: cl.Message):
  