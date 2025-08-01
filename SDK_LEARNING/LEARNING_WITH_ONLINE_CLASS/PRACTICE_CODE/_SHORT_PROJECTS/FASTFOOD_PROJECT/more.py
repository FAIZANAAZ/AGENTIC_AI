import json
from typing import Literal, Optional
from unittest import result
from dotenv import load_dotenv
from agents import Agent, Handoff, RunContextWrapper, Runner, function_tool, enable_verbose_stdout_logging
from pydantic import BaseModel, Field
import rich
from agents.extensions import handoff_filters
from order import MY_order_agent

# ***********************************************************
# Load environment variables and enable logging
load_dotenv()  # Load environment variables from .env file
# enable_verbose_stdout_logging()
# ***********************************************************

# ***********************************************************
# Revised Pydantic data model with improved field descriptions
class Order_Checker(BaseModel):
    is_order: bool = Field(
        description=(
            "True if the user's message is an order request for pizza or burger. "
            "False if the message is about anything else, "
            "such as general inquiries, complaints, or non-food-related topics. "
            "Respond true ONLY for clear pizza or burger orders."
        )
    )
    quantity: int = Field(
        default=0,
        description=(
            "The total number of pizzas and/or burgers explicitly requested by the user. "
            "Specify 0 if no quantity is mentioned or if the request is not a food order."
        )
    )
    order_type: Literal["pizza", "burger", None] = Field(
        default=None,
        description=(
            "Set to 'pizza' if the order is for pizza, 'burger' for burger. "
            "Use None if the user's request is not a direct order for either food item."
        )
    )
    reason: str = Field(
        description=(
            "If the request is NOT an order for pizza or burger, summarize the user's intent "
            "(e.g., requesting support, providing feedback, or asking a non-food question). "
            "Otherwise, briefly describe the food order."
        )
    )
    user_questions: str = Field(
        description=(
            "Copy-and-paste the user's exact message here to preserve the original inquiry or order."
        )
    )

# ***********************************************************
# Improved system instructions string that follows GPT-4.1 prompting best practices
SYSTEM_INSTRUCTIONS = """
You are a helpful, accurate triage agent for a fast food restaurant that ONLY handles queries related to pizza and burgers. Always strictly follow these instructions:

- Recognize and process only pizza and burger orders, or questions directly about pizza and burgers.
- For all other topics—including general customer support, feedback, or other menu items—summarize the request and do not attempt to process as an order.
- Return your response in the exact Order_Checker output format.
- If the user's request is ambiguous, err on the side of caution: only classify as an order if the intent is clear and specific.
- Do NOT process orders for anything other than pizza or burger. Orders for drinks, sides, or general inquiries should NOT be labeled as orders.
- Reflect on your answer before finalizing: confirm that your output matches both the user's message and these criteria.
- Repeat key rules if needed, and provide precise output without explanations outside of the model output format.
"""

# ***********************************************************
# Create the Agent with the improved instructions and output type
main_agent = Agent(
    model="gpt-4.1-mini",
    name="triage agent",
    instructions=SYSTEM_INSTRUCTIONS,
    output_type=Order_Checker,
)

# ***********************************************************
# Example runnable code for testing

    # Example user message
input_user=input("Enter your message:")    
test_input = input_user

# Run the agent synchronously with the input
ans = Runner.run_sync(main_agent, test_input)
rich.print(ans.final_output)

if ans.final_output.is_order==True:
    MY_order_agent_output=Runner.run_sync(MY_order_agent,input=ans.to_input_list(),context=ans.final_output)
    rich.print(MY_order_agent_output.final_output)
# Print the structured output from the agent
    
    
   
    
# ***********************************************************
