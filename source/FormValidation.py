import uvicorn
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field
from typing import List, Set, Dict

app = FastAPI(debug=True)

class Image(BaseModel):
    url : str
    name : str

class Item(BaseModel):
    name : str
    description : str = Field(None, title="Description of the item", max_length=250)
    price : float = Field(..., gt=0, le=100, description="The price must be greater than zero and must be lesser than or equal 100")
    tax : float = None
    tags: List[str] = []
    images : List[Image] = None #a list of images should be passed in
    # tags : Set[str] = [] Set removes duplicate from a list of items

class User(BaseModel):
    username : str
    full_name : str = None

class Offer(BaseModel):
    name : str
    description : str = None
    price : float
    items: List[Item]

@app.put("/get-ofer/{offer_id}")
async def get_offer(item : int, offer : Offer):
    results = {"item" : item, "offer" : offer}
    return results


@app.put("/items/{item_id}")
async def update_item(*, item_id: int, item : Item = Body(..., embed=True, example = {
    "name" : "Ayo Ade",
    "description" : "This is a brief description",
    "price" : 34.6,
    "tax" : 0.88,
    "tags" : ["me", "kola"],
    "images" : [
        {
            "url" : "https://www.imageurl.com",
            "name" : "Ajayi Image"
        },
        {
            "url" : "https://www.cloudinaryimageurl.com",
            "name" : "Nurudeen Image"
        },
    ]
})):
    results = {"item_id" : item_id, "item" : item}
    return results

@app.post("/create-post")
# key value pair key must be int in quotes while float could be int or decimal points
async def create_post(post : Dict[int, float]):
    return post



if __name__ == "__main__" :
    uvicorn.run(app, host = "127.0.0.1", port=8090)