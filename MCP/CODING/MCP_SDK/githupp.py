import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, Runner, enable_verbose_stdout_logging
import rich
from agents.mcp import MCPServerStreamableHttp, MCPServerStreamableHttpParams


# ***********************************************************

load_dotenv() 
GITHUP_PAT=os.getenv("GITHUP_PAT") 
enable_verbose_stdout_logging()

async def main():
    http_server = MCPServerStreamableHttp(params=MCPServerStreamableHttpParams(url="http://127.0.0.1:9002/mcp",
     headers={"Authorization": f"Bearer {GITHUP_PAT}" }))                                                                       
  
    async with http_server:
        agent = Agent(
            model="gpt-4.1-mini",
            name="triage agent",
            instructions="you are a helpful assistant",
            mcp_servers=[http_server]
        )
        
        # Agent ko yahan define kar rahe hain takay server connect ho jaye aur baad mein tools mil sakein
        ans = Runner.run_sync(agent, input="make a new repo of name 'test_mcp'")
        rich.print(ans.final_output)

# Agar event loop already chal raha ho to

asyncio.run(main())
