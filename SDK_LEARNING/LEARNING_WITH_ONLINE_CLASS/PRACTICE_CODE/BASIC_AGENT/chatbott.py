import os
from dotenv import load_dotenv
from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled
import chainlit as cl

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


agent =Agent(
    model=OpenAIChatCompletionsModel(model="deepseek/deepseek-r1:free",openai_client=client),
    name="practice agent",
    instructions="you are a helpful agents.",   
)

history :list= []
@cl.on_message
async def main(message: cl.Message):
    question =message.content
    history.append({"role": "user", "content": question})
    
    answer = Runner.run_sync(agent, history)
    # or jo agent ans kryga wo answer me aa jayega yni Runner.sync m or final output sy hmm dekhlengy 
    
    history.append({"role": "assistant", "content": answer.final_output})
    print(answer.final_output)
    
    # ab hm chahry hen ke hm is ans ko ui pr dikhaen 
    await cl.Message(content=answer.final_output).send()

