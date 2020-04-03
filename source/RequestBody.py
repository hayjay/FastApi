import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(debug=True)

class Item(BaseModel):
    name : str
    description : str = None
    price : float
    tax : float = None

@app.post("/items/create")
async def create_item(item : Item):
    item_dictionary = item.dict()
    if item.tax:
        total = item.price + item.tax
        item_dictionary.update({"TotalAmount": total})
    return item_dictionary

# sample_data = {
#     "name" : "Nurudeen Ajayi",
#     "description" : "Hey whatsup?",
#     "price" : 45.00,
#     "tax" : 32.42
# }

mandatory_data = {
    "name" : "Ibrahim Niyas",
    "price" : 33.14
}

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8090)