from dotenv import load_dotenv
from agents import Agent, Runner
from pydantic import BaseModel
import rich

class MyAgent(BaseModel):
    name: str
    age: int
    message: str
    is_human: bool
    
class weather(BaseModel):
    location: str
    temperature: float
    summary: str    
    
#  structure aoutput ak schema ki trha hota he ke is form me ans ay
# hmary pas output is form me ayga    yani name age osky ilawa koch ayga nhi 
# isy hmy handle krna easy hoga ke jesy if else lga den ke agr name ho faiza ke braber to hi khna ya koch bhi 
# wesy weather agy zada he 20 sy to cold likho print krky 

load_dotenv()

db=[]

agent = Agent(
    model="gpt-4.1-nano",
    name="my-agent",
    instructions="always use user input to answer in structure of output",
    output_type=weather
)

result=Runner.run_sync(agent, "what is the weather in karachi?")
db.append(result.final_output.model_dump())
# print(result.final_output.model_dump())
# model_dump() se hmary pas output ki sari fields ayengi object ki form me ayga
rich.print(db)




