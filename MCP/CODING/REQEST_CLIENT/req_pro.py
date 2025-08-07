
import requests
import rich




headers={
    "Accept":"application/json,text/event-stream",
    "Content-type":"application/json"}

        

body={
  "jsonrpc":"2.0"  ,
  "id":1,
  "method":"prompts/get",
  "params":{
    "name":"my_prompt",
    "argUments":{}
   
  }
}

# *****************************        

response=requests.post(
  url="http://localhost:9000/mcp",
  headers=headers,
  json=body
)

for line in response.iter_lines():
        rich.print(line)
        
        
# *****************************        
