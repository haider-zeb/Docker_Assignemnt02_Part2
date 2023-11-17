import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()
counter = os.getenv("COUNTER", 0)


@app.get("/")
def read_root():
    return JSONResponse({"Hello": "World"})

if __name__ == "__main__":
    uvicorn.run(
        "run:app",
        host="0.0.0.0",
        port=2010,
        reload=False,
    )
