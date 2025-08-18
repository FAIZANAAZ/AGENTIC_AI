# MCP Sampling Client
import os
import asyncio
from dotenv import load_dotenv
from mcp.client.streamable_http import streamablehttp_client
from mcp.client.session import ClientSession
from mcp.shared.context import RequestContext
from mcp.types import CreateMessageRequestParams, CreateMessageResult, ErrorData, TextContent
from openai import OpenAI
from typing import Any
import rich

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)
# ye open api ko direct mngwany ka tarika he

async def llm_call(context= RequestContext["ClientSession", Any], params= CreateMessageRequestParams,)-> CreateMessageResult | ErrorData:

    server_input = params.messages[0].content.text
# yha hmny server ka sawal lia he
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=server_input
    )

# llm ko bheja he
    llm_response = response.output[0].content[0].text
    #hmny llm ka response nikala he
    return CreateMessageResult(
        role= "assistant",
        content= TextContent(type= 'text', text= llm_response),
        model= "gpt-4.1-mini",
    )
# ye hmny Bheja he server ko return Kiya he
async def main():
# server connect Kiya he taky bhej saken hm ans
    async with streamablehttp_client("http://localhost:9001/mcp/") as (read_stream, write_stream, _):

        async with ClientSession(read_stream, write_stream, sampling_callback=llm_call) as session:
            await session.initialize()

            user_input = input("Enter your topic: ")

            tool_result = await session.call_tool(
                name="create_story",
                arguments={
                    "topic" : user_input
                }
            )

            rich.print(tool_result)


asyncio.run(main())
