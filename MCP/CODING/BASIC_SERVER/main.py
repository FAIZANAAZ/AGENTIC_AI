from mcp.server.fastmcp import FastMCP
import uvicorn

# Initialize MCP server
mcp = FastMCP(name="faiza_mcp", stateless_http=True)

# Define hello_function tool
@mcp.tool()
def hello_function(name: str):
    """Hello name Function"""
    return f"HI {name} HOW ARE u "

# Define bay_tool tool
@mcp.tool()
def bay_tool():
    """bay Function"""
    return {"message": "by World"}

# Initialize the MCP app
mcp_app = mcp.streamable_http_app()

# Run the server using uvicorn
if __name__ == "__main__":
    uvicorn.run(mcp_app, host="127.0.0.1", port=8000)
