import asyncio
from dotenv import load_dotenv
from agents import Agent,Runner
import rich
from agents.mcp import MCPServerStreamableHttp ,MCPServerStreamableHttpParams


# ***********************************************************


load_dotenv()  # Load environment variables from .env file
# enable_verbose_stdout_logging()

# ***********************************************************

async def main():
  server_response=MCPServerStreamableHttp(params=MCPServerStreamableHttpParams(url="http://127.0.0.1:8000/mcp"))

  
  async with server_response:
    
    agent =Agent(
        model="gpt-4.1-mini",
        name="triage agent",
        instructions="you are a helpful agents.",
        mcp_servers=[server_response]
        
     )

  # ***********************************************************

    ans= await Runner.run(agent,input="my name is faiza call hello_function")
    rich.print(ans.final_output)
    

asyncio.run(main())
# ***********************************************************
# ///////////////////////////////////////////////////////////
