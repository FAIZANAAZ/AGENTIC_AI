from fastapi.testclient import TestClient 
# ye rout chalny ke liye 
from main import app, hello_message

client = TestClient(app)

# 100 =information
# 200 =success -> related to the request
# 300  =redirection-> related to the request
# 400 = client error-> related to the request
# 500 = server error -> related to the server
def test_hello_message():
    response = client.get("/")
    assert response.status_code == 200
    assert hello_message() == {"name":"faiza", "age":22}
    
    

def test_call_info():
    response = client.get("/info/test/id=1")
    assert response.status_code == 200
    assert response.json() == {"username": "test","id":1}
    
# is trha sy hm path me jo url me dakty hen oski jha test likhty hen url me hm sath value bhi de dety hen ke ye ans hoga

def test_404():
    response = client.get("/info/test/id=1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}   
        