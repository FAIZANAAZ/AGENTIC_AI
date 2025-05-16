from fastapi.testclient import TestClient
# ye rout chalny ke liye 
from main import app, hello_message

client = TestClient(app)

def test_hello_message():
    response = client.get("/")
    assert response.status_code == 200
    assert hello_message() == {"name":"faiza", "age":22}
    
    
    #ye cheq kr rha he  