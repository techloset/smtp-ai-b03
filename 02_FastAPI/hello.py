from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root():
    return {"message": "Hello Danish, How are you?"}

@app.get("/create_user")
def get_root():
    return {"message": "I have  created a new user"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

