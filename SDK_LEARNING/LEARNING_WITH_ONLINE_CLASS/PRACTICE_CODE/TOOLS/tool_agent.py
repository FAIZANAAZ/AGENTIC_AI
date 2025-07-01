from agents import Agent, ModelSettings, Runner,OpenAIChatCompletionsModel , AsyncOpenAI,RunResult,set_tracing_disabled
import os
from dotenv import load_dotenv
import rich



load_dotenv()
Gemini_API_KEY= os.getenv("Gemini_API_KEY")

set_tracing_disabled(disabled=True)

# ******************************************************
 



client = AsyncOpenAI(
    api_key=Gemini_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

# ******************************************************
support_agent=Agent(
    name="support_agent",
    model=OpenAIChatCompletionsModel(openai_client=client,model="gemini-2.0-flash-lite"),
    instructions="you help user with post-purchase support, including order status, returns, and refunds.",
    handoff_description="support agent to assist users with their post-purchase and return products queries and issues."
)
# ******************************************************
shoping_agent=Agent(
    name="shoping_agent",
    model=OpenAIChatCompletionsModel(openai_client=client,model="gemini-2.0-flash-lite"),
    instructions="you assist user to finding products and making purchases  decisions.",
    handoff_description="a shoping agent to help users with their shopping needs."
)
# ******************************************************

# name hm small lateme ina space ke rakhty hen

agent=Agent(
    name="triage_agent",
    model=OpenAIChatCompletionsModel(openai_client=client,model="gemini-2.0-flash-lite"),
    instructions="you are a triage agent,you delegate task to appropriate agent or use appropriate given tools ."
    "when user ask for support related to order status, returns, or refunds, delegate to the support agent. "
    "when user ask for shopping assistance, delegate to the shopping agent."
    "you never reply on our own, always delegate to the appropriate agent or tool.",
    tools=[
        support_agent.as_tool(
            tool_name="support_agent",
            tool_description="you help user with post-purchase support , including order status , returns and refunds, always START your reply with this 😪 emoji in your reply "
        ),
        shoping_agent.as_tool(
            tool_name="shoping_agent",
            tool_description="you assist user to finding products and making purchases decisions, always START your reply with  this 🛒 emoji in your reply."
        )
    ],
    # model_settings=ModelSettings(tool_choice="auto")
    # ye by default bhi auto hota he agr hm required krengy to wo lazim use krega tool ornone krengy to sktip krdega tool
    
    # isko minimum 2 token chiye hoty hen or max 10 1me ye nhi kr payga handle 
)
# ******************************************************

result:RunResult = Runner.run_sync(agent, "i want to return my order .")

rich.print(result.final_output)