
from typing import Literal
from dotenv import load_dotenv
from agents import Agent, FunctionToolResult, RunContextWrapper, Runner, ToolsToFinalOutputResult, enable_verbose_stdout_logging, function_tool
from pydantic import BaseModel, Field
import rich




# ***********************************************************
enable_verbose_stdout_logging()


load_dotenv()  

# ***********************************************************
def tool_beh(ctx:RunContextWrapper,my_list:list[FunctionToolResult])->ToolsToFinalOutputResult:
    
    return ToolsToFinalOutputResult(is_final_output=True,final_output=my_list[0].output)
  
# ***********************************************************


@function_tool
def weather_tool():
    return f"karachi weather is karachi"

@function_tool
def time_tool():
    return "karachi time is 6 am"

agent =Agent(
    model="gpt-4.1-mini",
    name="triage agent",
    instructions="you ara a helpfull agent.",
    tools=[weather_tool,time_tool],
    # tool_use_behavior="stop_on_first_tool",
    # ismy wo sary tools chlayga lekin ans sirf first tool ka return krdega ye max turn 1 bhi ho skta he or ye jesa tool me ans he same dega khod koch add krky nhi dega hi wagera 
    
    # tool_use_behavior="run_llm_again",
    # ye 2 bar llm ke loop ko chlayga or tool ke ans ko modify krky osko khos ans dega
    
    # tool_use_behavior=["weather_tool"]
    #   is trha deny sy wo is tool ko run nhi kryga error dega program rok jayga agent hi rok jayga 
    
    # tool_use_behavior=StopAtTools   
    # ye chalta he or ans deta he phir rok deta he
    
    tool_use_behavior=tool_beh
    # ismy ye hoga ke hm jo bhi tools use krlen lekin hmny jo ye funtion bnaya he joky finalout ka he ye ans ko overide krta he yani koi bhi tool chala oska ans ayga lekin llm os ans ko is function ke output sy overide krdega or isi function wala ans nazr ayga ye wala nhi ayga 
    
   
)
# tool use behaviuor ko hm ak hi time pr ak hi method ko use kr skty hen sb sath nhi kr skty 
    
        

# ***********************************************************

ans=Runner.run_sync(agent,input="hi what is weather of karachi")
rich.print(ans.final_output)
  




# ***********************************************************
# ///////////////////////////////////////////////////////////
