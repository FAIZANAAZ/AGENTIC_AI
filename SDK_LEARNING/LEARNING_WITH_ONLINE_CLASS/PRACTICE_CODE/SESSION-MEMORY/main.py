
from dotenv import load_dotenv

from agents import Agent, Runner, SQLiteSession
import rich


load_dotenv()  

memory=SQLiteSession(session_id="conversation_134",db_path="test.dp")

#memory Sy wo hm jitny bhi runner pas krden to har runner phly waly runner ka Kam yad rkhyga 

#or dp_path me Jo name dengy os name ki file bb jaygi or osmy data store ho jayga runner Wala

    

# ***********************************************************
agent=Agent(
  model="gpt-4.1-mini",
  name="Account Service Agent",
  instructions=""" YOU ar a helpful assistant
  """
)


# ***********************************************************
ans=Runner.run_sync(agent, "iam faiza naaz" ,session=memory)
# session=memory lazmy pass krna ho ga
rich.print(ans.final_output)
  
ans2=Runner.run_sync(agent, "what is your name", session=memory)
rich.print(ans2.final_output)  