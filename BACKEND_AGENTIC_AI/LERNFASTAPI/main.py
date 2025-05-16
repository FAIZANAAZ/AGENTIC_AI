from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello_message():
    return  {"name":"faiza", "age":22}




# ******************************
from pydantic import BaseModel

class ChatInput(BaseModel):
    message: str
    
    
@app.post("/post")
def post_message(input: ChatInput):
    
    return {"message": "Hello, World!"}    