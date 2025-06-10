import asyncio
import os
from dotenv import load_dotenv
from agents import Agent , Runner ,set_tracing_disabled,OpenAIChatCompletionsModel ,AsyncOpenAI
from openai.types.responses import ResponseTextDeltaEvent
import chainlit as cl
import rich


load_dotenv()
set_tracing_disabled(disabled=True)

OPEN_ROUTER_API_KEY= os.getenv("OPEN_ROUTER_API_KEY")

if not OPEN_ROUTER_API_KEY:
    raise ValueError("OPEN_ROUTER_API_KEY is not set in the environment variables. Please set it and try again.")

# ***********************************************************

client = AsyncOpenAI(
    api_key=OPEN_ROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)
agent = Agent(
    model=OpenAIChatCompletionsModel(model="deepseek/deepseek-r1:free",openai_client=client),
    name="streaming_agent",
    instructions="your are helpfull assistant"
 
)

# ***********************************************************
history:list=[]
@cl.on_message
async def main(message: cl.Message):
    
    user_question = message.content

    history.append({"role":"user","content":user_question})
    
    
    response_message = cl.Message(content="")
    
    result =Runner.run_streamed(agent,history)
    
   

    # run stramed ak oop he jo bar bar chalta he bar bar chalta he or sath sath answer bhi krta jaa he 
    async for item in result.stream_events():
        if item.type=="raw_response_event" and isinstance(item.data,ResponseTextDeltaEvent):   
            await response_message.stream_token(item.data.delta)
            # end or flash stream_token khod sanbhalta he 
            rich.print(item.data.delta, end="", flush=True )
    
    
    
# if __name__ == "__main__":
#     asyncio.run(main())