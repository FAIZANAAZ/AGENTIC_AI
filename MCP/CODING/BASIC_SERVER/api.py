import requests as requests
import rich



url="http://127.0.0.1:8000/mcp"
headerss={
  "Accept":"application/json,text/event-stream",
  "Content-Type":"application/json"}

body={
    "jsonrpc":"2.0",
    "method":"tools/list",
    "params":{},
    "id":1    
    
}

result=requests.post(url,    headers=headerss,    json=body)

for item in result.iter_lines():
  rich.print(item)