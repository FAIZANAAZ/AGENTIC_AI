import os
from dotenv import load_dotenv
from agents import Agent , Runner, FileSearchTool 
import chainlit as cl


load_dotenv()
OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")
VECTOR_ID = os.getenv("VECTOR_ID")



# ***********************************************************


agent=Agent(
    model="gpt-4.1-mini",
    name="my_assistant",
    instructions="your are help_full assistant,always use FileSearchTool for information,answer question as concisely as possible",
    tools=[FileSearchTool(
        max_num_results=3,
        vector_store_ids=VECTOR_ID
    )]
    # file tool esy chalyga nhi hmy ak systemkrna hoga phly file ko
    # openai me paltform me dalna hoga osky bad wo ak link dega bna kr 
    # jisy hm file tool me rakh skty hen esy direct file nhi lega wo 
    
    # go https://platform.openai.com/storage 
    # wha hmy file or vector store milyga 
    # sbsy phly hmy vertore store create krna he ak 
    # click on create =>vector store ka ak name dengy koi=>click on chek box
    # phir jaygy hm files ke tab me
    # or phly perpose ko assistent me dalna hoga
    # koi bhi file upload krengy jismy data ho lekin image nhi text file 
    # upload ke button pr click krenge =>name dengy=>file dalengy 
    # ak id file id milygi or ak vector me vector id
    # vector id hm yha lgadengy 
)

# ***********************************************************


    
result = Runner.run_sync(agent, "what is span in tracing")

print(result.final_output)
    


@cl.on_message
async def main(message: cl.Message):
    user_question=message.content
    
    res=Runner.run_sync(agent,user_question)  
    await cl.Message(content=res.final_output).send()  
