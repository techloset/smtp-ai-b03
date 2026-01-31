from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def get_root():
    return {"message": "Hello Ali, How are you?"}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": "the item id is " +  str(item_id)}
