# MCP SERVER
from mcp.server.fastmcp import FastMCP, Context
from mcp.types import SamplingMessage, TextContent
import rich

app = FastMCP()

# SAMPLING
@app.tool()
async def create_story(ctx: Context ,topic: str):
    # yha hny ak toll bnaya he jo ctx lga or osmy ayga haamara sawal clint sy

    response = await ctx.session.create_message(
        # yha hmny client sy mngwaya he or bheja bi he message ki zariye
        messages = [SamplingMessage(
            role="user",
            content= TextContent(type="text", text=f"write a short story in hinglish of two lines on {topic}")
        )],
        max_tokens=100
    )

    rich.print("response: 🍎",response.content.text)

    return response.content.text

my_mcp = app.streamable_http_app()
