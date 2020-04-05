'''# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World during the coronavirus pandemic!"}
'''
from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()
# to see what funny will come
app.counter = 0


class HelloResp(BaseModel):
    msg: str

#@app.get("/")
#def root():
#    return {"method": "Hello World"}


@app.get('/counter')
def counter():
    app.counter += 1
    return str(app.counter)


@app.get("/", response_model=HelloResp)
async def read_item(name: str):
    return f"{'method': HelloResp}"