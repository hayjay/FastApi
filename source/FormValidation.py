import uvicorn
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field

app = FastAPI(debug=True)

class Item(BaseModel):
    name : str
    description : str = Field(None, title="Description of the item", max_length=250)
    price : float = Field(..., gt=0, le=100, description="The price must be greater than zero and must be lesser than or equal 100")
    tax : float = None

class User(BaseModel):
    username : str
    full_name : str = None

@app.put("/items/{item_id}")
async def update_item(*, item_id: int, item : Item = Body(..., embed=True)):
    results = {"item_id" : item_id, "item" : item}
    return results

if __name__ == "__main__" :
    uvicorn.run(app, host = "127.0.0.1", port=8090)