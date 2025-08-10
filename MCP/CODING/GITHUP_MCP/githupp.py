import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, Runner, enable_verbose_stdout_logging
import rich
from agents.mcp import MCPServerStreamableHttp, MCPServerStreamableHttpParams

load_dotenv()
GITHUP_PAT = os.getenv("GITHUP_PAT")
enable_verbose_stdout_logging()

async def main():
    http_server = MCPServerStreamableHttp(params=MCPServerStreamableHttpParams(
        url="https://api.githubcopilot.com/mcp/",
        headers={"Authorization": f"Bearer {GITHUP_PAT}"}
    ))

    async with http_server:
        agent = Agent(
            model="gpt-4.1-mini",
            name="mcp agent",
            instructions="you are a helpful assistant",
            mcp_servers=[http_server]
        )
        # Runner.run_sync is synchronous, don't use inside asyncio.run()
        # Instead, use the asynchronous version Runner.run
        ans = await Runner.run(agent, input="make a new repo of name 'test_mcp✅' you can do this because ia use mcp server of githup in your toll so please make auto repo of name 'test_mcp✅'")
        rich.print(ans.final_output)

if __name__ == "__main__":
    asyncio.run(main())
