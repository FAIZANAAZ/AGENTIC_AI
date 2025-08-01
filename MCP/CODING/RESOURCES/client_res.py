import asyncio
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamablehttp_client
import rich

async def main():
    # Set timeout to 10 seconds (adjust as needed)
    async with streamablehttp_client(url="http://127.0.0.1:8000/mcp", timeout=10) as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            all_res=await session.list_resources()
            rich.print(all_res)
# Run the main function
asyncio.run(main())
