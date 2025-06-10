from fastapi import FastAPI, Path, HTTPException
from fastapi.param_functions import Query
from pydantic import BaseModel

app = FastAPI()

@app.get("/info/{username}/{id}")
# ab hmy pasth me bhi ak string ka name or int ki id dengy to wo exces krna hoga tabhi req jaygi 
async def root(username:str,id:int=Path(...,gt=0,lt=100)):
    # ... ka matlb he required lazmi dalni he
    # prameter me path ke zariye hm validation lga skty hen ke kesy value ay hmny kha 100 tk taky osy oper na ay or 0 sy nichy na ay
    if username == "test" :
        raise HTTPException(status_code=404,detail="username Not Found")
    # HTTPException ko hm import krty hen to ismy wo sary error hoty hen 100 200 300 400 500 sb 101 201 all
    return {"username": username,"id":id}




# query perameter
@app.get("/info/all")
async def get_all_users(limit:int|None=Query(default=10,gt=0,lt=100)):
    # yani int me koch dedo or agr nhi bhi do to one dena error  nhi dena ismy pat ki jga ab query he 
    # default 10 ka matlb he na mily to 10 set krdena
    return {"message": limit}

# hm path or query ko sath bhi use kr skty hen ak perameter path me or ak ko hm query de skty hen 

# ///////////////////////////////////////////////////////////
# hm get or post alag alg method me same endpoint bna skty ehn get /name post /name
class User(BaseModel):
    id: int
    name: str
    
class UserResponse(BaseModel):
    id: int
    status: str    
@app.post("/post",response_model=UserResponse)

async def post_data(data:User):
    return {"id":data.id,"name":data.name,"status":"success"}
# hmny kioky url ki class me userresponse me id bheji he or id thi phly sy user me bhi lekin status bheja he to 
# status bhi return krwana lazmi he 

# ////////////////////////////////////////////////////////
# PUT

@app.put("/update/{id}")
async def update_data(data:User):
    return {"id":data.id,"name":data.name,"status":"success"}

# put or petch me fark ye hota he ke put ak new data lekr ata he yani jb hm update krty hen to wo phly waly ko hta kr new lata he
# patch ye he ke wo jo chiz update krny ki zarorat he sirf os chiz ko update kryga baqi sb phly jesa rhny dega 
@app.patch("/patch/{id}")
async def patch_data(data:User):
    return {"id":data.id,"name":data.name,"status":"success"}


# ////////////////////////////////////////////////////////


@app.delete("/delete/{id}")
async def delete_data(data:User):
    return {"id":data.id,"name":data.name,"status":"success"}


# uv run uvicorn main:app --reload