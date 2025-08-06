from mcp.server.fastmcp.prompts import base
from mcp.server.fastmcp import FastMCP
mcp =FastMCP(name="mcp",stateless_http=True)



@mcp.tool()
def hello():
    """function returns greeting message"""
    
    # api call logic
    # database call logic
    
    return "hi "


@mcp.resource(
    uri="docs://documents",
)
def my_resource():
    
    
    return "i am resource"
    

@mcp.prompt()
def my_prompt()->list[base.Message]:
    my_meessage=base.Message(
        Message="hi how are you"
    )
    return [base.Message([my_meessage])]
    
mcp_app=mcp.streamable_http_app()

