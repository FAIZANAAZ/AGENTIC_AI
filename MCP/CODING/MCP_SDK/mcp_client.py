import asyncio
import rich
from mcp.client.streamable_http import streamablehttp_client
from mcp.client.session import ClientSession
# clientsession ak class he jo mcp walo ne di he jismy bnaya bnya client he bs methods call krty jay 

async def main():
  async with streamablehttp_client(url="http://127.0.0.1:9002/mcp") as (read_stream,write_stream,_):
    async with ClientSession(read_stream,write_stream) as session:
      await session.initialize()
      # ye hand shak kiya he yani connection bnaya he 
      
      result_tool_list=await session.list_tools()
      rich.print(result_tool_list)
      
      # ///////////////
    result_tool_call=await session.call_tool()
    rich.print(result_tool_call)
      
      # ///////////////
      
    result_resource_list=await session.list_resources()
    rich.print(result_resource_list)
      
      # ///////////////
      
    result_resource_call=await session.call_resource()
    rich.print(result_resource_call)
      
      # ///////////////
      
    result_prompt_list=await session.list_prompts()
    rich.print(result_prompt_list)
      
      # ///////////////
      
    result_prompt_call=await session.call_prompt()
    rich.print(result_prompt_call)
      
      # ///////////////
      
      
      
      
asyncio.run(main())      