# Dependency injection
from typing import Annotated
from fastapi import FastAPI, Depends

# agr hm chahty hen ke hmary function ki functionality sy phky koch or kam ho ya chew ho wo dependency khlata he 
# depens hmar ak class he isky ander hm jo hm jo chiz pass krengy wo callable hoga or khod call ho jayga
# jesy functon kr skty hen wo callable yanii call hony wala hota he 

# dependency matlb kisi api ke ander function call krna 

app = FastAPI()

def get_user_count_from_db(limit:int = 10):
    # hm imyjo permter dery hen wo nichy waly me bhi jayga khofd yehi wala ioky ye wha chal rha he 
   return 100

def get_user_count_from_db2(limit:int = 10):
    # hm imyjo permter dery hen wo nichy waly me bhi jayga khofd yehi wala ioky ye wha chal rha he 
   return 100

@app.get("/items")
async def read_item(user_count:Annotated[int , Depends(get_user_count_from_db)]):
    # is waly function ke return sy phly perameter wala function ka return chalyga
    return {"user_count": user_count}
    
    
@app.get("/items")
async def read_item_multiple(user_count:Annotated[int , Depends(get_user_count_from_db)],user_count2:Annotated[int , Depends(get_user_count_from_db2)]):
    
    total=user_count+user_count2
    return {"user_count":   total}  

# multiple bhi kr skty hen call  
    