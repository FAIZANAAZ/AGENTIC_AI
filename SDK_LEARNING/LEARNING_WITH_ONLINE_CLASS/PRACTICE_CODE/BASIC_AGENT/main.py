import os
from dotenv import load_dotenv
from agents import Agent, RunConfig,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled


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

# ***********************************************************
def main():
    
  ans=Runner.run_sync(
         agent,
        "What is the capital of pakistan?"
    )
  print(ans.final_output)
main()  
# ***********************************************************
# ///////////////////////////////////////////////////////////

# 2. RUN LEVEL

# gemini_api_key = "AIzaSyAbpBootC7bPNAQ8JsfbBWnpGfzOOzE7ak"

# #Reference: https://ai.google.dev/gemini-api/docs/openai
# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=external_client
# )

# config = RunConfig(
#     model=model,
#     tracing_disabled=True
# )

# agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant")

# result = Runner.run_sync(agent, "Hello, how are you.", run_config=config)

# print(result.final_output)

# # ///////////////////////////////////////////////////////////
# # GLOBAL

# from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api

# gemini_api_key = "AIzaSyAbpBootC7bPNAQ8JsfbBWnpGfzOOzE7ak"
# set_tracing_disabled(True)
# set_default_openai_api("chat_completions")

# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )
# set_default_openai_client(external_client)

# agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant", model="gemini-2.0-flash")

# result = Runner.run_sync(agent, "Hello")

# print(result.final_output)


# Pehla tareeqa
# (Async method) mein asynchronous execution hota hai, iska matlab yeh task block nahi hota aur non-blocking hota hai. Yeh direct agent creation
# ka tareeqa hai, jisme aap ek agent ko create karke usse ek task run karwa rahe ho.

# Doosra tareeqa
# mein RunConfig ka use kiya gaya hai taake multiple agents ko manage kiya ja sake. Isme configuration ko zyada control kiya gaya hai,
# lekin yeh synchronous hai, matlab ek agent ke baad doosra agent run hoga.

# Teesra tareeqa 
# mein global configuration ka use kiya gaya hai. Yahan par aap ek hi client ko multiple agents ke liye bar bar use kar sakte ho,
# jo scalable aur reusable approach hai. Agar aapko kai agents ko manage karna ho, toh global configuration best option hai.


# ///////////////////////////////////////////////////////////



    