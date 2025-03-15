import asyncio
import os
import chainlit as cl
from agents import Agent, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

gemini_api_key = os.getenv("GEN_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

# config
config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

async def main():
    global agent1  # Declare agent1 as global to avoid reference error
    agent1 = Agent(
        name="Assistant",
        instructions="You are a helpful Assistant.",  # Corrected spelling of "Assistant"
        model=model
    )

    result = await Runner.run(agent1, "who is the founder of Pakistan?", run_config=config)
    print(result.final_output)

@cl.on_chat_start
async def handle_chat_start():  # Corrected function name from handle_chart_start to handle_chat_start
    cl.user_session.set("history", [])
    await cl.Message(content="Hello, I am Panaversity support Agent. How can I assist you?").send()  # Added send() to send the message

@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})
    result = await Runner.run(
        agent1,
        input=history,
        run_config=config
    )
    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)
    await cl.Message(content=result.final_output).send()

asyncio.run(main())


# uv run chainlit run main.py -w 