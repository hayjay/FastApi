import uvicorn
from fastapi import FastAPI

app = FastAPI(debug = True)

@app.get("/")
async def root() :
    return {
        "message" : "Welcome to learning fast api using python"
    }
if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port=8090)