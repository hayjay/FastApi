from enum import Enum

import uvicorn
from fastapi import FastAPI, Query, Body #query library is a built in module from fast api for validation
from typing import List
from pydantic import BaseModel

class ModelName(str, Enum) :
    alexnet = "alex"
    resnet = "res"
    lenet = "lenet"
app=FastAPI()

app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_item(item_id : int):
#     return {"item_id" : item_id}

@app.get("/model/{model_name}")
async def get_model(model_name : ModelName) :
    if model_name == ModelName.alexnet:
        return {
            "model_name" : model_name, "message" : "Deep Learning FW"
        }
    if model_name.value == "lenet":
        return {
            "model_name" : model_name, "message" : "LeCNN all the images"
        }
    return {"model_name" : model_name, "message" : "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_user_me(file_path : str):
    return {"file_path" : file_path}

fake_items_db = [
    {"item_name" : "Foo"},
    {"item_name" : "Bar"},
    {"item_name" : "Baz"}
]

@app.get("/items/{item_id}")
async def read_item(item_id : int = 0, q : str = Query(None, max_length=10)):
    #Query(None makes the str parameter optional) and max length validates the string data not more than 10 characters
    if q :
        return {"item_id" : item_id, "q" : q}
    return {"item_id" : item_id}
    #return {"skip" : skip, "limit" : limit}

@app.get("/getitem/{item_id}")
async def read_item(item_id: str, q: str = None, short : bool = False):
    item = {"item_id" : item_id}
    if q:
        #this gets executed when user adds question mark (?) as query string to the url
        item.update({"q" : q})
    if not short:
        #this gets executed when the user didnt add short as part of the query strings in the url
        item.update({"description" : "This is an amazing item that has a long description"})
    return item

@app.get("/users/{user_id}/items/{item_id}")
#/users/4/items/maggi?q=uhiu&short=on
async def read_user_item(user_id: int, item_id: str, q: str = None, short: bool = False):
    item = {"item_id" : item_id, "user_id" : user_id};
    if q :
        item.update({"q" : q})
    if not short :
        item.update({"description" : "This is a very loooong text"})
    return item

@app.get("/items")
#items?item_id=pen&item_id=paper
#List[str] means an array of strings would be expected by the parameter
async def get_items(item_id : List[str] = Query(..., min_length=2, max_length=10)):
    results = {"items" : item_id}
    return results

class Item(BaseModel):
    name : str
    description : str = None
    price: float
    tax : float = None

class User(BaseModel):
    username: str
    full_name : str = None

# PUT METHOD passing in data via form-body
@app.put("/items_new/{item_id}")
async def update_item(*, item_id : int, item : Item, user: User, q:int =  Body(...)):
    results = {"item_id" : item_id, "item" : item, "user" : user, "q" : q}
    return results

# url/files/folder/file.txt
if __name__ == "__main__" :
    uvicorn.run(app, host = "127.0.0.1", port=8090)