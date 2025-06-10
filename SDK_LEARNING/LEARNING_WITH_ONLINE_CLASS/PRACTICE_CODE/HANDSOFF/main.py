
from dotenv import load_dotenv
from agents import Agent ,Runner

load_dotenv()

billing_agent = Agent(
    model="gpt-4.1-nano",
    name="billing_agent",
    instructions="You are a billing agent. Handle all billing-related queries and tasks. If the task is not related to billing, ask for clarification.",
    handoff_description="you are an expert in billing and can handle all billing-related tasks",
    # ye hm har agent ko dengy jisko dkh kr main agent faisla kryYGA
)

refund_agent= Agent(
    model="gpt-4.1-nano",
    name="refund_agent",
    instructions="You are a refund agent. Handle all refund-related queries and tasks. If the task",
    handoff_description="you are an expert in refunds and can handle all refund-related tasks",
)

triage=Agent(
    model="gpt-4.1-nano",
    name="trige_agent",
    instructions="yoe delegate task to appropriate agent according to the task type. If the task is not recognized, ask for clarification.",
    handoffs=[billing_agent, refund_agent]
    # ye main agent he 
)

# **********************************
result = Runner.run_sync(triage, "I want to refund my 100$ of billing")
print(result.final_output)
# **********************************a