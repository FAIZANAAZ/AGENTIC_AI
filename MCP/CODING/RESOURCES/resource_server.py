from mcp.server.fastmcp import FastMCP
import uvicorn

# Initialize MCP server
mcp = FastMCP(name="faiza_mcp", stateless_http=True)

# ******************************************************************

resource_data={
    "video":"https://www.youtube.com/watch?v=QH2_TGUlwu4",
    "image":"https://i.ytimg.com/vi/QH2_TGUlwu4/maxresdefault.jpg"
}
url="docs://document"
@mcp.resource( uri=url) 
def resource_func():
    return resource_data


# Initialize the MCP app
mcp_app = mcp.streamable_http_app()

# Run the server using uvicorn
if __name__ == "__main__":
    uvicorn.run(mcp_app, host="127.0.0.1", port=8000)
