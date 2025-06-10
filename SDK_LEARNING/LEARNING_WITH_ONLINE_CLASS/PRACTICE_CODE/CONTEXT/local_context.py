from dotenv import load_dotenv
from agents import Agent, Runner, function_tool ,RunContextWrapper
from dataclasses import dataclass 



load_dotenv()

# ye hmara local context he or local context nhi jata llm ke pas 
@dataclass
class User_Info():
    name: str
    age: int
    location: str  
   
user_information=User_Info("faiza",23,"2")  
    
    
def dynamic_instruction(ctx:RunContextWrapper[User_Info],agent=Agent)->str:
    return f"user name is {ctx.context.name} and user age is {ctx.context.age}"

# hm llm ko khty hen wo helpfull assistence he to wo os hisab sy ans krta he ab hmny osko context ke ander ak dta de diya taky oska use
# krky wo de sky ans lekin ismy local context ka use is trha he ke llm ko simple functions nhi jata osko tool jaty hen hmny kioky is ke oper
# functiontool kA DECORAter nhi lgaya he ye simpl func he python ka to agent ko isy matlb nhi he wo bs instruction me osko rakh dega
# jo is func ke return me he or hmny osmy return me hi data rakh kr pass kr diya he    RunContextWrapper ka perameter dekr kioky jb bhi hm RunContextWrapper
# likhty hen to hm context me any wali har chiz ko access kr skty hen 

# isi liye hm ye khty hen ke ye local context he ye as a tool ja hi nhi rha llm ke pas 
agent=Agent[User_Info](
   model="gpt-4.1-nano",
   name="my_agent",
   instructions=dynamic_instruction,
    
)    

ans=Runner.run_sync(agent,"what is the age of user",context=user_information)
print(ans.final_output)