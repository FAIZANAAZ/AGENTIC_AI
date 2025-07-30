import asyncio
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamablehttp_client
import rich

async def main():
    # Set timeout to 10 seconds (adjust as needed)
    async with streamablehttp_client(url="http://127.0.0.1:8000/mcp", timeout=10) as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            # Get all tools
            all_tools = await session.list_tools()

            # Debugging: Print the structure of all_tools
            rich.print(all_tools)

            # Loop through the tools and access their names
            for tool in all_tools:
                # Check the type of 'tool' to debug
                rich.print(f"Tool type: {type(tool)}")
                if isinstance(tool, tuple):
                    rich.print(f"Tool tuple contents: {tool}")
                else:
                    rich.print(tool.name)

            # Call the 'hello_function' tool
            tool_result = await session.call_tool(
                name="hello_function",
                arguments={"name": "faiza"}
            )
            rich.print(tool_result.content[0].text)

# Run the main function
asyncio.run(main())
