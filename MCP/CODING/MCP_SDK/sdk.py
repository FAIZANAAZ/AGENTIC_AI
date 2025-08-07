import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, enable_verbose_stdout_logging
import rich
from agents.mcp import MCPServerStreamableHttp, MCPServerStreamableHttpParams


# ***********************************************************

load_dotenv()  
enable_verbose_stdout_logging()

async def main():
    http_server = MCPServerStreamableHttp(params=MCPServerStreamableHttpParams(url="http://127.0.0.1:9002/mcp"))
  
    async with http_server:
        agent = Agent(
            model="gpt-4.1-mini",
            name="triage agent",
            instructions="you are a helpful assistant",
            mcp_servers=[http_server]
        )
        
        # Agent ko yahan define kar rahe hain takay server connect ho jaye aur baad mein tools mil sakein
        ans = Runner.run_sync(agent, input="list all tools and resources and also prompt")
        rich.print(ans.final_output)

# Agar event loop already chal raha ho to
try:
    asyncio.get_event_loop().run_until_complete(main())
except RuntimeError:
    asyncio.run(main())
