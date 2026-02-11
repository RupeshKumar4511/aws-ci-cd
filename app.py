from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def message():
    return {"message":"Hello World"}


if __name__ == "__main__":
    
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)
